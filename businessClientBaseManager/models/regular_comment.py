from model_interfaces import CommentInterface, CustomerInterface, List


class RegularComment(CommentInterface):
    def __init__(self):
        self.__content:str
        self.__data_and_time:str
        self.__customers:List[CustomerInterface]

    def set_data_and_time(self, data_and_time:str):
        pass

    def get_data_and_time(self):
        pass

    def set_content(self, content:str):
        pass

    def view_content(self):
        pass

    def add_customer(self, customer:CustomerInterface):
        pass
