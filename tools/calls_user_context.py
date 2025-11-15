"""
TANSS API Tools - calls (user context)
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class CallsUserContextTools(BaseTool):
    """Tools for calls (user context) operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize calls (user context) tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def put_v1_phonecalls(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a list of phone calls
        
        Path: /api/v1/phoneCalls
        Method: put

        Parameters:
        body: filter settings
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/phoneCalls"
        return self._request("put", url, json=body)

    def get_v1_phonecalls(self, id: int) -> Dict[str, Any]:
        """
        Get phone call by id
        
        Path: /api/v1/phoneCalls/{id}
        Method: get

        Parameters:
        id: Id of the phone call to be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/phoneCalls/{id}"
        return self._request("get", url)

    def post_phonecalls_identify(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        identifies a phone call
        
        Path: /api/v1/phoneCalls/identify
        Method: post

        Parameters:
        body: call object to be identified
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/phoneCalls/identify"
        return self._request("post", url, json=body)
