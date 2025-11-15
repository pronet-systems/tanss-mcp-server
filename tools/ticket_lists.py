"""
TANSS API Tools - ticket lists
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TicketListsTools(BaseTool):
    """Tools for ticket lists operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize ticket lists tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_tickets_own(self) -> Dict[str, Any]:
        """
        gets a list of own tickets (assigned to currently logged in employee)
        
        Path: /api/v1/tickets/own
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/own"
        return self._request("get", url)

    def get_tickets_general(self) -> Dict[str, Any]:
        """
        gets a list of general tickets (assigned to no employee)
        
        Path: /api/v1/tickets/general
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/general"
        return self._request("get", url)

    def get_tickets_company(self, companyid: int) -> Dict[str, Any]:
        """
        gets a list of company tickets
        
        Path: /api/v1/tickets/company/{companyid}
        Method: get

        Parameters:
        companyid: id of the company for the tickets
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/company/{companyid}"
        return self._request("get", url)

    def get_tickets_technician(self) -> Dict[str, Any]:
        """
        gets a list of tickets of all technicians
        
        Path: /api/v1/tickets/technician
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/technician"
        return self._request("get", url)

    def get_tickets_repair(self) -> Dict[str, Any]:
        """
        gets a list of repair tickets
        
        Path: /api/v1/tickets/repair
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/repair"
        return self._request("get", url)

    def get_tickets_notidentified(self) -> Dict[str, Any]:
        """
        gets a list of not identified tickets
        
        Path: /api/v1/tickets/notIdentified
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/notIdentified"
        return self._request("get", url)

    def get_tickets_projects(self) -> Dict[str, Any]:
        """
        gets a list of all projects
        
        Path: /api/v1/tickets/projects
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/projects"
        return self._request("get", url)

    def get_tickets_localadminoverview(self) -> Dict[str, Any]:
        """
        gets a list of all tickets which are assigned to local ticket admins
        
        Path: /api/v1/tickets/localAdminOverview
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/localAdminOverview"
        return self._request("get", url)

    def get_tickets_withrole(self) -> Dict[str, Any]:
        """
        gets a list of all ticket which a technician has a role in
        
        Path: /api/v1/tickets/withRole
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/withRole"
        return self._request("get", url)

    def put_v1_tickets(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a (custom) ticket list
        
        Path: /api/v1/tickets
        Method: put

        Parameters:
        body: query parameters for retrieving ticket
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets"
        return self._request("put", url, json=body)
