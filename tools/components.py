"""
TANSS API Tools - components
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ComponentsTools(BaseTool):
    """Tools for components operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize components tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_components(self, componentid: int) -> Dict[str, Any]:
        """
        Gets a component by id
        
        Path: /api/v1/components/{componentid}
        Method: get

        Parameters:
        componentid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/{componentid}"
        return self._request("get", url)

    def put_v1_components(self, componentid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a component
        
        Path: /api/v1/components/{componentid}
        Method: put

        Parameters:
        componentid: 
        body: component object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/{componentid}"
        return self._request("put", url, json=body)

    def delete_v1_components(self, componentid: int) -> Dict[str, Any]:
        """
        Deletes a component
        
        Path: /api/v1/components/{componentid}
        Method: delete

        Parameters:
        componentid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/{componentid}"
        return self._request("delete", url)

    def post_v1_components(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a component
        
        Path: /api/v1/components
        Method: post

        Parameters:
        body: component object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components"
        return self._request("post", url, json=body)

    def put_v1_components(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gets a list of components
        
        Path: /api/v1/components
        Method: put

        Parameters:
        body: query parameters for the request
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components"
        return self._request("put", url, json=body)

    def get_components_types(self) -> Dict[str, Any]:
        """
        Gets a list of component types
        
        Path: /api/v1/components/types
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/types"
        return self._request("get", url)

    def post_components_types(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create component type
        
        Path: /api/v1/components/types
        Method: post

        Parameters:
        body: component type to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/types"
        return self._request("post", url, json=body)

    def put_components_types(self, typeid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update component type
        
        Path: /api/v1/components/types/{typeid}
        Method: put

        Parameters:
        typeid: type id to be updated
        body: component type to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/types/{typeid}"
        return self._request("put", url, json=body)

    def delete_components_types(self, typeid: int) -> Dict[str, Any]:
        """
        Delete component type
        
        Path: /api/v1/components/types/{typeid}
        Method: delete

        Parameters:
        typeid: type id to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/components/types/{typeid}"
        return self._request("delete", url)
