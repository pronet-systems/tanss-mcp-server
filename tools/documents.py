"""
TANSS API Tools - documents
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class DocumentsTools(BaseTool):
    """Tools for documents operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize documents tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def put_v1_documents(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a list of company documents
        
        Path: /api/v1/documents
        Method: put

        Parameters:
        body: query parameters for retrieving documents
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/documents"
        return self._request("put", url, json=body)

    def post_v1_documents(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a document
        
        Path: /api/v1/documents
        Method: post

        Parameters:
        body: document with content
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/documents"
        return self._request("post", url, json=body)

    def get_v1_documents(self, id: int) -> Dict[str, Any]:
        """
        Get a single document (including content)
        
        Path: /api/v1/documents/{id}
        Method: get

        Parameters:
        id: Id of the document
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/documents/{id}"
        return self._request("get", url)

    def put_v1_documents(self, id: int) -> Dict[str, Any]:
        """
        Updates a document
        
        Path: /api/v1/documents/{id}
        Method: put

        Parameters:
        id: Id of the document
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/documents/{id}"
        return self._request("put", url)

    def delete_v1_documents(self, id: int) -> Dict[str, Any]:
        """
        Deletes a document
        
        Path: /api/v1/documents/{id}
        Method: delete

        Parameters:
        id: Id of the document
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/documents/{id}"
        return self._request("delete", url)

    def post_documents_file(self, id: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Uploads a file
        
        Path: /api/v1/documents/{id}/file
        Method: post

        Parameters:
        id: Id of the document
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/documents/{id}/file"
        return self._request("post", url, json=body)
