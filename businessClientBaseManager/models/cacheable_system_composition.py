from typing import List


from model_interfaces import SystemCompositionInterface,TaskInterface , CustomerInterface, MarketingCompanyInterface

class CacheableSystemComposition(SystemCompositionInterface):
    def __init__(self):
        self.__composition:SystemCompositionInterface
    def cacheable_system_composition(self,composition:SystemCompositionInterface):
        pass
    def get_customer_list(self) -> List[CustomerInterface]:
        pass
    def get_marketing_company_list(self) -> List[MarketingCompanyInterface]:
        pass
    def get_task_list(self) -> List[TaskInterface]:
        pass

    def cashe_composition(self):
        pass
