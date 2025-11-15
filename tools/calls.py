"""
TANSS API Tools - calls
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class CallsTools(BaseTool):
    """Tools for calls operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize calls tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_calls_v1(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates/imports a phone call into the database
        
        Path: /api/calls/v1
        Method: post

        Parameters:
        body: call object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1"
        return self._request("post", url, json=body)

    def put_calls_v1(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a list of phone calls
        
        Path: /api/calls/v1
        Method: put

        Parameters:
        body: filter settings
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1"
        return self._request("put", url, json=body)

    def get_calls_v1(self, id: int) -> Dict[str, Any]:
        """
        Get phone call by id
        
        Path: /api/calls/v1/{id}
        Method: get

        Parameters:
        id: Id of the phone call to be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/{id}"
        return self._request("get", url)

    def put_calls_v1(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update phone call
        
        Path: /api/calls/v1/{id}
        Method: put

        Parameters:
        id: Id of the phone call to be updated
        body: Updated phone call object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/{id}"
        return self._request("put", url, json=body)

    def post_v1_identify(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        identifies a phone call
        
        Path: /api/calls/v1/identify
        Method: post

        Parameters:
        body: call object to be identified
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/identify"
        return self._request("post", url, json=body)

    def get_v1_employeeassignment(self) -> Dict[str, Any]:
        """
        Get all employee assignments
        
        Path: /api/calls/v1/employeeAssignment
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/employeeAssignment"
        return self._request("get", url)

    def post_v1_employeeassignment(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new employee assignment
        
        Path: /api/calls/v1/employeeAssignment
        Method: post

        Parameters:
        body: Phone employee assignment
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/employeeAssignment"
        return self._request("post", url, json=body)

    def delete_v1_employeeassignment(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deletes an employee assignment
        
        Path: /api/calls/v1/employeeAssignment
        Method: delete

        Parameters:
        body: Phone employee assignment to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/employeeAssignment"
        return self._request("delete", url, json=body)

    def post_v1_notification(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a call notification
        
        Path: /api/calls/v1/notification
        Method: post

        Parameters:
        body: call object for this notification
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/calls/v1/notification"
        return self._request("post", url, json=body)
