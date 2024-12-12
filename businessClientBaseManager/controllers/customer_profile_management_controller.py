from controller import ControllerInterface
from ..managers.managers_interfaces import CustomerProfileManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class CustomerProfileManagementController(ControllerInterface):
    def __init__(self):
        self.__manager: CustomerProfileManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass