"""
TANSS API Tools - services
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ServicesTools(BaseTool):
    """Tools for services operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize services tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_services(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a service
        
        Path: /api/v1/services
        Method: post

        Parameters:
        body: service object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/services"
        return self._request("post", url, json=body)

    def get_v1_services(self) -> Dict[str, Any]:
        """
        Gets a list of all services
        
        Path: /api/v1/services
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/services"
        return self._request("get", url)

    def get_v1_services(self, id: int) -> Dict[str, Any]:
        """
        Gets a service by id
        
        Path: /api/v1/services/{id}
        Method: get

        Parameters:
        id: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/services/{id}"
        return self._request("get", url)

    def put_v1_services(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a service
        
        Path: /api/v1/services/{id}
        Method: put

        Parameters:
        id: 
        body: service object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/services/{id}"
        return self._request("put", url, json=body)

    def delete_v1_services(self, id: int) -> Dict[str, Any]:
        """
        Deletes a service
        
        Path: /api/v1/services/{id}
        Method: delete

        Parameters:
        id: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/services/{id}"
        return self._request("delete", url)
