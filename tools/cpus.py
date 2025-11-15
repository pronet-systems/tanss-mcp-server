"""
TANSS API Tools - cpus
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class CpusTools(BaseTool):
    """Tools for cpus operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize cpus tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_cpus(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new cpu
        
        Path: /api/v1/cpus
        Method: post

        Parameters:
        body: cpu to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/cpus"
        return self._request("post", url, json=body)

    def get_v1_cpus(self) -> Dict[str, Any]:
        """
        Get a list of all cpus
        
        Path: /api/v1/cpus
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/cpus"
        return self._request("get", url)

    def put_v1_cpus(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a cpu
        
        Path: /api/v1/cpus/{id}
        Method: put

        Parameters:
        id: Id of the cpu
        body: cpu to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/cpus/{id}"
        return self._request("put", url, json=body)

    def get_v1_cpus(self, id: int) -> Dict[str, Any]:
        """
        Get a cpu
        
        Path: /api/v1/cpus/{id}
        Method: get

        Parameters:
        id: Id of the cpu
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/cpus/{id}"
        return self._request("get", url)

    def delete_v1_cpus(self, id: int) -> Dict[str, Any]:
        """
        Deletes a cpu
        
        Path: /api/v1/cpus/{id}
        Method: delete

        Parameters:
        id: Id of the cpu
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/cpus/{id}"
        return self._request("delete", url)
