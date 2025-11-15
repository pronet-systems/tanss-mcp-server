"""
TANSS API Tools - operating systems
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class OperatingSystemsTools(BaseTool):
    """Tools for operating systems operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize operating systems tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_os(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new os
        
        Path: /api/v1/os
        Method: post

        Parameters:
        body: operating system to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/os"
        return self._request("post", url, json=body)

    def get_v1_os(self) -> Dict[str, Any]:
        """
        Get a list of all os
        
        Path: /api/v1/os
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/os"
        return self._request("get", url)

    def put_v1_os(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a os
        
        Path: /api/v1/os/{id}
        Method: put

        Parameters:
        id: Id of the operating system
        body: operating system to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/os/{id}"
        return self._request("put", url, json=body)

    def get_v1_os(self, id: int) -> Dict[str, Any]:
        """
        Get a specific os
        
        Path: /api/v1/os/{id}
        Method: get

        Parameters:
        id: Id of the operating system
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/os/{id}"
        return self._request("get", url)

    def delete_v1_os(self, id: int) -> Dict[str, Any]:
        """
        Deletes a specific os
        
        Path: /api/v1/os/{id}
        Method: delete

        Parameters:
        id: Id of the operating system
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/os/{id}"
        return self._request("delete", url)
