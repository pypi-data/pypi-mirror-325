from __future__ import annotations

from collections import Counter
import random

from typing_extensions import Any, ClassVar, Final, Iterator, cast, no_type_check, override

from .utils import SetupOptions, unreachable


class Card(int):
    '''An individual playing card. Subclass of int for simplicity.'''

    rank: str

    def __new__(cls, rank: str) -> Card:
        value: int
        if rank == 'A':
            value = 1
        elif rank in 'JQK':
            value = 10
        else:
            value = int(rank)
        self: Card = super().__new__(cls, value)
        self.rank = rank
        return self

    def __str__(self) -> str:
        return str(self.rank)


CARDSET = [
    Card('A'),
    Card('2'),
    Card('3'),
    Card('4'),
    Card('5'),
    Card('6'),
    Card('7'),
    Card('8'),
    Card('9'),
    Card('10'),
    Card('J'),
    Card('Q'),
    Card('K'),
]

DECK: Final[list[Card]] = CARDSET * 4


class Shoe:

    def __init__(self, *, decks: int = 6):
        self.decks: int = decks
        self.cards: list[Card] = []
        self.cut: int = 0
        self.new()

    def deal(self) -> Card:
        return self.cards.pop()

    def needs_shuffle(self) -> bool:
        return len(self.cards) <= self.cut

    def new(self) -> None:
        self.cards = DECK * self.decks
        random.shuffle(self.cards)
        if self.decks == 1:
            self.cut = len(self.cards) // 2
        else:
            self.cut = len(self.cards) // 4
        self.cut += random.randint(self.decks * -4, self.decks * 4)

    def __getstate__(self) -> tuple[int, dict[str, int], int, int]:
        version = 1
        counter = Counter(card.rank for card in self.cards)
        return (version, dict(counter), self.decks, self.cut)

    def __setstate__(self, state: tuple[Any, ...]) -> None:
        match state:
            case (1, dict() as counter, int() as decks, int() as cut):
                self.decks = decks
                self.cut = cut
                self.cards = []
                for rank, count in cast(dict[str, int], counter).items():
                    self.cards.extend([Card(rank)] * count)
                random.shuffle(self.cards)
            case _:
                unreachable()


class Hand(list[Card]):

    def __init__(self, *, bet: int) -> None:
        super().__init__()
        self.bet: int = bet

    def hard_total(self) -> int:
        return sum(self)

    def soft_total(self) -> int | None:
        total = self.hard_total()
        if total > 11 or 1 not in self:
            return None
        return total + 10

    def total(self) -> int:
        return self.soft_total() or self.hard_total()

    def is_blackjack(self) -> bool:
        return len(self) == 2 and self.total() == 21

    def is_busted(self) -> bool:
        return self.hard_total() > 21

    def hit_from_shoe(self, shoe: Shoe) -> None:
        self.append(shoe.deal())

    def reset(self) -> None:
        self.clear()


class Dealer(Hand):

    def __init__(self, shoe: Shoe, hit_soft_17: bool = True):
        super().__init__(bet=0)
        self.hard_stand: Final[int] = 17
        self.soft_stand: Final[int] = 18 if hit_soft_17 else 17
        self.downcard: bool = True
        self.shoe: Shoe = shoe

    def has_ace_up(self) -> bool:
        return self[1] == 1

    def hit(self) -> None:
        self.hit_from_shoe(self.shoe)

    def flip(self) -> None:
        assert self.downcard is True
        self.downcard = False

    @override
    def reset(self) -> None:
        super().reset()
        self.downcard = True

    def __getstate__(self) -> tuple[int, int]:
        super().reset()
        version = 1
        return (version, self.soft_stand)

    @no_type_check
    def __setstate__(self, state: tuple[Any, ...]) -> None:
        super().__init__(bet=0)
        match state:
            case (1, int() as soft_stand):
                self.soft_stand = soft_stand
            case _:
                unreachable()
        self.hard_stand = 17


class Player:
    _id: ClassVar[int] = 0

    def __init__(
        self,
        shoe: Shoe,
        name: str,
        chips: int = 1000,
    ):
        self.__class__._id += 1
        self.name: Final[str] = name
        self.chips: int = chips
        self.bet: int = 0
        self.insurance: int | None = None
        self.hands: list[Hand] = []
        self.active_hand_index: int = 0
        self.shoe: Shoe = shoe

    def __iter__(self) -> Iterator[tuple[int, Hand]]:
        while self.active_hand_index < len(self.hands):
            yield (self.active_hand_index + 1, self.active_hand)
            self.active_hand_index += 1
        # cleanup
        self.active_hand_index = 0

    @property
    def active_hand(self) -> Hand:
        return self.hands[self.active_hand_index]

    def is_split(self) -> bool:
        return len(self.hands) > 1

    def can_afford_double(self) -> bool:
        return self.chips >= self.bet

    def has_blackjack(self) -> bool:
        return not self.is_split() and self.active_hand.is_blackjack()

    def hit(self) -> None:
        self.active_hand.hit_from_shoe(self.shoe)

    def can_split(self) -> bool:
        hand: Hand = self.active_hand
        return len(hand) == 2 and hand[0].rank == hand[1].rank

    def split(self) -> None:
        assert self.can_afford_double()
        assert self.can_split()
        self.chips -= self.bet
        new_hand = Hand(bet=self.bet)
        new_hand.append(self.active_hand.pop())
        self.hands.append(new_hand)
        self.active_hand.hit_from_shoe(self.shoe)

    def can_double(self) -> bool:
        return (len(self.active_hand) == 2
                and 9 <= self.active_hand.total() <= 11)

    def double_down(self) -> None:
        assert self.can_afford_double()
        assert len(self.active_hand) == 2
        self.chips -= self.active_hand.bet
        self.active_hand.bet *= 2
        self.active_hand.hit_from_shoe(self.shoe)

    def surrender(self) -> None:
        assert len(self.active_hand) == 2
        self.chips += self.bet // 2

    def can_afford_insurance(self) -> bool:
        return self.chips >= self.bet // 2

    def buy_insurance(self) -> None:
        assert self.can_afford_insurance()
        self.insurance = self.bet // 2
        self.chips -= self.insurance

    def reset(self) -> None:
        self.hands.clear()
        self.active_hand_index = 0
        self.insurance = None

    def __getstate__(self) -> tuple[int, str, int]:
        version = 1
        return (version, self.name, self.chips)

    @no_type_check
    def __setstate__(self, state: tuple[Any, ...]) -> None:
        match state:
            case (1, str() as name, int() as chips):
                self.name = name
                self.chips = chips
            case _:
                unreachable()
        self.bet = 0
        self.insurance = None
        self.hands = []
        self.active_hand_index = 0


class Game:

    def __init__(self, options: SetupOptions):
        self.shoe: Final[Shoe] = Shoe(decks=options.decks)
        self.dealer: Final[Dealer] = Dealer(self.shoe, hit_soft_17=options.hit_soft_17)
        self.players: Final[list[Player]] = [
            Player(self.shoe, name, options.starting_chips)
            for name in options.player_names
        ]
        self.active_players: list[Player] = []

    def activate_player(self, player: Player) -> None:
        self.active_players.append(player)

    def deactivate_player(self, player: Player) -> None:
        self.active_players.remove(player)

    def __getstate__(self) -> tuple[int, Dealer, list[Player], Shoe]:
        version = 1
        return (version, self.dealer, self.players, self.shoe)

    @no_type_check
    def __setstate__(self, state: tuple[Any, ...]) -> None:
        match state:
            case (1, Dealer() as dealer, list() as players, Shoe() as shoe):
                # Dealer, list[Player], Shoe
                self.dealer = dealer
                self.players = cast(list[Player], players)
                self.shoe = shoe
            case _:
                unreachable()
        self.dealer.shoe = self.shoe
        for player in self.players:
            player.shoe = self.shoe
        self.active_players = []
