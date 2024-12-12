from controller import ControllerInterface
from ..managers.managers_interfaces import TaskManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class TaskController(ControllerInterface):
    def __init__(self):
        self.__manager: TaskManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass
