"""
TANSS API Tools - availability
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class AvailabilityTools(BaseTool):
    """Tools for availability operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize availability tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_availability(self, employeeids: str) -> Dict[str, Any]:
        """
        Fetches availability infos
        
        Path: /api/v1/availability
        Method: get

        Parameters:
        employeeids: Ids of the employees (comma separated)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/availability"
        params = {}
        if employeeids is not None:
            params["employeeIds"] = employeeids
        return self._request("get", url, params=params)
