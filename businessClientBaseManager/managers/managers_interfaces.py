from abc import ABC, abstractmethod
from ..models.model_interfaces import MarketingCompanyInterface, SystemCompositionInterface, TaskInterface, \
    MailingInterface, CustomerInterface, CommentInterface


class CustomerProfileManagementInterface(ABC):
    @abstractmethod
    def create_customer_profile(self):
            pass
    @abstractmethod
    def erase_customer_profile(self, customer: CustomerInterface ):
        pass
    @abstractmethod
    def edit_customer_profile(self, customer_profile):
        pass
    @abstractmethod
    def save_customer_profile(self, ):
        pass

class MarketingCompanyManagementInterface(ABC):
    @abstractmethod
    def create_marketing_company(self):
        pass

    @abstractmethod
    def edit_marketing_company(self, marketing_company: MarketingCompanyInterface):
        pass

    @abstractmethod
    def save_marketing_company(self, composition: SystemCompositionInterface):
        pass

    @abstractmethod
    def delete_marketing_company(self, marketing_company: MarketingCompanyInterface):
        pass

class TaskManagementInterface(ABC):
    @abstractmethod
    def create_task(self):
        pass

    @abstractmethod
    def edit_task(self, task: TaskInterface):
        pass

    @abstractmethod
    def save_task(self, composition: SystemCompositionInterface):
        pass

    @abstractmethod
    def delete_task(self, task: TaskInterface):
        pass

class MailingManagementInterface(ABC):
    @abstractmethod
    def create_mailing(self):
        pass

    @abstractmethod
    def save_mailing(self, company: MarketingCompanyInterface):
        pass

    @abstractmethod
    def view_mailing(self,mailing: MailingInterface):
        pass

    @abstractmethod
    def edit_task(self, task: TaskInterface):
        pass

class SendingMailingManagementInterface(ABC):
    @abstractmethod
    def send_mailing(self,mailing: MailingInterface):
        pass

    @abstractmethod
    def save_sending_mailing(self, marketing_company: MarketingCompanyInterface):
        pass


class ViewingMessagesManagementInterface(ABC):
    @abstractmethod
    def view_messages(self, customer: CustomerInterface):
        pass

    @abstractmethod
    def view_mailing(self, mailing: MailingInterface):
        pass

    @abstractmethod
    def edit_task(self, task: TaskInterface):
        pass

    @abstractmethod
    def save_mailing(self, company: MarketingCompanyInterface):
        pass

class AddingCommentManagementInterface(ABC):
    @abstractmethod
    def create_comment(self):
        pass

    @abstractmethod
    def save_comment(self, task: TaskInterface):
        pass
