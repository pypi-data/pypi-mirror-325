import argparse
import importlib
import pickle
import pickletools

from typing_extensions import assert_never, cast

from .model import Game, Hand, Player
from .utils import SAVE_DIR, SAVE_EXT, Action, StartOption
from .views._abc import AbstractBlackjackView, PlayerQuit, SaveGame


class BlackjackController:

    game: Game
    view: AbstractBlackjackView

    def __init__(self, view: AbstractBlackjackView):
        self.view = view

    def mainloop(self) -> None:
        while self.play_hand():
            pass

    def play_hand(self) -> bool:
        new_shoe = self.game.shoe.needs_shuffle()
        self.view.display_new_hand(new_shoe=new_shoe)
        if new_shoe:
            self.game.shoe.new()
        self.game.active_players.clear()
        self.collect_bets()
        if not self.game.players:
            return False
        self.deal_cards()
        self.display_hands()
        self.view.display_start_of_actions()
        if self.check_dealer_blackjack():
            return True
        self.check_player_blackjacks()
        for player in self.game.active_players.copy():
            self.play_player_hand(player)
        self.view.display_end_of_actions()
        if self.game.active_players:
            self.play_dealer_hand()
            self.pay_winners()
        else:
            self.game.dealer.flip()
            self.view.display_dealer_hand(self.game.dealer)
        return True

    def collect_bets(self) -> None:
        for player in self.game.players.copy():
            player.reset()
            self.get_bet(player)

    def get_bet(self, player: Player) -> None:
        player.hands = []
        if player.chips == 0:
            self.view.display_player_elimination(player)
            self.game.players.remove(player)
            return
        try:
            bet = self.view.get_bet(player,
                                    save=player is self.game.players[0])
        except SaveGame:
            self.save_game()
            try:
                bet = self.view.get_bet(player, save=False)
            except PlayerQuit:
                self.game.players.remove(player)
                return
        except PlayerQuit:
            self.game.players.remove(player)
            return
        player.bet = bet
        if bet > 0:
            player.chips -= bet
            self.game.active_players.append(player)
            player.hands.append(Hand(bet=bet))

    def deal_cards(self) -> None:
        self.game.dealer.reset()
        for _ in range(2):
            for hand in self.game.active_players + [self.game.dealer]:
                hand.hit()

    def display_hands(self) -> None:
        self.view.display_dealer_hand(self.game.dealer)
        for player in self.game.active_players:
            self.view.display_player_hand(player, 1)

    def check_dealer_blackjack(self) -> bool:
        if self.game.dealer.has_ace_up():
            self.handle_insurance()
        if self.game.dealer.is_blackjack():
            self.game.dealer.flip()
            self.view.display_dealer_hand(self.game.dealer)
            self.resolve_dealer_blackjack()
            return True
        for player in self.game.active_players:
            player.insurance = None
        return False

    def handle_insurance(self) -> None:
        for player in self.game.active_players:
            if (player.can_afford_insurance()
                    and self.view.get_insurance_option(player)):
                player.buy_insurance()

    def resolve_dealer_blackjack(self) -> None:
        self.view.display_dealer_blackjack(self.game.dealer)
        for player in self.game.active_players:
            if player.insurance:
                player.chips += player.insurance * 3
                player.insurance = None
            if player.has_blackjack():
                self.view.display_blackjack(player)
                player.chips += player.bet
        self.game.active_players.clear()

    def check_player_blackjacks(self) -> None:
        for player in self.game.active_players.copy():
            if player.has_blackjack():
                self.view.display_blackjack(player)
                player.chips += int(player.bet * 2.5)
                self.game.active_players.remove(player)

    def play_player_hand(self, player: Player) -> None:
        for _ in player:
            self.play_single_hand(player)
        hands_busted: list[bool] = [hand.is_busted() for _, hand in player]
        if all(hands_busted):
            self.game.active_players.remove(player)

    def play_single_hand(self, player: Player) -> None:
        hand: Hand = player.active_hand
        i: int = player.active_hand_index + 1
        if len(hand) == 1:
            # split hand
            player.hit()
        while not hand.is_busted():
            self.view.display_player_hand(player, i)
            if player.is_split() and hand[0] == 1:
                # split aces auto-stand
                break
            if hand.total() == 21:
                # 21 auto-stands
                break
            action: Action = self.get_action(player, hand)
            if not self.perform_action(action, player):
                break
        else:
            self.view.display_player_hand(player, i)
            self.view.display_bust(player, i)

    def get_action(self, player: Player, hand: Hand) -> Action:
        action_set: Action = Action.HIT | Action.STAND
        low_chips_set: Action = Action(0)
        if len(hand) == 2:
            if player.can_split():
                if player.can_afford_double():
                    action_set |= Action.SPLIT
                else:
                    low_chips_set |= Action.SPLIT
            if player.can_double():
                if player.can_afford_double():
                    action_set |= Action.DOUBLE_DOWN
                else:
                    low_chips_set |= Action.DOUBLE_DOWN
            if not player.is_split():
                action_set |= Action.SURRENDER
        return self.view.get_action(action_set, low_chips_set)

    def perform_action(self, action: Action, player: Player) -> bool:
        match action:
            case Action.HIT:
                player.hit()
                return True
            case Action.STAND:
                return False
            case Action.SPLIT:
                player.split()
                return True
            case Action.DOUBLE_DOWN:
                player.double_down()
                self.view.display_player_hand(player, player.active_hand_index + 1)
                return False
            case Action.SURRENDER:
                player.surrender()
                self.game.active_players.remove(player)
                return False
            case unreachable:
                assert_never(unreachable)

    def play_dealer_hand(self) -> None:
        dealer = self.game.dealer
        dealer.flip()
        while True:
            soft_total: int | None = dealer.soft_total()
            if ((soft_total and soft_total >= dealer.soft_stand)
                    or dealer.hard_total() >= dealer.hard_stand):
                break
            dealer.hit()
        self.view.display_dealer_hand(dealer)

    def pay_winners(self) -> None:
        for player in self.game.active_players:
            self.resolve_player_hands(player)

    def resolve_player_hands(self, player: Player) -> None:
        hand: Hand
        for index, hand in player:
            if hand.is_busted():
                continue
            if (self.game.dealer.is_busted()
                    or hand.total() > self.game.dealer.total()):
                player.chips += hand.bet * 2
                self.view.display_win(player, index)
            elif hand.total() == self.game.dealer.total():
                player.chips += hand.bet
                self.view.display_push(player, index)
            else:
                self.view.display_loss(player, index)

    def save_game(self, filename: str | None = None, /) -> None:
        if not SAVE_DIR.exists():
            SAVE_DIR.mkdir()
        if filename is None:
            filename = self.view.get_save_filename()
        path = SAVE_DIR / f"{filename}{SAVE_EXT}"
        if path.exists():
            if not self.view.confirm_overwrite():
                return
        pkl: bytes = pickle.dumps(self.game)
        pkl = pickletools.optimize(pkl)
        path.write_bytes(pkl)

    def load_game(self) -> None:
        filename = self.view.get_load_game()
        if filename is None:
            self.game = Game(self.view.get_setup_options())
            return
        else:
            with (SAVE_DIR / filename).open("rb") as file:
                self.game = cast(Game, pickle.load(file))

    def main(self) -> int:
        match self.view.get_start_option():
            case StartOption.NEW_GAME:
                self.game = Game(self.view.get_setup_options())
            case StartOption.LOAD_GAME:
                self.load_game()
            case unreachable:
                assert_never(unreachable)
        # For debugging: stack cards to top to reproduce bugs
        #                            D   P1B  P1A  P1A  Dup  P1B  Ddn  P1A
        #stacked_cards: list[str] = ["9", "A", "J", "5", "K", "8", "6", "8"]
        #from .model import Card
        #for rank in stacked_cards:
        #    self.game.shoe.cards.append(Card(rank))
        self.mainloop()
        self.view.display_exit()
        return 0

def entrypoint() -> int:
    parser = argparse.ArgumentParser()
    view_group = parser.add_mutually_exclusive_group(required=False)
    view_group.add_argument("--boss",
                            const="boss",
                            action="store_const",
                            dest="view")
    view_group.add_argument("-v", "--view", action="store", dest="view")
    parser.set_defaults(view="terminal")
    args = parser.parse_args()
    view_mod = importlib.import_module(f"pyblackjack.views.{args.view}")
    controller = BlackjackController(view_mod.BlackjackView())
    return controller.main()
