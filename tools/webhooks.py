"""
TANSS API Tools - webHooks
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class WebhooksTools(BaseTool):
    """Tools for webHooks operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize webHooks tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_tanssevents_rules(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        creates a rule
        
        Path: /api/v1/tanssEvents/rules
        Method: post

        Parameters:
        body: tanss event rule object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/rules"
        return self._request("post", url, json=body)

    def put_tanssevents_rules(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        get a list of rules
        
        Path: /api/v1/tanssEvents/rules
        Method: put

        Parameters:
        body: tanss event rule filter
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/rules"
        return self._request("put", url, json=body)

    def put_tanssevents_rules(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        updates a rule
        
        Path: /api/v1/tanssEvents/rules/{id}
        Method: put

        Parameters:
        id: id of the rule
        body: tanss event rule object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/rules/{id}"
        return self._request("put", url, json=body)

    def get_tanssevents_rules(self, id: int) -> Dict[str, Any]:
        """
        gets a rule
        
        Path: /api/v1/tanssEvents/rules/{id}
        Method: get

        Parameters:
        id: id of the rule
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/rules/{id}"
        return self._request("get", url)

    def delete_tanssevents_rules(self, id: int) -> Dict[str, Any]:
        """
        deletes a rule
        
        Path: /api/v1/tanssEvents/rules/{id}
        Method: delete

        Parameters:
        id: id of the rule
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/rules/{id}"
        return self._request("delete", url)

    def put_test_action(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        test a rule
        
        Path: /api/v1/tanssEvents/rules/test/action
        Method: put

        Parameters:
        body: tanss event test information
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tanssEvents/rules/test/action"
        return self._request("put", url, json=body)
