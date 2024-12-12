from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App
from controller import ControllerInterface

class TaskDisplayController(ControllerInterface):
    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass
