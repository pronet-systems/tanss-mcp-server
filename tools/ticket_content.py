"""
TANSS API Tools - ticket content
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TicketContentTools(BaseTool):
    """Tools for ticket content operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize ticket content tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_tickets_documents(self, ticketid: int) -> Dict[str, Any]:
        """
        Gets all ticket documents
        
        Path: /api/v1/tickets/{ticketid}/documents
        Method: get

        Parameters:
        ticketid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}/documents"
        return self._request("get", url)

    def get_tickets_documents(self, ticketid: int, documentid: int) -> Dict[str, Any]:
        """
        Gets a ticket document
        
        Path: /api/v1/tickets/{ticketid}/documents/{documentid}
        Method: get

        Parameters:
        ticketid: 
        documentid: id of the document
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}/documents/{documentid}"
        return self._request("get", url)

    def get_tickets_screenshots(self, ticketid: int) -> Dict[str, Any]:
        """
        Gets all ticket images
        
        Path: /api/v1/tickets/{ticketid}/screenshots
        Method: get

        Parameters:
        ticketid: 
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}/screenshots"
        return self._request("get", url)

    def get_tickets_screenshots(self, ticketid: int, imageid: int) -> Dict[str, Any]:
        """
        Gets a ticket image
        
        Path: /api/v1/tickets/{ticketid}/screenshots/{imageid}
        Method: get

        Parameters:
        ticketid: 
        imageid: id of the image
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}/screenshots/{imageid}"
        return self._request("get", url)

    def post_tickets_upload(self, ticketid: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        upload a document/image
        
        Path: /api/v1/tickets/{ticketid}/upload
        Method: post

        Parameters:
        ticketid: 
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tickets/{ticketid}/upload"
        return self._request("post", url, json=body)
