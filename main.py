"""
Ciallo Widget
Pop up Ciallo every morning.
"""

from ClassWidgets.SDK import CW2Plugin, PluginAPI

import src

class Plugin(CW2Plugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        self.notification_provider = None
        self.provider_id = str(self.pid)
        
        # 请在此导入第三方库 / Import third-party libraries here


    def on_load(self):
        super().on_load()
        self.notification_provider = self.api.notification.register_provider(
            provider_id = self.provider_id,
            name = src.name,
            icon = src.icon,
            use_system_notify = True
        )
        self.api.widgets.register(
            widget_id = src.widget_id,
            name = src.name,
            qml_path = src.qml_path / "widget.qml",
            settings_qml = src.qml_path / "settings.qml",
            backend_obj = self,
            default_settings = {
                "target_title": "Welcome",
                "target_text": "Ciallo～(∠・ω< )⌒★",
                "display_in_class": False,  # 是否在非下课时段显示
            }
        )
        print(f"Ciallo Widget loaded")

    def on_unload(self):
        print(f"Ciallo Widget unloaded")
