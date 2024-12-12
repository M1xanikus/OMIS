from controller import ControllerInterface
from ..managers.managers_interfaces import SendingMailingManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class MailingDistrubuteController(ControllerInterface):
    def __init__(self):
        self.__manager: SendingMailingManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass