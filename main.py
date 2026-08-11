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
        self.current_statue = self.api.runtime.current_status
        
        # 请在此导入第三方库 / Import third-party libraries here


    def on_load(self):
        super().on_load()
        self.notification_provider = self.api.notification.register_provider(
            provider_id = self.provider_id,
            name = src.name,
            icon = src.icon,
            use_system_notify = False
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
                "display_in_class": False,
            }
        )
        self.api.ui.register_settings_page(
            qml_path = src.qml_path / "settings.qml",
            title = "Ciallo Widget Settings",
            icon = "ic_fluent_animal_cat_20_regular"
        )
        print(f"Ciallo Widget loaded")

    def on_unload(self):
        self.api.ui.unregister_settings_page(
            qml_path = src.qml_path / "settings.qml"
        )
        print(f"Ciallo Widget unloaded")
