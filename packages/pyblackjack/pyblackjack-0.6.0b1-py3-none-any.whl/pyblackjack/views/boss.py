import os

from blessed import Terminal
from typing_extensions import Final, Literal, cast, overload, override

from ..model import Dealer, Hand, Player
from ..utils import Action, SetupOptions, SAVE_DIR, SAVE_EXT, StartOption
from ._abc import AbstractBlackjackView, PlayerQuit, SaveGame


DIVIDER_LENGTH: Final[int] = 10

ACTIONS_BY_LETTER: dict[str, Action] = {
    "h": Action.HIT,
    "s": Action.STAND,
    "p": Action.SPLIT,
    "d": Action.DOUBLE_DOWN,
    "u": Action.SURRENDER,
}

START_OPTIONS_BY_LETTER: dict[str, StartOption] = {
    "n": StartOption.NEW_GAME,
    "l": StartOption.LOAD_GAME,
}

LETTERS_BY_ACTION: dict[Action, str] = {}
for letter, action in ACTIONS_BY_LETTER.items():
    LETTERS_BY_ACTION[action] = letter

LETTERS_BY_START_OPTION: dict[StartOption, str] = {}
for letter, option in START_OPTIONS_BY_LETTER.items():
    LETTERS_BY_START_OPTION[option] = letter

ACTION_WORDS: dict[Action, str] = {
    Action.HIT: "[H]it",
    Action.STAND: "[S]tand",
    Action.SPLIT: "S[p]lit",
    Action.DOUBLE_DOWN: "[D]ouble down",
    Action.SURRENDER: "S[u]rrender",
}

START_OPTION_WORDS: dict[StartOption, str] = {
    StartOption.NEW_GAME: "[N]ew game",
    StartOption.LOAD_GAME: "[L]oad saved game",
}


class BlackjackView(AbstractBlackjackView):  # pylint: disable=too-many-public-methods

    def __init__(self) -> None:
        super().__init__()
        self.term = Terminal()

    @override
    def get_setup_options(self) -> SetupOptions:
        print("Welcome to PyBlackjack!")
        numplayers = cast(
            int | Literal["q"],
            self._get_int("Enter number of players [1-6] or [q]uickstart: ", 1,
                            6, "q"))
        if numplayers == "q":
            return SetupOptions()

        players: list[str] = []
        for n in range(numplayers):
            name: str = self._get_str(f"Enter name for player {n + 1}: ")
            players.append(name)
        chips: int = self._get_int("Enter starting chips: ", min=1)
        decks: int = self._get_int("Enter number of decks in the shoe: ", 1, 8)
        hit_soft_17: bool = self._get_yes_no("Should dealer hit on soft 17?")

        return SetupOptions(
            player_names=players,
            starting_chips=chips,
            decks=decks,
            hit_soft_17=hit_soft_17,
        )

    @override
    def get_bet(self, player: Player, *, save: bool = False) -> int:
        print(f"{player.name} has {player.chips} chips.")
        save_text = ", [s]ave," if save else ""
        bet = cast(
            int | Literal["q", "s"],
            self._get_int(f"Enter a bet{save_text} or [q]uit: ", 0, player.chips,
                            "qs"))
        if bet == "q":
            raise PlayerQuit
        if bet == "s":
            raise SaveGame
        return bet

    @override
    def get_insurance_option(self, player: Player) -> bool:
        return self._get_yes_no(f"{player.name}: Buy insurance?")

    @override
    def get_action(self, actions: Action,
                   lowchips: Action = Action(0)) -> Action:
        text = ", ".join(ACTION_WORDS[action] for action in actions) + "? "
        letters = "".join(LETTERS_BY_ACTION[action] for action in actions)
        lowchips_letters = "".join(LETTERS_BY_ACTION[action]
                                   for action in lowchips)
        choice = self._get_action(text,
                                  options=letters,
                                  lowchips=lowchips_letters)
        return ACTIONS_BY_LETTER[choice]

    @override
    def get_start_option(self) -> StartOption:
        choice = self._get_action("[N]ew game or [L]oad saved game? ",
                                  options="nl",
                                  lowchips="")
        return START_OPTIONS_BY_LETTER[choice]

    @override
    def display_player_hand(self, player: Player, i: int) -> None:
        assert i > 0
        hand_number: str = f" (hand {i})" if player.is_split() else ""
        hand: Hand = player.hands[i - 1]
        card_text: str = " ".join(str(card) for card in hand)
        print(
            f"{player.name}{hand_number}: {card_text} ({hand.total()})"
        )

    @override
    def display_dealer_hand(self, dealer: Dealer) -> None:
        print("Dealer: ", end="")
        cards = [str(card) for card in dealer]
        if dealer.downcard:
            cards[0] = "[]"
            print(" ".join(cards))
        else:
            print(f"{' '.join(cards)} ({dealer.total()})")

    @override
    def display_bet(self, player: Player) -> None:
        pass

    @override
    def display_blackjack(self, player: Player) -> None:
        print(f"{player.name} has blackjack!")

    def _hand_index_message(self, player: Player, i: int, /) -> str:
        assert i > 0
        return f" on hand {i}" if player.is_split() else ""

    @override
    def display_win(self, player: Player, i: int) -> None:
        msg = self._hand_index_message(player, i)
        print(f"{player.name} wins{msg}!")

    @override
    def display_push(self, player: Player, i: int) -> None:
        msg = self._hand_index_message(player, i)
        print(f"{player.name} pushes{msg}.")

    @override
    def display_loss(self, player: Player, i: int) -> None:
        msg = self._hand_index_message(player, i)
        print(f"{player.name} loses{msg}.")

    @override
    def display_bust(self, player: Player, i: int) -> None:
        msg = self._hand_index_message(player, i)
        print(f"{player.name} busted{msg}!")

    @override
    def display_dealer_bust(self, dealer: Dealer) -> None:
        pass

    @override
    def display_dealer_blackjack(self, dealer: Dealer) -> None:
        print("Dealer has blackjack!")

    @override
    def display_new_hand(self, *, new_shoe: bool = False) -> None:
        print("=" * DIVIDER_LENGTH)
        if new_shoe:
            print("New shoe in play!")
            print("=" * DIVIDER_LENGTH)

    @override
    def display_start_of_actions(self) -> None:
        print("-" * DIVIDER_LENGTH)

    @override
    def display_end_of_actions(self) -> None:
        print("-" * DIVIDER_LENGTH)

    @override
    def display_player_elimination(self, player: Player) -> None:
        print(f"{player.name} is out of chips and is eliminated.")

    @override
    def display_exit(self) -> None:
        print("Thanks for playing!")

    @override
    def get_save_filename(self) -> str:
        return self._get_str("Enter filename: ")

    @override
    def confirm_overwrite(self) -> bool:
        return self._get_yes_no("File exists. Overwrite?")

    @override
    def get_load_game(self) -> str | None:
        save_files: list[str] = []
        for _, _, files in os.walk(SAVE_DIR):
            for filename in files:
                if not filename.endswith(SAVE_EXT):
                    continue
                save_files.append((filename))
        if len(save_files) == 0:
            print("No saved games found. Starting a new game instead.")
            return None
        save_files.sort()
        for n, filename in enumerate(save_files, start=1):
            print(f"{n:>3}: {filename.removesuffix(SAVE_EXT)}")
        file_num = cast(
            int | Literal["n"],
            self._get_int("Select file by number or [n]ew game: ",
                          min=1,
                          max=len(save_files),
                          alt="n"))
        if file_num == "n":
            return None
        return save_files[file_num - 1]

    def _error(self, message: str, /) -> None:
        print(f"Error: {message} Try again.")

    def _get_str(self, prompt: str, /) -> str:
        while True:
            s: str = input(prompt).strip()
            if s:
                return s
            else:
                self._error("Input required.")

    def _get_action(self, prompt: str, /, options: str, lowchips: str) -> str:
        while True:
            print(prompt, end="", flush=True)
            with self.term.cbreak():
                s: str = self.term.inkey().lower()
            print()
            if s in options:
                return s
            elif s in lowchips:
                self._error("Insufficient chips for that action.")
            else:
                self._error("Invalid input.")

    def _get_yes_no(self, prompt: str, /) -> bool:
        while True:
            s: str = self._get_action(f"{prompt} [y/n]: ", "yn", "")
            return s == "y"

    @overload
    def _get_int(self,
                 prompt: str,
                 /,
                 min: int | None = None,
                 max: int | None = None,
                 alt: None = None) -> int:
        ...

    @overload
    def _get_int(self,
                 prompt: str,
                 /,
                 min: int | None = None,
                 max: int | None = None,
                 alt: str = "") -> int | str:
        ...

    def _get_int(self,
                 prompt: str,
                 /,
                 min: int | None = None,
                 max: int | None = None,
                 alt: str | None = None) -> int | str:
        while True:
            s: str = self._get_str(prompt).lower()
            if alt and s.lower() in alt.lower():
                return s.lower()
            try:
                z: int = int(s)
            except ValueError:
                self._error("Invalid integer.")
                continue
            if min is not None and z < min:
                self._error(f"Integer must be at least {min}.")
                continue
            if max is not None and max < z:
                self._error(f"Integer must be at most {max}.")
                continue
            return z
