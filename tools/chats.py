"""
TANSS API Tools - chats
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ChatsTools(BaseTool):
    """Tools for chats operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize chats tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_chats(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new chat
        
        Path: /api/v1/chats
        Method: post

        Parameters:
        body: chat object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats"
        return self._request("post", url, json=body)

    def put_v1_chats(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get a list of chats
        
        Path: /api/v1/chats
        Method: put

        Parameters:
        body: filter settings
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats"
        return self._request("put", url, json=body)

    def get_v1_chats(self, chatid: int, withmessages: Optional[bool] = None) -> Dict[str, Any]:
        """
        Gets a chat
        
        Path: /api/v1/chats/{chatid}
        Method: get

        Parameters:
        chatid: Id of the chat to be fetched
        withmessages: If "false" is given here, no messages will be loaded
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/{chatid}"
        params = {}
        if withmessages is not None:
            params["withMessages"] = withmessages
        return self._request("get", url, params=params)

    def get_chats_closerequests(self) -> Dict[str, Any]:
        """
        Gets chat close requests
        
        Path: /api/v1/chats/closeRequests
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/closeRequests"
        return self._request("get", url)

    def post_chats_messages(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new chat message
        
        Path: /api/v1/chats/messages
        Method: post

        Parameters:
        body: chat message to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/messages"
        return self._request("post", url, json=body)

    def post_chats_participants(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Adds a participant
        
        Path: /api/v1/chats/participants
        Method: post

        Parameters:
        body: chat participant object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/participants"
        return self._request("post", url, json=body)

    def delete_chats_participants(self, chatid: int, employeeid: int, departmentid: Optional[int] = None) -> Dict[str, Any]:
        """
        Deletes a participant
        
        Path: /api/v1/chats/participants
        Method: delete

        Parameters:
        chatid: Id of the chat
        employeeid: Either the id of the employee ...
        departmentid: ... or the id of the department
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/participants"
        params = {}
        if chatid is not None:
            params["chatId"] = chatid
        if employeeid is not None:
            params["employeeId"] = employeeid
        if departmentid is not None:
            params["departmentId"] = departmentid
        return self._request("delete", url, params=params)

    def post_chats_close(self, chatid: int) -> Dict[str, Any]:
        """
        Closes a chat
        
        Path: /api/v1/chats/close/{chatid}
        Method: post

        Parameters:
        chatid: Id of the chat
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/close/{chatid}"
        return self._request("post", url)

    def put_chats_close(self, chatid: int, accept: bool) -> Dict[str, Any]:
        """
        Accept/decline close request
        
        Path: /api/v1/chats/close/{chatid}
        Method: put

        Parameters:
        chatid: Id of the chat
        accept: true = accept cloe request / false = decline close request
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/close/{chatid}"
        params = {}
        if accept is not None:
            params["accept"] = accept
        return self._request("put", url, params=params)

    def post_chats_reopen(self, chatid: int) -> Dict[str, Any]:
        """
        re-opens a chat
        
        Path: /api/v1/chats/reOpen/{chatid}
        Method: post

        Parameters:
        chatid: Id of the chat
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/chats/reOpen/{chatid}"
        return self._request("post", url)
