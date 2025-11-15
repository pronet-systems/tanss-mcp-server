"""
TANSS API Tools - pc
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class PcTools(BaseTool):
    """Tools for pc operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize pc tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_pcs(self, pcid: int) -> Dict[str, Any]:
        """
        Gets a pc by id
        
        Path: /api/v1/pcs/{pcid}
        Method: get

        Parameters:
        pcid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/pcs/{pcid}"
        return self._request("get", url)

    def put_v1_pcs(self, pcid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a pc
        
        Path: /api/v1/pcs/{pcid}
        Method: put

        Parameters:
        pcid: 
        body: pc object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/pcs/{pcid}"
        return self._request("put", url, json=body)

    def delete_v1_pcs(self, pcid: int) -> Dict[str, Any]:
        """
        Deletes a pc
        
        Path: /api/v1/pcs/{pcid}
        Method: delete

        Parameters:
        pcid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/pcs/{pcid}"
        return self._request("delete", url)

    def post_v1_pcs(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a pc
        
        Path: /api/v1/pcs
        Method: post

        Parameters:
        body: pc object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/pcs"
        return self._request("post", url, json=body)

    def put_v1_pcs(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gets a list of pcs
        
        Path: /api/v1/pcs
        Method: put

        Parameters:
        body: query parameters for the request
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/pcs"
        return self._request("put", url, json=body)
