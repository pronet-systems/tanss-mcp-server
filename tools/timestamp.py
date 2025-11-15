"""
TANSS API Tools - timestamp
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class TimestampTools(BaseTool):
    """Tools for timestamp operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize timestamp tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def get_v1_timestamps(self, from_param: Optional[int] = None, till: Optional[int] = None) -> Dict[str, Any]:
        """
        gets a list of timestamps from a given period
        
        Path: /api/v1/timestamps
        Method: get

        Parameters:
        from_param: timestamp of start of period. if omitted,the beginning of the current day will be used
        till: timestamp of end of period. if omitted,the end of the current day will be used
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps"
        params = {}
        if from_param is not None:
            params["from"] = from_param
        if till is not None:
            params["till"] = till
        return self._request("get", url, params=params)

    def post_v1_timestamps(self, body: Dict[str, Any], autopause: Optional[bool] = None) -> Dict[str, Any]:
        """
        writes a timestamp into the database
        
        Path: /api/v1/timestamps
        Method: post

        Parameters:
        autopause: if true, a pause will automatically be inserted, if the minimum pause is not met for this day (see "pause config" routes)
        body: timestamp object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps"
        params = {}
        if autopause is not None:
            params["autoPause"] = autopause
        return self._request("post", url, params=params, json=body)

    def put_v1_timestamps(self, timestampid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        edits a single timestamp
        
        Path: /api/v1/timestamps/{timestampId}
        Method: put

        Parameters:
        timestampid: id of the timestamp
        body: timestamp object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/{timestampId}"
        return self._request("put", url, json=body)

    def put_timestamps_day(self, employeeid: int, day: str, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        writes the timstamps of a whole day into the database at once
        
        Path: /api/v1/timestamps/{employeeid}/day/{day}
        Method: put

        Parameters:
        employeeid: 
        day: 
        body: list of timestamps of the user for this day
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/{employeeid}/day/{day}"
        return self._request("put", url, json=body)

    def get_timestamps_info(self, from_param: Optional[int] = None, till: Optional[int] = None) -> Dict[str, Any]:
        """
        gets the timestamp infos for a given time period
        
        Path: /api/v1/timestamps/info
        Method: get

        Parameters:
        from_param: timestamp of start of period. if omitted,the beginning of the current day will be used
        till: timestamp of end of period. if omitted,the end of the current day will be used
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/info"
        params = {}
        if from_param is not None:
            params["from"] = from_param
        if till is not None:
            params["till"] = till
        return self._request("get", url, params=params)

    def get_timestamps_statistics(self, from_param: Optional[int] = None, till: Optional[int] = None, employeeids: Optional[str] = None) -> Dict[str, Any]:
        """
        gets the timestamp infos for a given time period (with statistical values)

        
        Path: /api/v1/timestamps/statistics
        Method: get

        Parameters:
        from_param: timestamp of start of period. if omitted,the beginning of the current day will be used
        till: timestamp of end of period. if omitted,the end of the current day will be used
        employeeids: id of all employees of whom the statistics shall be generated (comma sperated). Important you must have the
permission to view the statistics for this employee

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/statistics"
        params = {}
        if from_param is not None:
            params["from"] = from_param
        if till is not None:
            params["till"] = till
        if employeeids is not None:
            params["employeeIds"] = employeeids
        return self._request("get", url, params=params)

    def post_timestamps_dayclosing(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        does one or more "day closings" for the timestamp module
        
        Path: /api/v1/timestamps/dayClosing
        Method: post

        Parameters:
        body: Array of day closing identifiers (each representing the employee and date)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/dayClosing"
        return self._request("post", url, json=body)

    def delete_timestamps_dayclosing(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        remove / undo one or more "day closings" for the timestamp module
        
        Path: /api/v1/timestamps/dayClosing
        Method: delete

        Parameters:
        body: Array of day closing identifiers (each representing the employee and date)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/dayClosing"
        return self._request("delete", url, json=body)

    def get_dayclosing_tilldate(self) -> Dict[str, Any]:
        """
        gets all infos about last dayclosings for employees
        
        Path: /api/v1/timestamps/dayClosing/tillDate
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/dayClosing/tillDate"
        return self._request("get", url)

    def post_dayclosing_tilldate(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        created dayClosings to a given date
        
        Path: /api/v1/timestamps/dayClosing/tillDate
        Method: post

        Parameters:
        body: Parameters defining the request (date end list of employees)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/dayClosing/tillDate"
        return self._request("post", url, json=body)

    def post_employee_initialbalance(self, employeeid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        sets the initial balance for this employee
        
        Path: /api/v1/timestamps/employee/{employeeid}/initialBalance
        Method: post

        Parameters:
        employeeid: id of the employee
        body: Array of day closing identifiers (each representing the employee and date)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/employee/{employeeid}/initialBalance"
        return self._request("post", url, json=body)

    def get_timestamps_pauseconfigs(self) -> Dict[str, Any]:
        """
        gets a list of all pause configs
        
        Path: /api/v1/timestamps/pauseConfigs
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/pauseConfigs"
        return self._request("get", url)

    def post_timestamps_pauseconfigs(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        creates a pause config
        
        Path: /api/v1/timestamps/pauseConfigs
        Method: post

        Parameters:
        body: pause config object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/pauseConfigs"
        return self._request("post", url, json=body)

    def put_timestamps_pauseconfigs(self, id: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        updates a pause config
        
        Path: /api/v1/timestamps/pauseConfigs/{id}
        Method: put

        Parameters:
        id: id of the pause config
        body: pause config object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/pauseConfigs/{id}"
        return self._request("put", url, json=body)

    def delete_timestamps_pauseconfigs(self, id: int) -> Dict[str, Any]:
        """
        deletes a pause config
        
        Path: /api/v1/timestamps/pauseConfigs/{id}
        Method: delete

        Parameters:
        id: id of the pause config
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/timestamps/pauseConfigs/{id}"
        return self._request("delete", url)
