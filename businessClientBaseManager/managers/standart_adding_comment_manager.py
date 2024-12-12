from ..models.model_interfaces import CommentInterface, TaskInterface, MarketingCompanyInterface
from managers_interfaces import AddingCommentManagementInterface

class StandardAddCommentManager(AddingCommentManagementInterface):
    def __init__(self):
        self.__comment:CommentInterface
        self.__task:TaskInterface

    def create_comment(self):
        pass

    def save_comment(self,task:TaskInterface):
        pass

    def save_mailing(self,marketing_company:MarketingCompanyInterface):
        pass
