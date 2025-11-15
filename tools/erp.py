"""
TANSS API Tools - erp
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class ErpTools(BaseTool):
    """Tools for erp operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize erp tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_v1_invoices(self, apitoken: str, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Insert new invoices
        
        Path: /api/erp/v1/invoices
        Method: post

        Parameters:
        apitoken: ERP Api-Token
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/invoices"
        return self._request("post", url, json=body)

    def get_v1_invoices(self, apitoken: str, pdf: Optional[bool] = None) -> Dict[str, Any]:
        """
        Gets a list of billable supports
        
        Path: /api/erp/v1/invoices
        Method: get

        Parameters:
        apitoken: ERP Api-Token
        pdf: When set to true the response includes the support evaluation PDF without an invoice number in Base64 format
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/invoices"
        params = {}
        if pdf is not None:
            params["pdf"] = pdf
        return self._request("get", url, params=params)

    def get_v1_customers(self, apitoken: str, modified: float) -> Dict[str, Any]:
        """
        Get a list of customers and employees
        
        Path: /api/erp/v1/customers
        Method: get

        Parameters:
        apitoken: ERP Api-Token
        modified: Timestamp in seconds from which created or modified customers and employees will be send. If you set the value to -1 then all customers and employees will be send
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/customers"
        params = {}
        if modified is not None:
            params["modified"] = modified
        return self._request("get", url, params=params)

    def post_v1_customers(self, apitoken: str, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Insert new customers
        
        Path: /api/erp/v1/customers
        Method: post

        Parameters:
        apitoken: ERP Api-Token
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/customers"
        return self._request("post", url, json=body)

    def post_v1_tickets(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        create a new ticket
        
        Path: /api/erp/v1/tickets
        Method: post

        Parameters:
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/tickets"
        return self._request("post", url, json=body)

    def get_tickets_status(self) -> Dict[str, Any]:
        """
        gets a list of tickets states
        
        Path: /api/erp/v1/tickets/status
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/tickets/status"
        return self._request("get", url)

    def get_tickets_types(self) -> Dict[str, Any]:
        """
        gets a list of tickets types
        
        Path: /api/erp/v1/tickets/types
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/tickets/types"
        return self._request("get", url)

    def post_tickets_upload(self, ticketid: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        upload a document/image into a ticket
        
        Path: /api/erp/v1/tickets/{ticketid}/upload
        Method: post

        Parameters:
        ticketid: 
        body: Request body
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/tickets/{ticketid}/upload"
        return self._request("post", url, json=body)

    def get_companies_employees(self, companyid: Optional[str] = None) -> Dict[str, Any]:
        """
        get all employees of a company
        
        Path: /api/erp/v1/companies/employees
        Method: get

        Parameters:
        companyid: id of the company
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/companies/employees"
        params = {}
        if companyid is not None:
            params["companyId"] = companyid
        return self._request("get", url, params=params)

    def get_companies_departments(self) -> Dict[str, Any]:
        """
        gets all departments
        
        Path: /api/erp/v1/companies/departments
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/companies/departments"
        return self._request("get", url)

    def get_v1_companycategories(self) -> Dict[str, Any]:
        """
        list of company categories
        
        Path: /api/erp/v1/companyCategories
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/companyCategories"
        return self._request("get", url)

    def post_v1_companycategories(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new company category
        
        Path: /api/erp/v1/companyCategories
        Method: post

        Parameters:
        body: company category object to be saved
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/companyCategories"
        return self._request("post", url, json=body)

    def get_departments_employees(self, departmentid: int) -> Dict[str, Any]:
        """
        gets all employees of a department
        
        Path: /api/erp/v1/departments/{departmentid}/employees
        Method: get

        Parameters:
        departmentid: Id of the department
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/departments/{departmentid}/employees"
        return self._request("get", url)

    def get_companies_searchid(self, displayid: str) -> Dict[str, Any]:
        """
        search for a company
        
        Path: /api/erp/v1/companies/searchId/{displayid}
        Method: get

        Parameters:
        displayid: external customer number, which is used by the ERP system
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/companies/searchId/{displayid}"
        return self._request("get", url)

    def get_employees_departments(self, employeeid: int) -> Dict[str, Any]:
        """
        gets all departments of a employee
        
        Path: /api/erp/v1/employees/{employeeid}/departments
        Method: get

        Parameters:
        employeeid: Id of the employee
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/employees/{employeeid}/departments"
        return self._request("get", url)

    def get_employees_departments(self) -> Dict[str, Any]:
        """
        gets all users with the associated departments
        
        Path: /api/erp/v1/companies/employees/departments/
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/erp/v1/companies/employees/departments/"
        return self._request("get", url)
