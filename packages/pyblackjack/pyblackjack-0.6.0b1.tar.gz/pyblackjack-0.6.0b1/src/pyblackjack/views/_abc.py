from abc import abstractmethod

from ..utils import Action, SetupOptions, StartOption
from ..model import Dealer, Player


class PlayerQuit(Exception):
    pass


class SaveGame(Exception):
    pass


class AbstractBlackjackView:  # pylint: disable=too-many-public-methods

    @abstractmethod
    def get_setup_options(self) -> SetupOptions:
        raise NotImplementedError

    @abstractmethod
    def get_bet(self, player: Player, *, save: bool = False) -> int:
        """Raises PlayerQuit if player indicates a quit.

        Raises SaveGame if player indicates to save the game."""
        raise NotImplementedError

    @abstractmethod
    def get_insurance_option(self, player: Player) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_action(self, actions: Action,
                   lowchips: Action = Action(0)) -> Action:
        raise NotImplementedError

    @abstractmethod
    def get_start_option(self) -> StartOption:
        raise NotImplementedError

    @abstractmethod
    def display_player_hand(self, player: Player, i: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_dealer_hand(self, dealer: Dealer) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_bet(self, player: Player) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_blackjack(self, player: Player) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_win(self, player: Player, i: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_push(self, player: Player, i: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_loss(self, player: Player, i: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_bust(self, player: Player, i: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_dealer_bust(self, dealer: Dealer) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_dealer_blackjack(self, dealer: Dealer) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_new_hand(self, *, new_shoe: bool = False) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_start_of_actions(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_end_of_actions(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_player_elimination(self, player: Player) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_exit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_save_filename(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def confirm_overwrite(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_load_game(self) -> str | None:
        raise NotImplementedError
