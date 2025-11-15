"""
TANSS API Tools - ticket board
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TicketBoardTools(BaseTool):
    """Tools for ticket board operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize ticket board tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_ticketboard(self) -> Dict[str, Any]:
        """
        Gets the ticket board with all panels
        
        Path: /api/v1/ticketBoard
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard"
        return self._request("get", url)

    def get_ticketboard_panel(self, mode: Optional[str] = None) -> Dict[str, Any]:
        """
        Gets an empty ticket board panel
        
        Path: /api/v1/ticketBoard/panel
        Method: get

        Parameters:
        mode: If mode = "edit" you get all possible employees, departments, tags, ticket types and tickets status which can be assigned
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/panel"
        params = {}
        if mode is not None:
            params["mode"] = mode
        return self._request("get", url, params=params)

    def post_ticketboard_panel(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new ticket board panel
        
        Path: /api/v1/ticketBoard/panel
        Method: post

        Parameters:
        body: Ticket board panel
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/panel"
        return self._request("post", url, json=body)

    def put_ticketboard_panel(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a ticket board panel
        
        Path: /api/v1/ticketBoard/panel
        Method: put

        Parameters:
        body: Ticket board panel
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/panel"
        return self._request("put", url, json=body)

    def get_ticketboard_panel(self, id: int) -> Dict[str, Any]:
        """
        Gets a ticket board panel
        
        Path: /api/v1/ticketBoard/panel/{id}
        Method: get

        Parameters:
        id: Panel id
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/panel/{id}"
        return self._request("get", url)

    def delete_ticketboard_panel(self, id: int) -> Dict[str, Any]:
        """
        Deletes a ticket board panel
        
        Path: /api/v1/ticketBoard/panel/{id}
        Method: delete

        Parameters:
        id: Panel id
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/panel/{id}"
        return self._request("delete", url)

    def get_panel_registers(self, id: int) -> Dict[str, Any]:
        """
        Gets all registers from a ticket board panel
        
        Path: /api/v1/ticketBoard/panel/{id}/registers
        Method: get

        Parameters:
        id: Panel id
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/panel/{id}/registers"
        return self._request("get", url)

    def get_ticketboard_project(self, id: int) -> Dict[str, Any]:
        """
        Gets a ticket board from a project
        
        Path: /api/v1/ticketBoard/project/{id}
        Method: get

        Parameters:
        id: Project id
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/project/{id}"
        return self._request("get", url)

    def get_project_registers(self, id: int) -> Dict[str, Any]:
        """
        Gets all registers from a ticket board project
        
        Path: /api/v1/ticketBoard/project/{id}/registers
        Method: get

        Parameters:
        id: Project id
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/project/{id}/registers"
        return self._request("get", url)

    def get_project_globalpanels(self) -> Dict[str, Any]:
        """
        Get global ticket panels
        
        Path: /api/v1/ticketBoard/project/globalPanels
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ticketBoard/project/globalPanels"
        return self._request("get", url)
