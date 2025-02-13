from __future__ import annotations

from curses import (
    A_BOLD,
)
from datetime import datetime
from typing import TYPE_CHECKING


from cursedtodo.config import Config
from cursedtodo.utils.colors import RED
from cursedtodo.utils.formater import Formater
from cursedtodo.utils.time import TimeUtil
from cursedtodo.utils.window_utils import add_borders, draw_line
from cursedtodo.views.base_view import BaseView

if TYPE_CHECKING:
    from cursedtodo.controlers.view_todo_controller import ViewTodoController


class ViewTodoView(BaseView):
    def __init__(self, controller: ViewTodoController) -> None:
        super().__init__(controller)
        self.controller = controller

    def render(self) -> None:
        self.height, self.length = self.window.getmaxyx()
        todo = self.controller.todo
        self.window.erase()
        self.window.border()
        add_borders(self.window)
        self.window.addstr(self.height - 1, 5, " q: go back ")
        self.window.addstr(0, 5, todo.summary)

        line = 1

        self.window.addstr(line, 1, "Liste: ", A_BOLD)
        self.window.addstr(todo.calendar.name, todo.calendar.color_attr)
        line += 1

        self.window.addstr(line, 1, "Priority: ", A_BOLD)
        text, color = Formater.formatPriority(todo.priority)
        self.window.addstr(text, color)
        line += 1

        if todo.completed:
            self.window.addstr(line, 1, "Completed: ", A_BOLD)
            self.window.addstr(f"{todo.completed.strftime(Config.ui.date_format)}")
            line += 1

        if todo.due:
            self.window.addstr(line, 1, "Due: ", A_BOLD)
            local_tz = TimeUtil.get_locale_tz()
            color = (
                RED if todo.due.replace(tzinfo=local_tz) < datetime.now(local_tz) else 0
            )
            self.window.addstr(f"{todo.due.strftime(Config.ui.date_format)}", color)
            line += 1

        if todo.categories and len(todo.categories) > 0:
            self.window.addstr(line, 1, "Categories: ", A_BOLD)
            self.window.addstr(", ".join(todo.categories or []))
            line += 1

        if todo.location and len(todo.location) > 0:
            self.window.addstr(line, 1, "Location: ", A_BOLD)
            self.window.addstr(todo.location)
            line += 1

        if todo.description:
            draw_line(self.window, line, self.length)
            line += 1
            self.window.addstr(line, 1, "Description: ", A_BOLD)
            line += 1
            i = 0
            for i, description_line in enumerate(todo.description.splitlines()):
                self.window.addstr(line + i, 1, description_line)
            line = line + i

        self.window.refresh()

    def main_loop(self) -> None:
        while True:
            k = self.window.getch()
            if self.controller.handle_key(k):
                break
