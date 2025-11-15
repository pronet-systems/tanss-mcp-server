"""
TANSS API Tools - hddTypes
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class HddtypesTools(BaseTool):
    """Tools for hddTypes operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize hddTypes tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_hddtypes(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new hdd type
        
        Path: /api/v1/hddTypes
        Method: post

        Parameters:
        body: hdd type to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/hddTypes"
        return self._request("post", url, json=body)

    def get_v1_hddtypes(self) -> Dict[str, Any]:
        """
        Get a list of all hdd types
        
        Path: /api/v1/hddTypes
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/hddTypes"
        return self._request("get", url)

    def put_v1_hddtypes(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a hdd type
        
        Path: /api/v1/hddTypes/{id}
        Method: put

        Parameters:
        id: Id of the hdd type
        body: hdd type to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/hddTypes/{id}"
        return self._request("put", url, json=body)

    def get_v1_hddtypes(self, id: int) -> Dict[str, Any]:
        """
        Get a hdd type
        
        Path: /api/v1/hddTypes/{id}
        Method: get

        Parameters:
        id: Id of the hdd type
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/hddTypes/{id}"
        return self._request("get", url)

    def delete_v1_hddtypes(self, id: int) -> Dict[str, Any]:
        """
        Deletes a hdd type
        
        Path: /api/v1/hddTypes/{id}
        Method: delete

        Parameters:
        id: Id of the hdd type
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/hddTypes/{id}"
        return self._request("delete", url)
