"""
Ciallo Widget
Pop up Ciallo every morning.
"""

from ClassWidgets.SDK import CW2Plugin, PluginAPI, ConfigBaseModel
from loguru import logger

plugin_logger = logger.bind(plugin="Ciallo Widget")

class Plugin(CW2Plugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        import plugin_src
        plugin_logger.debug(f"[PLUGIN] src.__file__ = {plugin_src.__file__}")
        plugin_logger.debug(f"[PLUGIN] dir(src) = {dir(plugin_src)}")
        self.src = plugin_src
        self.notification_provider = None
        self.provider_id = str(self.pid)
        self.current_statue = self.api.runtime.current_status
        self.pid_str = str(self.pid)
        self.config: ConfigBaseModel = self.src.Config()


    def on_load(self):
        super().on_load()
        self.notification_provider = self.api.notification.register_provider(
            provider_id = self.provider_id,
            name = self.src.name,
            icon = self.src.icon,
            use_system_notify = False
        )
        self.api.widgets.register(
            widget_id = self.src.widget_id,
            name = self.src.name,
            qml_path = self.src.qml_path / "widget.qml",
            settings_qml = self.src.qml_path / "settings.qml",
            backend_obj = self,
            default_settings = {
                "target_title": "Welcome",
                "target_text": "Ciallo～(∠・ω< )⌒★",
                "display_in_class": False,
            }
        )
        self.api.ui.register_settings_page(
            qml_path = self.src.qml_path / "settings.qml",
            title = "Ciallo Widget Settings",
            icon = "ic_fluent_animal_cat_20_regular"
        )
        self.api.config.register_plugin_model(self.pid_str, self.config)
        plugin_logger.info(f"Ciallo Widget loaded")

    def on_unload(self):
        self.api.ui.unregister_settings_page(
            qml_path = self.src.qml_path / "settings.qml"
        )
        plugin_logger.info(f"Ciallo Widget unloaded")
