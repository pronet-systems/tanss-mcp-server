"""
TANSS API Tools - employees
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class EmployeesTools(BaseTool):
    """Tools for employees operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize employees tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_employees_technicians(self, freelancercompanyid: Optional[int] = None) -> Dict[str, Any]:
        """
        Gets all technicians
        
        Path: /api/v1/employees/technicians
        Method: get

        Parameters:
        freelancercompanyid: If this parameter is given, also fetches the freelancers of this company (0 if all freelancers shall be retrieved)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/employees/technicians"
        params = {}
        if freelancercompanyid is not None:
            params["freelancerCompanyId"] = freelancercompanyid
        return self._request("get", url, params=params)

    def post_v1_employees(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        creates an employee
        
        Path: /api/v1/employees
        Method: post

        Parameters:
        body: employee object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/employees"
        return self._request("post", url, json=body)
