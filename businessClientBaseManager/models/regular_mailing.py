from typing import List

from model_interfaces import MessageInterface, MailingInterface, CustomerInterface


class RegularMailing(MailingInterface):
    def __init__(self):
        self.__message:MessageInterface
        self.__name:str
        self.customers:List[CustomerInterface]

    def add_customer(self, customer:CustomerInterface):
        pass

    def remove_customer(self, customer:CustomerInterface):
        pass

    def get_customers(self)->List[CustomerInterface]:
        pass

    def set_name(self, name:str):
        pass

    def get_name(self)->str:
        pass

    def set_message(self, message:MessageInterface):
        pass

    def get_message(self)->MessageInterface:
        pass
