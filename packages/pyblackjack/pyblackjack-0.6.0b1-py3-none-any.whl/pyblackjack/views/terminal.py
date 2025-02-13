import sys

from typing_extensions import override

from . import boss
from ..utils import SAVE_DIR


class BlackjackView(boss.BlackjackView):

    def __init__(self) -> None:
        super().__init__()
        # pylint: disable-next=consider-using-with
        sys.stderr = open(SAVE_DIR / "stderr.log", "w", encoding="utf-8")
        self._print_codes(
            self.term.enter_fullscreen,
            self.term.home,
            self.term.black_on_green,
            self.term.clear,
        )

    def __del__(self) -> None:
        self._print_codes(self.term.exit_fullscreen)
        sys.stderr.close()

    @override
    def display_exit(self) -> None:
        super().display_exit()
        print("Press any key to exit...")
        with self.term.cbreak():
            self.term.inkey()

    def _print_codes(self, *codes: str) -> None:
        for code in codes:
            print(code, end="", flush=True)
