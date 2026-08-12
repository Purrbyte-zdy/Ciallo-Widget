from ClassWidgets.SDK import NotificationLevel, NotificationProvider
from loguru import logger
from src.configuration import Config

plugin_logger = logger.bind(plugin="Ciallo Widget")


def is_time_to_notify(current_statue: str, display_in_class: bool) -> bool:
    if (
            not  (current_statue == "break"
            or    current_statue == "free")
            and display_in_class == False):
        return False
    return True

def push_notification(provider: NotificationProvider, current_statue: str) -> bool:
    if not is_time_to_notify(current_statue, Config.display_in_class):
        plugin_logger.info("Isn't time to notify.")
        return False
    provider.push(
        level = NotificationLevel.INFO,
        title = "Ciallo Widget",
        message = Config.target_text,
        duration = 1000,
        closable = True
    )
    plugin_logger.info("Notification pushed.")
    return True