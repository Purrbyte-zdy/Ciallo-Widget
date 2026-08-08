from pathlib import Path

widget_id = "top.purrbyte.ciallo-widget"
name = "Ciallo Widget"
description = "Pop up Ciallo every morning."

root_path = Path(__file__).parent

icon = root_path / "icon.png"
qml_path = root_path / "qml"