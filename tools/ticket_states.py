"""
TANSS API Tools - ticket states
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TicketStatesTools(BaseTool):
    """Tools for ticket states operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize ticket states tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_admin_ticketstates(self) -> Dict[str, Any]:
        """
        Gets a list of all ticket states
        
        Path: /api/v1/admin/ticketStates
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/admin/ticketStates"
        return self._request("get", url)

    def post_admin_ticketstates(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a ticket state
        
        Path: /api/v1/admin/ticketStates
        Method: post

        Parameters:
        body: ticket state object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/admin/ticketStates"
        return self._request("post", url, json=body)

    def put_admin_ticketstates(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a ticket state
        
        Path: /api/v1/admin/ticketStates/{id}
        Method: put

        Parameters:
        id: id of the ticket state that shall be updated
        body: ticket state object to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/admin/ticketStates/{id}"
        return self._request("put", url, json=body)

    def delete_admin_ticketstates(self, id: int) -> Dict[str, Any]:
        """
        Deletes a ticket state
        
        Path: /api/v1/admin/ticketStates/{id}
        Method: delete

        Parameters:
        id: id of the ticket state that shall be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/admin/ticketStates/{id}"
        return self._request("delete", url)
