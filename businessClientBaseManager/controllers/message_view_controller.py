from controller import ControllerInterface
from ..managers.managers_interfaces import ViewingMessagesManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class MessageViewController(ControllerInterface):
    def __init__(self):
        self.__manager: ViewingMessagesManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass
