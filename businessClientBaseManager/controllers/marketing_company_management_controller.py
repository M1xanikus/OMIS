from controller import ControllerInterface
from ..managers.standart_marketing_company_management_manager import MarketingCompanyManagementInterface
from ..models.model_interfaces import SystemCompositionInterface
from ..view.app_file import App


class MarketingCompanyManagementController(ControllerInterface):
    def __init__(self):
        self.__manager: MarketingCompanyManagementInterface

    def control(self,app:App, system_composition:SystemCompositionInterface):
        pass