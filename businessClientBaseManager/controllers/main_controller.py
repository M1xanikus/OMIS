from typing import List

from ..controllers.controller import ControllerInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class MainController:# чел в синглтоны полез
    def __init__(self):
        self.__app: App
        self.__controllers: List[ControllerInterface]
        self.__composition: SystemCompositionInterface
        self.__controller: MainController

    def main_controller(self,app:App, controllers:List[ControllerInterface], system_composition:SystemCompositionInterface, controller: MainController):
        pass

    def start_app(self, app: App, controllers: List[ControllerInterface],
                        system_composition: SystemCompositionInterface, controller: MainController):
        pass


    def control_app(self, app: App, controllers: List[ControllerInterface], system_composition: SystemCompositionInterface, controller: MainController):
        pass