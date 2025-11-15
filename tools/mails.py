"""
TANSS API Tools - mails
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class MailsTools(BaseTool):
    """Tools for mails operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize mails tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_test_smtp(self, receiver: str, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Test email smtp settings
        
        Path: /api/v1/mails/test/smtp
        Method: post

        Parameters:
        receiver: receiver of the test message
        body: email settings object to be used for sending
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/mails/test/smtp"
        params = {}
        if receiver is not None:
            params["receiver"] = receiver
        return self._request("post", url, params=params, json=body)
