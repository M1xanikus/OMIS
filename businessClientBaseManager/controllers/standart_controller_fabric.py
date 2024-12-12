from abc import ABC
from typing import List

from .controller import ControllerInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class StandartControllerFabric(ABC):
    def init_controllers(self,app:App, system_composition:SystemCompositionInterface)-> List[ControllerInterface]:
        pass
