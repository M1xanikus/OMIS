from model_interfaces import TaskInterface,CommentInterface, List

class RegularTask(TaskInterface):
    def __init__(self):
        self.__name:str
        self.__description:str
        self.__priority:str
        self.__status:str
        self.__commentaries: List[CommentInterface]
        self.__term:str
    def set_name(self,name:str):
        pass

    def set_description(self,description:str):
        pass

    def set_priority(self,priority:str):
        pass

    def set_status(self,status:str):
        pass

    def add_commentary(self,commentary:CommentInterface):
        pass

    def add_term(self,term:str):
        pass

    def del_commentary(self,commentary:CommentInterface):
        pass

    def get_name(self)->str:
        pass

    def get_description(self)->str:
        pass

    def get_priority(self)->str:
        pass

    def get_status(self)->str:
        pass

    def get_commentaries(self)->List[CommentInterface]:
        pass

    def get_term(self)->str:
        pass

    def view_task(self):
        pass
