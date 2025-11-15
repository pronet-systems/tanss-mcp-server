"""
Base tool class for TANSS API
"""
from typing import Any, Dict, Optional
import httpx


class BaseTool:
    """Base class for all TANSS API tools"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize base tool
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (ERP, PHONE, etc.)
        """
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.role_specific_token = role_specific_token
        
        # Determine which token to use
        # Role-specific token takes precedence if provided
        active_token = role_specific_token if role_specific_token else api_token

        # Add 'Bearer ' prefix if not present
        if active_token and not active_token.startswith('Bearer '):
            auth_header = f'Bearer {active_token}'
        else:
            auth_header = active_token

        # TANSS API uses custom 'apiToken' header instead of standard 'Authorization'
        self.headers = {
            'apiToken': auth_header,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def _request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to TANSS API"""
        # Merge headers
        headers = {**self.headers, **kwargs.pop('headers', {})}
        
        with httpx.Client(timeout=30.0) as client:
            response = client.request(
                method=method.upper(),
                url=url,
                headers=headers,
                **kwargs
            )
            response.raise_for_status()
            
            # Return JSON if available
            if response.headers.get('content-type', '').startswith('application/json'):
                return response.json()
            
            return {'status': response.status_code, 'content': response.text}
