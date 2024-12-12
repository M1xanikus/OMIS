from typing import List

from model_interfaces import MessageInterface, CustomerInterface

class RegularCustomer(CustomerInterface):
    def __init__(self):
        self.__sex:str
        self.__age:int
        self.__region:str
        self.__phone_number:str
        self.__email:str
        self.__messages:List[MessageInterface]
        self.__full_name:str

    def get_sex(self)->str:
        pass

    def get_age(self)->int:
        pass

    def get_phone_number(self)->str:
        pass

    def get_email(self)->str:
        pass

    def get_full_name(self)->str:
        pass

    def get_messages(self)->List[MessageInterface]:
        pass

    def get_region(self)->str:
        pass

    def set_age(self, age:int):
        pass

    def set_phone_number(self, phone_number:str):
        pass

    def set_email(self, email:str):
        pass

    def set_full_name(self, full_name:str):
        pass

    def view_profile(self):
        pass

    def view_messages(self):
        pass

    def send_message(self, message:MessageInterface):
        pass

    def set_region(self, region:str):
        pass

