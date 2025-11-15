"""
TANSS API Tools - manufacturer
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ManufacturerTools(BaseTool):
    """Tools for manufacturer operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize manufacturer tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_manufacturers(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new manufacturer
        
        Path: /api/v1/manufacturers
        Method: post

        Parameters:
        body: manufacturer to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/manufacturers"
        return self._request("post", url, json=body)

    def get_v1_manufacturers(self) -> Dict[str, Any]:
        """
        Get a list of all manufacturers
        
        Path: /api/v1/manufacturers
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/manufacturers"
        return self._request("get", url)

    def put_v1_manufacturers(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a manufacturer
        
        Path: /api/v1/manufacturers/{id}
        Method: put

        Parameters:
        id: Id of the manufacturer
        body: manufacturer to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/manufacturers/{id}"
        return self._request("put", url, json=body)

    def get_v1_manufacturers(self, id: int) -> Dict[str, Any]:
        """
        Get a manufacturer
        
        Path: /api/v1/manufacturers/{id}
        Method: get

        Parameters:
        id: Id of the manufacturer
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/manufacturers/{id}"
        return self._request("get", url)

    def delete_v1_manufacturers(self, id: int) -> Dict[str, Any]:
        """
        Deletes a manufacturer
        
        Path: /api/v1/manufacturers/{id}
        Method: delete

        Parameters:
        id: Id of the manufacturer
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/manufacturers/{id}"
        return self._request("delete", url)
