"""
TANSS API Tools - callback
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class CallbackTools(BaseTool):
    """Tools for callback operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize callback tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_callbacks(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a callback
        
        Path: /api/v1/callbacks
        Method: post

        Parameters:
        body: callback object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/callbacks"
        return self._request("post", url, json=body)

    def put_v1_callbacks(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a list of callbacks
        
        Path: /api/v1/callbacks
        Method: put

        Parameters:
        body: filter settings
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/callbacks"
        return self._request("put", url, json=body)

    def get_v1_callbacks(self, callbackid: int) -> Dict[str, Any]:
        """
        Gets a callback
        
        Path: /api/v1/callbacks/{callbackid}
        Method: get

        Parameters:
        callbackid: Id of the callback to be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/callbacks/{callbackid}"
        return self._request("get", url)

    def put_v1_callbacks(self, callbackid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a callback
        
        Path: /api/v1/callbacks/{callbackid}
        Method: put

        Parameters:
        callbackid: Id of the callback to be updated
        body: callback object to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/callbacks/{callbackid}"
        return self._request("put", url, json=body)
