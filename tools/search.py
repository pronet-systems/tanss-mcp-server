"""
TANSS API Tools - search
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class SearchTools(BaseTool):
    """Tools for search operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize search tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def put_v1_search(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        global search
        
        Path: /api/v1/search
        Method: put

        Parameters:
        body: defines the search parameters
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/search"
        return self._request("put", url, json=body)
