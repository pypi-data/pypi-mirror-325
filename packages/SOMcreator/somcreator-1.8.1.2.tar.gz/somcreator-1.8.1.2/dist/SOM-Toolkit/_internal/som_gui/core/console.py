from __future__ import annotations

from typing import TYPE_CHECKING, Type

from PySide6.QtWidgets import QPushButton

if TYPE_CHECKING:
    from som_gui import tool


def create_console_trigger(main_menu: Type[tool.MainWindow], console: Type[tool.Console]):
    status_bar = main_menu.get_statusbar()
    button = QPushButton("C")
    button.setMaximumWidth(24)
    status_bar.addPermanentWidget(button)
    button.clicked.connect(lambda: show(console))


def show(console: Type[tool.Console]):
    console.create_console()


def close(console: Type[tool.Console]):
    console.close_console()
