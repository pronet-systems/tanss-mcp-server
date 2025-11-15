"""
TANSS API Tools - emailAccounts
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class EmailaccountsTools(BaseTool):
    """Tools for emailAccounts operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize emailAccounts tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_emailaccounts(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates an email account
        
        Path: /api/v1/emailAccounts
        Method: post

        Parameters:
        body: account object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/emailAccounts"
        return self._request("post", url, json=body)

    def get_emailaccounts_compamy(self, companyid: int) -> Dict[str, Any]:
        """
        List accounts of company
        
        Path: /api/v1/emailAccounts/compamy/{companyid}
        Method: get

        Parameters:
        companyid: Id of the company
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/emailAccounts/compamy/{companyid}"
        return self._request("get", url)

    def get_v1_emailaccounts(self, id: int) -> Dict[str, Any]:
        """
        Gets an account
        
        Path: /api/v1/emailAccounts/{id}
        Method: get

        Parameters:
        id: Id of the E-mail account
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/emailAccounts/{id}"
        return self._request("get", url)

    def put_v1_emailaccounts(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Edit an accounts
        
        Path: /api/v1/emailAccounts/{id}
        Method: put

        Parameters:
        id: Id of the E-mail account
        body: account object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/emailAccounts/{id}"
        return self._request("put", url, json=body)

    def delete_v1_emailaccounts(self, id: int) -> Dict[str, Any]:
        """
        Deletes an account
        
        Path: /api/v1/emailAccounts/{id}
        Method: delete

        Parameters:
        id: Id of the E-mail account
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/emailAccounts/{id}"
        return self._request("delete", url)

    def get_emailaccounts_types(self) -> Dict[str, Any]:
        """
        List account types
        
        Path: /api/v1/emailAccounts/types
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/emailAccounts/types"
        return self._request("get", url)
