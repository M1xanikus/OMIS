from typing import List

from model_interfaces import MarketingCompanyInterface, CustomerInterface, MailingInterface


class RegularMarketingCompany(MarketingCompanyInterface):
    def __init__(self):
        self.__name:str
        self.__customers:List[CustomerInterface] = []
        self.__mailings:List[MailingInterface] = []
        self.__aim:str

    def get_name(self) -> str:
        pass

    def set_name(self, name:str):
        pass

    def get_customers(self) -> List[CustomerInterface]:
        pass

    def add_customer(self, customer:CustomerInterface):
        pass

    def remove_customer(self, customer:CustomerInterface):
        pass

    def view_marketing_company(self):
        pass

    def create_mailing(self):
        pass

    def make_mailing(self, mailing:MailingInterface):
        pass

    def get_aim(self) -> str:
        pass

    def set_aim(self, aim:str):
        pass


