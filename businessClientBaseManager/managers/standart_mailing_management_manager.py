from businessClientBaseManager.models.model_interfaces import MailingInterface, MarketingCompanyInterface, TaskInterface
from managers_interfaces import MailingManagementInterface

class StandardMailingManagementManager(MailingManagementInterface):
    def __init__(self):
        self.__mailing:MailingInterface
        self.__marketing_company:MarketingCompanyInterface

    def create_mailing(self):
        pass

    def edit_task(self, task:TaskInterface):
        pass

    def save_mailing(self, marketing_company:MarketingCompanyInterface):
        pass