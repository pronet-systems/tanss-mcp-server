"""
TANSS API Tools - activityFeed
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ActivityfeedTools(BaseTool):
    """Tools for activityFeed operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize activityFeed tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def put_v1_tanssevents(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        List of user items
        
        Path: /api/v1/tanssEvents
        Method: put

        Parameters:
        body: list filter object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents"
        return self._request("put", url, json=body)

    def get_tanssevents_unseen(self) -> Dict[str, Any]:
        """
        Number of unseen events
        
        Path: /api/v1/tanssEvents/unseen
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/unseen"
        return self._request("get", url)

    def post_all_seen(self) -> Dict[str, Any]:
        """
        Marks all as seen
        
        Path: /api/v1/tanssEvents/mark/all/seen
        Method: post

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/mark/all/seen"
        return self._request("post", url)
