from som_gui import tool
from som_gui.plugins.aggregation_window import tool as aw_tool
from som_gui.plugins.aggregation_window.core import modelcheck as core


def connect():
    core.add_modelcheck_plugin(tool.Modelcheck, aw_tool.Modelcheck)


def on_new_project():
    pass


def retranslate_ui():
    pass
