from __future__ import annotations

from som_gui.plugins.aggregation_window import tool as aw_tool
from som_gui.plugins.aggregation_window.core import connection as core


def connect():
    pass


def on_new_project():
    pass


def paint_connection(connection):
    core.paint_connection(connection, aw_tool.Connection)


def retranslate_ui():
    pass
