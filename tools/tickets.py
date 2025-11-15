"""
TANSS API Tools - tickets
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TicketsTools(BaseTool):
    """Tools for tickets operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize tickets tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_tickets(self, body: Dict[str, Any], remittercheck: Optional[Any] = None) -> Dict[str, Any]:
        """
        Creates a ticket in the database
        
        Path: /api/v1/tickets
        Method: post

        Parameters:
        remittercheck: can be given to omit the check that a remitter is required when storing tickets
        body: ticket object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets"
        return self._request("post", url, json=body)

    def get_v1_tickets(self, ticketid: int) -> Dict[str, Any]:
        """
        Gets a ticket by id

        Path: /api/v1/tickets/{ticketid}
        Method: get

        Parameters:
        ticketid:

        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}"
        return self._request("get", url)

    def delete_v1_tickets(self, ticketid: int, targetticketid: Optional[int] = None) -> Dict[str, Any]:
        """
        Deletes a ticket by id
        
        Path: /api/v1/tickets/{ticketid}
        Method: delete

        Parameters:
        ticketid: 
        targetticketid: if given, will also move entities such as chats or callbacks to a target ticket
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}"
        params = {}
        if targetticketid is not None:
            params["targetTicketId"] = targetticketid
        return self._request("delete", url, params=params)

    def put_v1_tickets(self, ticketid: int, body: Dict[str, Any], remittercheck: Optional[Any] = None) -> Dict[str, Any]:
        """
        Updates a ticket
        
        Path: /api/v1/tickets/{ticketid}
        Method: put

        Parameters:
        ticketid: 
        remittercheck: can be given to omit the check that a remitter is required when storing tickets
        body: updated ticket object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}"
        return self._request("put", url, json=body)

    def get_tickets_history(self, ticketid: int) -> Dict[str, Any]:
        """
        Gets a ticket history
        
        Path: /api/v1/tickets/history/{ticketid}
        Method: get

        Parameters:
        ticketid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/history/{ticketid}"
        return self._request("get", url)

    def post_tickets_comments(self, ticketid: int, body: Dict[str, Any], pinned: Optional[bool] = None) -> Dict[str, Any]:
        """
        Creates a comment
        
        Path: /api/v1/tickets/{ticketid}/comments
        Method: post

        Parameters:
        ticketid: 
        pinned: comment can optionally be "pinned" to the ticket
        body: comment to be created
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}/comments"
        params = {}
        if pinned is not None:
            params["pinned"] = pinned
        return self._request("post", url, params=params, json=body)
