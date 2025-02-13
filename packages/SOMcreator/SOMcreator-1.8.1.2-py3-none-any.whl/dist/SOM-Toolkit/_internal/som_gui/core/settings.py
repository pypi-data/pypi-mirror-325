from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Type

from PySide6.QtCore import QCoreApplication

from som_gui import tool

if TYPE_CHECKING:
    from som_gui import tool


def create_main_menu_actions(settings: Type[tool.Settings], main_window: Type[tool.MainWindow]) -> None:
    from som_gui.module.settings import trigger
    action = main_window.add_action("menuEdit", "Settings", trigger.open_window)
    settings.set_action("open_window", action)


def retranslate_ui(settings: Type[tool.Settings], util: Type[tool.Util]):
    open_window_action = settings.get_action("open_window")
    title = QCoreApplication.translate('Settings', "Settings")

    open_window_action.setText(title)
    widget = settings.get_widget()
    if widget:
        widget.ui.retranslateUi(widget)
        widget.setWindowTitle(util.get_window_title(title))


def open_window(settings: Type[tool.Settings]):
    logging.info(f"Opening Settings Window")
    dialog = settings.create_dialog()
    from som_gui.module.settings import trigger
    trigger.retranslate_ui()
    if dialog.exec():
        for func in settings.get_accept_functions():
            func()
    settings.close()
