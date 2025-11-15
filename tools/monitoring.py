"""
TANSS API Tools - monitoring
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class MonitoringTools(BaseTool):
    """Tools for monitoring operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize monitoring tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_ticket(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a ticket, using the monitoring api
        
        Path: /api/monitoring/v1/ticket
        Method: post

        Parameters:
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/ticket"
        return self._request("post", url, json=body)

    def post_v1_assigngroup(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assigns a groupName to a company or device
        
        Path: /api/monitoring/v1/assignGroup
        Method: post

        Parameters:
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/assignGroup"
        return self._request("post", url, json=body)

    def delete_v1_assigngroup(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delete a group assignment
        
        Path: /api/monitoring/v1/assignGroup
        Method: delete

        Parameters:
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/assignGroup"
        return self._request("delete", url, json=body)

    def get_v1_assigngroup(self) -> Dict[str, Any]:
        """
        Gets all group assignments
        
        Path: /api/monitoring/v1/assignGroup
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/assignGroup"
        return self._request("get", url)

    def get_v1_ticketsfromgroup(self, groupname: str, closedtickets: Optional[bool] = None) -> Dict[str, Any]:
        """
        Gets ticket(s), based on a given group
        
        Path: /api/monitoring/v1/ticketsFromGroup
        Method: get

        Parameters:
        groupname: Name of the group, which the ticket shall be retrieved for
        closedtickets: The default behaviour ist that only "open" tickets will be returned. Set this to "true" if you want to retrieve closed tickets as well
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/ticketsFromGroup"
        params = {}
        if groupname is not None:
            params["groupName"] = groupname
        if closedtickets is not None:
            params["closedTickets"] = closedtickets
        return self._request("get", url, params=params)

    def get_v1_ticket(self, ticketid: int) -> Dict[str, Any]:
        """
        Gets a ticket (created by the monitoring api) by id
        
        Path: /api/monitoring/v1/ticket/{ticketid}
        Method: get

        Parameters:
        ticketid: Id of the ticket that should be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/ticket/{ticketid}"
        return self._request("get", url)

    def put_v1_ticket(self, ticketid: int) -> Dict[str, Any]:
        """
        Updates a ticket (created by the monitoring api) by id
        
        Path: /api/monitoring/v1/ticket/{ticketid}
        Method: put

        Parameters:
        ticketid: Id of the ticket that should be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/monitoring/v1/ticket/{ticketid}"
        return self._request("put", url)
