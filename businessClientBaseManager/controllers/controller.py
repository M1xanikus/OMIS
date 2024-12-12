from abc import ABC
from ..view.app_file import App
from ..models.model_interfaces import SystemCompositionInterface

class ControllerInterface(ABC):
    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass