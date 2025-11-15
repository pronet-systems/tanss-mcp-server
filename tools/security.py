"""
TANSS API Tools - security
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class SecurityTools(BaseTool):
    """Tools for security operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize security tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_login(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        logs in the user and generates an api token for further authentication
        
        Path: /api/v1/login
        Method: post

        Parameters:
        body: login credentials (as json)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/login"
        return self._request("post", url, json=body)
