"""
TANSS API Tools - supports
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class SupportsTools(BaseTool):
    """Tools for supports operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize supports tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def put_supports_list(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a support list
        
        Path: /api/v1/supports/list
        Method: put

        Parameters:
        body: query parameters for retrieving supports
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/supports/list"
        return self._request("put", url, json=body)

    def post_v1_supports(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a support/appointment
        
        Path: /api/v1/supports
        Method: post

        Parameters:
        body: support object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/supports"
        return self._request("post", url, json=body)

    def get_v1_supports(self, supportid: int) -> Dict[str, Any]:
        """
        Gets a support/appointment
        
        Path: /api/v1/supports/{supportid}
        Method: get

        Parameters:
        supportid: id of the support that shall be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/supports/{supportid}"
        return self._request("get", url)

    def put_v1_supports(self, supportid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Edits a support/appointment
        
        Path: /api/v1/supports/{supportid}
        Method: put

        Parameters:
        supportid: id of the support that shall be updated
        body: support object to be saved. The best way is only to give the fields that have changed.
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/supports/{supportid}"
        return self._request("put", url, json=body)

    def post_supports_signature(self, supportid: int, supportids: Optional[str] = None, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Uploads a signature for supports
        
        Path: /api/v1/supports/signature/{supportid}
        Method: post

        Parameters:
        supportid: id of the support that the signature shall be uploaded
        supportids: if the signature is used for multiple supports, give them here (separated by commas)
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/supports/signature/{supportid}"
        params = {}
        if supportids is not None:
            params["supportIds"] = supportids
        return self._request("post", url, params=params, json=body)
