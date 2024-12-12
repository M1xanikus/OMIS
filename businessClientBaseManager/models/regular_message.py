from model_interfaces import MessageInterface

class RegularMessage(MessageInterface):
    def __init__(self):
        self.__sender: str
        self.__password: str
        self.__data_and_time_sending: str
        self.__content: str

    def get_sender(self) -> str:
        pass

    def get_data_and_time_sending(self) -> str:
        pass

    def get_content(self) -> str:
        pass

    def set_sender(self, sender: str):
        pass

    def set_data_and_time_sending(self, data_and_time_sending: str):
        pass

    def set_content(self, content: str):
        pass

    def default_admin(self,full_name:str , password:str ):
        pass

