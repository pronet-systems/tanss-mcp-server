"""
TANSS API Tools - company
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class CompanyTools(BaseTool):
    """Tools for company operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize company tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_companies(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new company
        
        Path: /api/v1/companies
        Method: post

        Parameters:
        body: company object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companies"
        return self._request("post", url, json=body)

    def get_companies_employees(self, id: int) -> Dict[str, Any]:
        """
        Gets all employees of a company

        Path: /api/v1/companies/{companyid}/employees
        Method: get

        Parameters:
        id: Id of the company

        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companies/{id}/employees"
        return self._request("get", url)
