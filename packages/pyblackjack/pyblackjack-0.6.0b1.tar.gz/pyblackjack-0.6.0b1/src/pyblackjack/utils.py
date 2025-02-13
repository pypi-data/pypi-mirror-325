from __future__ import annotations

from dataclasses import dataclass
from enum import Flag, auto
from pathlib import Path
import sys

from typing_extensions import Final, Generator, Never, Sequence

SAVE_DIR: Final[Path] = Path.home() / ".pyblackjack"
SAVE_EXT: Final[str] = ".pybj"


class Action(Flag):
    HIT = auto()
    STAND = auto()
    SPLIT = auto()
    DOUBLE_DOWN = auto()
    SURRENDER = auto()

    if sys.version_info < (3, 11):
        def __iter__(self) -> Generator[Action]:
            for action in Action:
                if action in self:
                    yield action


class StartOption(Flag):
    NEW_GAME = auto()
    LOAD_GAME = auto()

    if sys.version_info < (3, 11):
        def __iter__(self) -> Generator[Action]:
            for action in Action:
                if action in self:
                    yield action


@dataclass
class SetupOptions:
    player_names: Sequence[str] = ("Player 1",)
    starting_chips: int = 1000
    decks: int = 1
    hit_soft_17: bool = True


def unreachable() -> Never:
    raise RuntimeError("pyblackjack internal error: unreachable code reached")
