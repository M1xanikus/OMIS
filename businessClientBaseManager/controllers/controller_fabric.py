from abc import ABC, abstractmethod
from typing import List

from ..view.app_file import App
from controller import ControllerInterface
from ..models.model_interfaces import  SystemCompositionInterface


class ControllerFabric(ABC):
    @abstractmethod
    def initialize(self, app:App, system:SystemCompositionInterface )-> List[ControllerInterface]:
        pass