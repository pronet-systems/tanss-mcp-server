"""
TANSS API Tools - timers
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TimersTools(BaseTool):
    """Tools for timers operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize timers tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_timers(self) -> Dict[str, Any]:
        """
        Get all timers of current user
        
        Path: /api/v1/timers
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers"
        return self._request("get", url)

    def post_v1_timers(self) -> Dict[str, Any]:
        """
        Creates a timer
        
        Path: /api/v1/timers
        Method: post

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers"
        return self._request("post", url)

    def delete_v1_timers(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deletes a timer
        
        Path: /api/v1/timers
        Method: delete

        Parameters:
        body: timer object to be deleted. The only important field is the "id"
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers"
        return self._request("delete", url, json=body)

    def get_v1_timers(self, timerid: int) -> Dict[str, Any]:
        """
        Get a specific timer
        
        Path: /api/v1/timers/{timerid}
        Method: get

        Parameters:
        timerid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers/{timerid}"
        return self._request("get", url)

    def put_v1_timers(self, timerid: int) -> Dict[str, Any]:
        """
        Starts/stops timer
        
        Path: /api/v1/timers/{timerid}
        Method: put

        Parameters:
        timerid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers/{timerid}"
        return self._request("put", url)

    def get_timers_notes(self, timerid: int) -> Dict[str, Any]:
        """
        Get all timer fragments
        
        Path: /api/v1/timers/notes/{timerid}
        Method: get

        Parameters:
        timerid: id of the timer
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers/notes/{timerid}"
        return self._request("get", url)

    def delete_timers_notes(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deletes a timer fragment
        
        Path: /api/v1/timers/notes
        Method: delete

        Parameters:
        body: timer fragment to be deleted. The only important field is the "startTime" and "timerId"
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers/notes"
        return self._request("delete", url, json=body)

    def put_timers_notes(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a timer fragment
        
        Path: /api/v1/timers/notes
        Method: put

        Parameters:
        body: timer fragment to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timers/notes"
        return self._request("put", url, json=body)
