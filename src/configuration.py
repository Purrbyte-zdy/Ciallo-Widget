from ClassWidgets.SDK import ConfigBaseModel
from loguru import logger

plugin_logger = logger.bind(plugin="Ciallo Widget")

class Config(ConfigBaseModel):
    display_in_class: bool = False
    target_text: str = "Ciallo～(∠・ω< )⌒★"

    def _on_change(self):
        updated_config = self.model_dump()
        plugin_logger.debug(updated_config)
        # global config
        # config = updated_config

    @staticmethod
    def make_me_happy() -> None:
        return None
