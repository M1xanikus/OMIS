from abc import ABC, abstractmethod
from interface_fabric import InterfaceFabric
class App(ABC):
    def __init__(self):
        self.__windows: dict
        self.__fabric: InterfaceFabric

    @abstractmethod
    def create_interface(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def draw_interface(self):
        pass