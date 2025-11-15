"""
TANSS API Tools - domains
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class DomainsTools(BaseTool):
    """Tools for domains operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize domains tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_domains(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a domain
        
        Path: /api/v1/domains
        Method: post

        Parameters:
        body: domain object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/domains"
        return self._request("post", url, json=body)

    def get_v1_domains(self, id: int) -> Dict[str, Any]:
        """
        Gets a single domain
        
        Path: /api/v1/domains/{id}
        Method: get

        Parameters:
        id: id of the domain that shall be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/domains/{id}"
        return self._request("get", url)

    def put_v1_domains(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a domain
        
        Path: /api/v1/domains/{id}
        Method: put

        Parameters:
        id: id of the domain that shall be updated
        body: domain object to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/domains/{id}"
        return self._request("put", url, json=body)

    def delete_v1_domains(self, id: int) -> Dict[str, Any]:
        """
        Deletes a domain
        
        Path: /api/v1/domains/{id}
        Method: delete

        Parameters:
        id: id of the domain that shall be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/domains/{id}"
        return self._request("delete", url)

    def get_domains_company(self, id: int) -> Dict[str, Any]:
        """
        List of domains of a company
        
        Path: /api/v1/domains/company/{id}
        Method: get

        Parameters:
        id: id of the company
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/domains/company/{id}"
        return self._request("get", url)
