"""
TANSS API Tools - remote supports
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class RemoteSupportsTools(BaseTool):
    """Tools for remote supports operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize remote supports tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_remotesupports_v1(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates/imports a remote support into the database
        
        Path: /api/remoteSupports/v1
        Method: post

        Parameters:
        body: remote object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1"
        return self._request("post", url, json=body)

    def put_v1_list(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get list of remote supports

        Path: /api/remoteSupports/v1
        Method: put

        Parameters:
        body: filter settings

        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1"
        return self._request("put", url, json=body)

    def get_remotesupports_v1(self, remotesupportid: int) -> Dict[str, Any]:
        """
        Get remote support by id
        
        Path: /api/remoteSupports/v1/{remotesupportid}
        Method: get

        Parameters:
        remotesupportid: Id of the remote support to be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/{remotesupportid}"
        return self._request("get", url)

    def put_remotesupports_v1(self, remotesupportid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a remote support
        
        Path: /api/remoteSupports/v1/{remotesupportid}
        Method: put

        Parameters:
        remotesupportid: Id of the remote support to be updated
        body: new values for the remote support object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/{remotesupportid}"
        return self._request("put", url, json=body)

    def delete_remotesupports_v1(self, remotesupportid: int) -> Dict[str, Any]:
        """
        Delete remote support
        
        Path: /api/remoteSupports/v1/{remotesupportid}
        Method: delete

        Parameters:
        remotesupportid: Id of the remote support to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/{remotesupportid}"
        return self._request("delete", url)

    def get_v1_assigndevice(self) -> Dict[str, Any]:
        """
        Gets all device assignments
        
        Path: /api/remoteSupports/v1/assignDevice
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/assignDevice"
        return self._request("get", url)

    def post_v1_assigndevice(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a device assignment
        
        Path: /api/remoteSupports/v1/assignDevice
        Method: post

        Parameters:
        body: object containing the assignment of "`deviceId` -> `company` / `linkTypeId` / `linkId`"
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/assignDevice"
        return self._request("post", url, json=body)

    def delete_v1_assigndevice(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deletes a device assignment
        
        Path: /api/remoteSupports/v1/assignDevice
        Method: delete

        Parameters:
        body: object containing the assignment of "`type` + `deviceId` -> `company` / `linkTypeId` / `linkId`"
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/assignDevice"
        return self._request("delete", url, json=body)

    def get_v1_assignemployee(self) -> Dict[str, Any]:
        """
        Gets all technician assignments
        
        Path: /api/remoteSupports/v1/assignEmployee
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/assignEmployee"
        return self._request("get", url)

    def post_v1_assignemployee(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a technician assignment
        
        Path: /api/remoteSupports/v1/assignEmployee
        Method: post

        Parameters:
        body: object containing the assignment of "`type` + `userId` -> `employeeId`"
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/assignEmployee"
        return self._request("post", url, json=body)

    def delete_v1_assignemployee(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delets a technician assignment
        
        Path: /api/remoteSupports/v1/assignEmployee
        Method: delete

        Parameters:
        body: object containing the assignment of "`type` + `userId` -> `employeeId`"
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/remoteSupports/v1/assignEmployee"
        return self._request("delete", url, json=body)
