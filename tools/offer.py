"""
TANSS API Tools - offer
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class OfferTools(BaseTool):
    """Tools for offer operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize offer tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    

    def post_offers_erpselections(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new erp selection
        
        Path: /api/v1/offers/erpSelections
        Method: post

        Parameters:
        body: erp selection to be saved (including materials)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/erpSelections"
        return self._request("post", url, json=body)

    def get_offers_erpselections(self, erpselectionid: int) -> Dict[str, Any]:
        """
        Fetches an erp selection
        
        Path: /api/v1/offers/erpSelections/{erpselectionid}
        Method: get

        Parameters:
        erpselectionid: Id of the erp selection to be fetched
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/erpSelections/{erpselectionid}"
        return self._request("get", url)

    def put_offers_erpselections(self, erpselectionid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an erp selection
        
        Path: /api/v1/offers/erpSelections/{erpselectionid}
        Method: put

        Parameters:
        erpselectionid: Id of the erp selection to be updated
        body: erp selection to be saved (including materials)
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/erpSelections/{erpselectionid}"
        return self._request("put", url, json=body)

    def delete_offers_erpselections(self, erpselectionid: int) -> Dict[str, Any]:
        """
        Deletes an erp selection
        
        Path: /api/v1/offers/erpSelections/{erpselectionid}
        Method: delete

        Parameters:
        erpselectionid: Id of the erp selection to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/erpSelections/{erpselectionid}"
        return self._request("delete", url)

    def get_offers_templates(self) -> Dict[str, Any]:
        """
        Gets list of offer templates
        
        Path: /api/v1/offers/templates
        Method: get

        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/templates"
        return self._request("get", url)

    def post_offers_templates(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates an offer template
        
        Path: /api/v1/offers/templates
        Method: post

        Parameters:
        body: offer templates
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/templates"
        return self._request("post", url, json=body)

    def get_offers_templates(self, templateid: int) -> Dict[str, Any]:
        """
        Gets an offer templates
        
        Path: /api/v1/offers/templates/{templateid}
        Method: get

        Parameters:
        templateid: Id of the offer template
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/templates/{templateid}"
        return self._request("get", url)

    def put_offers_templates(self, templateid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an offer templates
        
        Path: /api/v1/offers/templates/{templateid}
        Method: put

        Parameters:
        templateid: Id of the offer template
        body: offer template
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/templates/{templateid}"
        return self._request("put", url, json=body)

    def delete_offers_templates(self, templateid: int) -> Dict[str, Any]:
        """
        Deletes an offer template
        
        Path: /api/v1/offers/templates/{templateid}
        Method: delete

        Parameters:
        templateid: Id of the offer template to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/templates/{templateid}"
        return self._request("delete", url)

    def get_erpselections_matpicker(self, source: str, searchtext: Optional[str] = None) -> Dict[str, Any]:
        """
        material picker
        
        Path: /api/v1/offers/erpSelections/matPicker
        Method: get

        Parameters:
        searchtext: if result should be filtered, the search text goes here
        source: determines the source for this picker
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/erpSelections/matPicker"
        params = {}
        if searchtext is not None:
            params["searchText"] = searchtext
        if source is not None:
            params["source"] = source
        return self._request("get", url, params=params)

    def get_erpselections_matpicker(self, erpselectionid: int) -> Dict[str, Any]:
        """
        material picker for erp selection
        
        Path: /api/v1/offers/erpSelections/matPicker/{erpselectionid}
        Method: get

        Parameters:
        erpselectionid: Id of the erp selection
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers/erpSelections/matPicker/{erpselectionid}"
        return self._request("get", url)

    def put_v1_offers(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gets list of offers
        
        Path: /api/v1/offers
        Method: put

        Parameters:
        body: filter settings for the offer list
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers"
        return self._request("put", url, json=body)

    def post_v1_offers(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates an offer
        
        Path: /api/v1/offers
        Method: post

        Parameters:
        body: offer object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offers"
        return self._request("post", url, json=body)

    def get_v1_offer(self, offerid: int) -> Dict[str, Any]:
        """
        Gets an offer
        
        Path: /api/v1/offer/{offerid}
        Method: get

        Parameters:
        offerid: Id of the offer
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offer/{offerid}"
        return self._request("get", url)

    def put_v1_offer(self, offerid: int, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an offer
        
        Path: /api/v1/offer/{offerid}
        Method: put

        Parameters:
        offerid: Id of the offer
        body: offer object
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offer/{offerid}"
        return self._request("put", url, json=body)

    def delete_v1_offer(self, offerid: int) -> Dict[str, Any]:
        """
        Deletes an offer
        
        Path: /api/v1/offer/{offerid}
        Method: delete

        Parameters:
        offerid: Id of the offer to be deleted
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/api/v1/offer/{offerid}"
        return self._request("delete", url)
