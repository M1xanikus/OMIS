from ..models.model_interfaces import MarketingCompanyInterface, SystemCompositionInterface
from managers_interfaces import MarketingCompanyManagementInterface

class StandardMarketingCompanyManagementManager(MarketingCompanyManagementInterface):
    def __init__(self):
        self.__company:MarketingCompanyInterface

    def create_marketing_company(self):
        pass

    def edit_marketing_company(self, marketing_company:MarketingCompanyInterface):
        pass

    def delete_marketing_company(self, marketing_company:MarketingCompanyInterface):
        pass

    def save_marketing_company(self, system_composition: SystemCompositionInterface ):
        pass

    
