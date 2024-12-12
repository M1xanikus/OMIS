from typing import List

from model_interfaces import SystemCompositionInterface, CustomerInterface, MarketingCompanyInterface, TaskInterface

class BasicSystemComposition(SystemCompositionInterface):
    def __init__(self):
        self.__customers: List[CustomerInterface]
        self.__marketing_companies: List[MarketingCompanyInterface]
        self.__tasks: List[TaskInterface]

    def basic_system_composition(self, system_composition: SystemCompositionInterface):
        pass

    def get_customer_list(self) -> List[CustomerInterface]:
        pass
    def get_marketing_companies(self) -> List[MarketingCompanyInterface]:
        pass
    def get_task_list(self) -> List[TaskInterface]:
        pass

    def cache_composition(self):
        pass