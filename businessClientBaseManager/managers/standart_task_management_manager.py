from businessClientBaseManager.models.model_interfaces import TaskInterface, SystemCompositionInterface
from managers_interfaces import TaskManagementInterface

class StandartTaskManager(TaskManagementInterface):
    def __init__(self):
        self.__task:TaskInterface

    def create_task(self):
        pass

    def delete_task(self, task:TaskInterface):
        pass

    def edit_task(self, task:TaskInterface):
        pass

    def save_task(self, system_composition:SystemCompositionInterface):
        pass

