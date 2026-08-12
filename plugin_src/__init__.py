from pathlib import Path
from .configuration import Config

widget_id = "top.purrbyte.ciallo-widget"
name = "Ciallo Widget"
description = "Pop up Ciallo every morning."

root_path = Path(__file__).parent

icon = root_path / "icon.png"
qml_path = root_path / "qml"

__all__ = ["Config", "widget_id", "name", "description", "icon", "qml_path"]

print("Debug: plugin_src.__init__ successfully run.")