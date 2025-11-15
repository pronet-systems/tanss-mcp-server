"""
TANSS API Tools - vacationRequests
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class VacationrequestsTools(BaseTool):
    """Tools for vacationRequests operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize vacationRequests tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def put_vacationrequests_list(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gets a list of vacation requests
        
        Path: /api/v1/vacationRequests/list
        Method: put

        Parameters:
        body: query parameters for retrieving vacation requests
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests/list"
        return self._request("put", url, json=body)

    def get_vacationrequests_planningadditionaltypes(self) -> Dict[str, Any]:
        """
        Gets a list of absence/custom types
        
        Path: /api/v1/vacationRequests/planningAdditionalTypes
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests/planningAdditionalTypes"
        return self._request("get", url)

    def post_v1_vacationrequests(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        creates a vacation request
        
        Path: /api/v1/vacationRequests
        Method: post

        Parameters:
        body: vacation request to be stored
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests"
        return self._request("post", url, json=body)

    def put_v1_vacationrequests(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        updates a vacation request
        
        Path: /api/v1/vacationRequests/{id}
        Method: put

        Parameters:
        id: 
        body: vacation request to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests/{id}"
        return self._request("put", url, json=body)

    def delete_v1_vacationrequests(self, id: int) -> Dict[str, Any]:
        """
        deletes a vacation request
        
        Path: /api/v1/vacationRequests/{id}
        Method: delete

        Parameters:
        id: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests/{id}"
        return self._request("delete", url)

    def get_vacationdays_year(self, year: int) -> Dict[str, Any]:
        """
        gets the available vacation days per year
        
        Path: /api/v1/vacationRequests/vacationDays/year/{year}
        Method: get

        Parameters:
        year: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests/vacationDays/year/{year}"
        return self._request("get", url)

    def post_vacationrequests_vacationdays(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        sets the available vacation days per year
        
        Path: /api/v1/vacationRequests/vacationDays
        Method: post

        Parameters:
        body: infos on employee and vacation days per year
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/vacationRequests/vacationDays"
        return self._request("post", url, json=body)
