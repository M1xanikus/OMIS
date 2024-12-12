from abc import ABC, abstractmethod
from ctypes.wintypes import tagSIZE
from typing import List


class CustomerInterface(ABC):
    @abstractmethod
    def view_profile(self):
        pass
    @abstractmethod
    def view_messages(self):
        pass
    @abstractmethod
    def send_message(self, message):
        pass

class MessageInterface(ABC):
    @abstractmethod
    def send_message(self, message):
        pass
    @abstractmethod
    def set_content(self, content:str):
        pass
    @abstractmethod
    def get_content(self)-> str:
        pass

class MailingInterface(ABC):
    @abstractmethod
    def send_message(self, message):
        pass
    @abstractmethod
    def set_content(self, content:str):
        pass
    @abstractmethod
    def get_content(self)-> str:
        pass

class CommentInterface(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

    def set_content(self, content:str):
        pass

    def get_content(self)-> str:
        pass

class MarketingCompanyInterface(ABC):
    @abstractmethod
    def make_mailing(self, mailing: MailingInterface):
        pass

    @abstractmethod
    def create_mailing(self):
        pass

    @abstractmethod
    def show_marketing_company(self):
        pass

class TaskInterface(ABC):
    @abstractmethod
    def view_task(self):
        pass

class SystemCompositionInterface(ABC):
    @abstractmethod
    def get_customer_list(self)-> List[CustomerInterface]:
        pass
    def get_marketing_company_list(self)-> List[MarketingCompanyInterface]:
        pass
    def get_task_list(self)-> List[TaskInterface]:
        pass

