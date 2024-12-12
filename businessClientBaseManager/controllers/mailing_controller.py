from controller import ControllerInterface
from ..managers.managers_interfaces import MailingManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class MailingController(ControllerInterface):
    def __init__(self):
        self.__manager: MailingManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass
