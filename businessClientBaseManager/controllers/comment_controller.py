from controller import ControllerInterface
from ..managers.managers_interfaces import AddingCommentManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class CommentController(ControllerInterface):
    def __init__(self):
        self.__manager: AddingCommentManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass