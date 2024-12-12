from ..models.model_interfaces import CustomerInterface, MarketingCompanyInterface, \
    TaskInterface
from managers_interfaces import ViewingMessagesManagementInterface

class StandardViewingMessagesManager(ViewingMessagesManagementInterface):
    def __init__(self):
        self.__customer:CustomerInterface
        self.__marketing_company:MarketingCompanyInterface


    def view_messages(self, customer: CustomerInterface):
        pass

    def edit_task(self, task: TaskInterface):
        pass