"""
TANSS API Tools - tags
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TagsTools(BaseTool):
    """Tools for tags operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize tags tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_tags(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new tag
        
        Path: /api/v1/tags
        Method: post

        Parameters:
        body: tag object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags"
        return self._request("post", url, json=body)

    def get_v1_tags(self) -> Dict[str, Any]:
        """
        Get all tags
        
        Path: /api/v1/tags
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags"
        return self._request("get", url)

    def get_v1_tags(self, id: int) -> Dict[str, Any]:
        """
        Gets a tag
        
        Path: /api/v1/tags/{id}
        Method: get

        Parameters:
        id: id of the tag
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/{id}"
        return self._request("get", url)

    def put_v1_tags(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Edits a tag
        
        Path: /api/v1/tags/{id}
        Method: put

        Parameters:
        id: id of the tag
        body: tag object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/{id}"
        return self._request("put", url, json=body)

    def delete_v1_tags(self, id: int) -> Dict[str, Any]:
        """
        Deletes a tag
        
        Path: /api/v1/tags/{id}
        Method: delete

        Parameters:
        id: id of the tag to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/{id}"
        return self._request("delete", url)

    def post_tags_assignment(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assigns a tag
        
        Path: /api/v1/tags/assignment
        Method: post

        Parameters:
        body: tag assignment object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/assignment"
        return self._request("post", url, json=body)

    def delete_tags_assignment(self, tagid: int, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        Removes a tag
        
        Path: /api/v1/tags/assignment
        Method: delete

        Parameters:
        tagid: id of the tag
        linktypeid: linkType of the assignment
        linkid: id of the assignment
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/assignment"
        params = {}
        if tagid is not None:
            params["tagId"] = tagid
        if linktypeid is not None:
            params["linkTypeId"] = linktypeid
        if linkid is not None:
            params["linkId"] = linkid
        return self._request("delete", url, params=params)

    def get_tags_assignment(self, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        List of tags to an assignment
        
        Path: /api/v1/tags/assignment
        Method: get

        Parameters:
        linktypeid: linkType of the assignment
        linkid: id of the assignment
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/assignment"
        params = {}
        if linktypeid is not None:
            params["linkTypeId"] = linktypeid
        if linkid is not None:
            params["linkId"] = linkid
        return self._request("get", url, params=params)

    def put_tags_assignment(self, linktypeid: int, linkid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assigns multiple tags
        
        Path: /api/v1/tags/assignment
        Method: put

        Parameters:
        linktypeid: linkType of the assignment
        linkid: id of the assignment
        body: tag assignment object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/assignment"
        params = {}
        if linktypeid is not None:
            params["linkTypeId"] = linktypeid
        if linkid is not None:
            params["linkId"] = linkid
        return self._request("put", url, params=params, json=body)

    def get_assignment_log(self, linktypeid: int, linkid: int) -> Dict[str, Any]:
        """
        List of tags logs to an assignment
        
        Path: /api/v1/tags/assignment/log
        Method: get

        Parameters:
        linktypeid: linkType of the assignment
        linkid: id of the assignment
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/tags/assignment/log"
        params = {}
        if linktypeid is not None:
            params["linkTypeId"] = linktypeid
        if linkid is not None:
            params["linkId"] = linkid
        return self._request("get", url, params=params)
