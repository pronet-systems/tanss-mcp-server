"""
TANSS API Tools - periphery
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class PeripheryTools(BaseTool):
    """Tools for periphery operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize periphery tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_peripheries(self, peripheryid: int) -> Dict[str, Any]:
        """
        Gets a periphery by id
        
        Path: /api/v1/peripheries/{peripheryid}
        Method: get

        Parameters:
        peripheryid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/{peripheryid}"
        return self._request("get", url)

    def put_v1_peripheries(self, peripheryid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a periphery
        
        Path: /api/v1/peripheries/{peripheryid}
        Method: put

        Parameters:
        peripheryid: 
        body: periphery object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/{peripheryid}"
        return self._request("put", url, json=body)

    def delete_v1_peripheries(self, peripheryid: int) -> Dict[str, Any]:
        """
        Deletes a periphery
        
        Path: /api/v1/peripheries/{peripheryid}
        Method: delete

        Parameters:
        peripheryid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/{peripheryid}"
        return self._request("delete", url)

    def post_v1_peripheries(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a periphery
        
        Path: /api/v1/peripheries
        Method: post

        Parameters:
        body: periphery object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries"
        return self._request("post", url, json=body)

    def put_v1_peripheries(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gets a list of peripheries
        
        Path: /api/v1/peripheries
        Method: put

        Parameters:
        body: query parameters for the request
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries"
        return self._request("put", url, json=body)

    def get_peripheries_types(self) -> Dict[str, Any]:
        """
        Get periphery types
        
        Path: /api/v1/peripheries/types
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/types"
        return self._request("get", url)

    def post_peripheries_types(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create periphery type
        
        Path: /api/v1/peripheries/types
        Method: post

        Parameters:
        body: periphery type to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/types"
        return self._request("post", url, json=body)

    def put_peripheries_types(self, typeid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update periphery type
        
        Path: /api/v1/peripheries/types/{typeid}
        Method: put

        Parameters:
        typeid: type id to be updated
        body: periphery type to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/types/{typeid}"
        return self._request("put", url, json=body)

    def delete_peripheries_types(self, typeid: int) -> Dict[str, Any]:
        """
        Delete periphery type
        
        Path: /api/v1/peripheries/types/{typeid}
        Method: delete

        Parameters:
        typeid: type id to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/types/{typeid}"
        return self._request("delete", url)

    def post_peripheries_buildin(self, peripheryid: int, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        Assign periphery
        
        Path: /api/v1/peripheries/{peripheryid}/buildIn/{linktypeid}/{linkid}
        Method: post

        Parameters:
        peripheryid: id of the periphery to be assigned
        linktypeid: link type of the "target" assignment (i.e. 1 = pc)
        linkid: link id of the "target" assignment (i.e. id of the pc)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/{peripheryid}/buildIn/{linktypeid}/{linkid}"
        return self._request("post", url)

    def delete_peripheries_buildin(self, peripheryid: int, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        Delete periphery assignment
        
        Path: /api/v1/peripheries/{peripheryid}/buildIn/{linktypeid}/{linkid}
        Method: delete

        Parameters:
        peripheryid: id of the periphery to be removed
        linktypeid: link type of the "target" assignment (i.e. 1 = pc)
        linkid: link id of the "target" assignment (i.e. id of the pc)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/peripheries/{peripheryid}/buildIn/{linktypeid}/{linkid}"
        return self._request("delete", url)
