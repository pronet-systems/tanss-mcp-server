"""
TANSS API Tools - checklists
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ChecklistsTools(BaseTool):
    """Tools for checklists operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize checklists tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_checklists_assignment(self, linktypeid: int, linkid: int, checklistid: int) -> Dict[str, Any]:
        """
        Assigns a checklist to a ticket
        
        Path: /api/v1/checklists/assignment/{linktypeid}/{linkid}/{checklistid}
        Method: post

        Parameters:
        linktypeid: linkTypeId (11 = ticket)
        linkid: id of the ticket
        checklistid: id of the checklist
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/checklists/assignment/{linktypeid}/{linkid}/{checklistid}"
        return self._request("post", url)

    def delete_checklists_assignment(self, linktypeid: int, linkid: int, checklistid: int) -> Dict[str, Any]:
        """
        Removes a checklist from a ticket
        
        Path: /api/v1/checklists/assignment/{linktypeid}/{linkid}/{checklistid}
        Method: delete

        Parameters:
        linktypeid: linkTypeId (11 = ticket)
        linkid: id of the ticket
        checklistid: id of the checklist
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/checklists/assignment/{linktypeid}/{linkid}/{checklistid}"
        return self._request("delete", url)

    def get_checklists_assignment(self, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        Gets checklists for a ticket
        
        Path: /api/v1/checklists/assignment/{linktypeid}/{linkid}
        Method: get

        Parameters:
        linktypeid: linkTypeId (11 = ticket)
        linkid: id of the ticket
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/checklists/assignment/{linktypeid}/{linkid}"
        return self._request("get", url)

    def get_checklists_process(self, checklistid: int, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        Gets checklist for ticket
        
        Path: /api/v1/checklists/{checklistid}/process
        Method: get

        Parameters:
        checklistid: id of the checklist
        linktypeid: linkTypeId (11 = ticket)
        linkid: id of the ticket
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/checklists/{checklistid}/process"
        params = {}
        if linktypeid is not None:
            params["linkTypeId"] = linktypeid
        if linkid is not None:
            params["linkId"] = linkid
        return self._request("get", url, params=params)

    def put_checklists_check(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Check an item
        
        Path: /api/v1/checklists/check
        Method: put

        Parameters:
        body: infos regarding the item to be checked
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/checklists/check"
        return self._request("put", url, json=body)
