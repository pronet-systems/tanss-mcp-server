"""
TANSS API Tools - company category
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class CompanyCategoryTools(BaseTool):
    """Tools for company category operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize company category tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_companycategories(self) -> Dict[str, Any]:
        """
        list of categories
        
        Path: /api/v1/companyCategories
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories"
        return self._request("get", url)

    def post_v1_companycategories(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new company category
        
        Path: /api/v1/companyCategories
        Method: post

        Parameters:
        body: company category object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories"
        return self._request("post", url, json=body)

    def get_v1_companycategories(self, id: int) -> Dict[str, Any]:
        """
        gets a category
        
        Path: /api/v1/companyCategories/{id}
        Method: get

        Parameters:
        id: Id of the company category
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/{id}"
        return self._request("get", url)

    def put_v1_companycategories(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        updates a category
        
        Path: /api/v1/companyCategories/{id}
        Method: put

        Parameters:
        id: Id of the company category
        body: company category object to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/{id}"
        return self._request("put", url, json=body)

    def delete_v1_companycategories(self, id: int) -> Dict[str, Any]:
        """
        Deletes a company category
        
        Path: /api/v1/companyCategories/{id}
        Method: delete

        Parameters:
        id: Id of the company category
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/{id}"
        return self._request("delete", url)

    def get_companycategories_types(self) -> Dict[str, Any]:
        """
        list of company types
        
        Path: /api/v1/companyCategories/types
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/types"
        return self._request("get", url)

    def post_companycategories_types(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new company type
        
        Path: /api/v1/companyCategories/types
        Method: post

        Parameters:
        body: company ztype object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/types"
        return self._request("post", url, json=body)

    def get_companycategories_types(self, id: int) -> Dict[str, Any]:
        """
        gets a company type
        
        Path: /api/v1/companyCategories/types/{id}
        Method: get

        Parameters:
        id: Id of the company type
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/types/{id}"
        return self._request("get", url)

    def put_companycategories_types(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        updates a company type
        
        Path: /api/v1/companyCategories/types/{id}
        Method: put

        Parameters:
        id: Id of the company type
        body: company type object to be updated
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/types/{id}"
        return self._request("put", url, json=body)

    def delete_companycategories_types(self, id: int) -> Dict[str, Any]:
        """
        Deletes a company type
        
        Path: /api/v1/companyCategories/types/{id}
        Method: delete

        Parameters:
        id: Id of the company type
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/companyCategories/types/{id}"
        return self._request("delete", url)
