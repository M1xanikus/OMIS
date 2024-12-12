from ..models.model_interfaces import CustomerInterface, SystemCompositionInterface
from managers_interfaces import CustomerProfileManagementInterface

class StandardCustomerProfileManagementManager(CustomerProfileManagementInterface):
    def __init__(self):
        self.__customer:CustomerInterface
    def create_customer_profile(self):
        pass

    def edit_customer_profile(self, customer_profile:CustomerInterface):
        pass

    def erase_customer_profile(self,customer_profile:CustomerInterface):
        pass

    def save_customer_profile(self, composition: SystemCompositionInterface):
        pass

