from businessClientBaseManager.models.model_interfaces import MailingInterface, MarketingCompanyInterface
from managers_interfaces import SendingMailingManagementInterface

class StandardSendingMailingManager(SendingMailingManagementInterface):
    def __init__(self):
        self.__mailing: MailingInterface
        self.__marketing_company: MarketingCompanyInterface

    def send_mailing(self,mailing: MailingInterface):
        pass

    def save_sending_mailing(self, marketing_company: MarketingCompanyInterface):
        pass
