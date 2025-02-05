from collections.abc import Callable
from curses import A_BOLD, KEY_RESIZE, window

from cursedtodo.utils.colors import WHITE
from cursedtodo.utils.editor import Editor
from cursedtodo.views.form.base_field import BaseField


class TextArea(BaseField):
    def __init__(
        self,
        y: int,
        window: window,
        name: str,
        id: str,
        validator: Callable[[int | str], int | str],
        value: str | None = None,
    ):
        super().__init__(y, window, name, id, validator, value)
        # TODO: Make that fixed height dynamic
        self.textwindow = window.derwin(7, 100, y + 1, 1)
        self.textwindow.bkgd(" ", WHITE)
        self.value: str = str(value)
        self.validator = validator
        self.editor = Editor(self.textwindow, self.value or "", self._validator)

    def _validator(self, ch: str | int) -> str | int:
        if ch == KEY_RESIZE:
            self.value = self.editor.gather()
        self.validator(ch)
        return ch

    def render(self) -> None:
        self.window.addstr(self.y, 1, f"{self.name}: ", A_BOLD)
        self.textwindow.move(0, 0)
        self.editor.set_value(self.value or "")
        self.editor.render()
        # Editor().main(self.textwindow,self.value or "")

    def focus(self) -> None:
        self.editor.main()
        self.value = self.editor.gather()
