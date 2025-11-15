"""
TANSS API Tools - ips
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class IpsTools(BaseTool):
    """Tools for ips operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize ips tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_ips(self, assignmenttype: str, assignmentid: int) -> Dict[str, Any]:
        """
        Gets ip addresses
        
        Path: /api/v1/ips/{assignmenttype}/{assignmentid}
        Method: get

        Parameters:
        assignmenttype: assignment type (PC / PERIPHERY)
        assignmentid: id of the pc / periphery
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ips/{assignmenttype}/{assignmentid}"
        return self._request("get", url)

    def post_v1_ips(self, assignmenttype: str, assignmentid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates an ip address
        
        Path: /api/v1/ips/{assignmenttype}/{assignmentid}
        Method: post

        Parameters:
        assignmenttype: assignment type (PC / PERIPHERY)
        assignmentid: id of the pc / periphery
        body: ip address object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ips/{assignmenttype}/{assignmentid}"
        return self._request("post", url, json=body)

    def put_v1_ips(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update ip address
        
        Path: /api/v1/ips/{id}
        Method: put

        Parameters:
        id: id of ip address
        body: ip address object to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ips/{id}"
        return self._request("put", url, json=body)

    def delete_v1_ips(self, id: int) -> Dict[str, Any]:
        """
        Deletes an ip address
        
        Path: /api/v1/ips/{id}
        Method: delete

        Parameters:
        id: id of ip address
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/ips/{id}"
        return self._request("delete", url)
