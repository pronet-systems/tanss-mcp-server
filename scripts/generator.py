#!/usr/bin/env python3
"""
Generator script to create MCP tools from TANSS API specification
"""
import yaml
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any


def sanitize_name(name: str) -> str:
    """Convert a string to a valid Python identifier"""
    # Replace special characters with underscores
    name = re.sub(r'[^\w\s]', '_', name)
    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name)
    # Remove consecutive underscores
    name = re.sub(r'_+', '_', name)
    # Remove leading/trailing underscores
    name = name.strip('_')
    # Make lowercase
    name = name.lower()
    # Ensure it doesn't start with a number
    if name and name[0].isdigit():
        name = f'n_{name}'
    
    # Handle Python reserved keywords
    reserved_keywords = {
        'from', 'to', 'in', 'for', 'while', 'if', 'else', 'elif',
        'return', 'def', 'class', 'import', 'as', 'try', 'except',
        'finally', 'with', 'lambda', 'yield', 'global', 'nonlocal',
        'pass', 'break', 'continue', 'raise', 'assert', 'del', 'and',
        'or', 'not', 'is', 'None', 'True', 'False', 'type', 'object'
    }
    
    if name in reserved_keywords:
        name = f'{name}_param'
    
    return name


def get_operation_id(path: str, method: str, summary: str) -> str:
    """Generate a unique operation ID"""
    # Clean path
    path_parts = [p for p in path.split('/') if p and not p.startswith('{')]
    path_name = '_'.join(path_parts[-2:]) if len(path_parts) >= 2 else path_parts[-1] if path_parts else 'api'
    
    # Combine with method
    op_id = f"{method}_{sanitize_name(path_name)}"
    
    return op_id


def extract_parameters(details: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract parameters from endpoint details"""
    params = []
    
    # Path and query parameters
    if 'parameters' in details:
        for param in details['parameters']:
            param_info = {
                'name': param['name'],
                'in': param['in'],
                'required': param.get('required', False),
                'type': param.get('schema', {}).get('type', 'string'),
                'description': param.get('description', '')
            }
            params.append(param_info)
    
    # Request body parameters
    if 'requestBody' in details:
        req_body = details['requestBody']
        if 'content' in req_body:
            for content_type, content in req_body['content'].items():
                if 'schema' in content:
                    params.append({
                        'name': 'body',
                        'in': 'body',
                        'required': req_body.get('required', False),
                        'type': 'object',
                        'description': req_body.get('description', 'Request body'),
                        'content_type': content_type
                    })
    
    return params


def generate_tool_class(tag: str, endpoints: List[Dict[str, Any]]) -> str:
    """Generate a Python class file for a tag/category"""
    class_name = ''.join(word.capitalize() for word in sanitize_name(tag).split('_'))
    
    code = f'''"""
TANSS API Tools - {tag}
Auto-generated from TANSS API specification v10.10.0
"""
from typing import Any, Dict, Optional, List
import httpx
from .base import BaseTool


class {class_name}Tools(BaseTool):
    """Tools for {tag} operations"""
    
    def __init__(self, base_url: str, api_token: str, role_specific_token: Optional[str] = None):
        """
        Initialize {tag} tools
        
        Args:
            base_url: TANSS API base URL
            api_token: Default API token (employee login)
            role_specific_token: Optional role-specific token (e.g., ERP, PHONE, MONITORING)
        """
        super().__init__(base_url, api_token, role_specific_token)
    
'''
    
    # Generate methods for each endpoint
    for endpoint in endpoints:
        method_name = sanitize_name(
            endpoint.get('operationId') or 
            get_operation_id(endpoint['path'], endpoint['method'], endpoint['summary'])
        )
        
        # Extract parameters
        params = endpoint.get('parameters', [])
        
        # Build method signature
        # Separate required and optional parameters
        required_params = []
        optional_params = []
        param_docs = []
        
        for param in params:
            param_name = sanitize_name(param['name'])
            param_type = param.get('type', 'str')
            
            # Map types
            type_map = {
                'integer': 'int',
                'string': 'str',
                'boolean': 'bool',
                'number': 'float',
                'object': 'Dict[str, Any]',
                'array': 'List[Any]'
            }
            python_type = type_map.get(param_type, 'Any')
            
            if param.get('required', False):
                required_params.append(f"{param_name}: {python_type}")
            else:
                optional_params.append(f"{param_name}: Optional[{python_type}] = None")
            
            param_docs.append(f"        {param_name}: {param.get('description', 'Parameter')}")
        
        # Combine parameters with required first, then optional
        param_list = ['self'] + required_params + optional_params
        signature = ', '.join(param_list)
        
        # Build docstring
        docstring = f'''        """
        {endpoint.get('summary', 'API operation')}
        
        Path: {endpoint['path']}
        Method: {endpoint['method']}
'''
        
        if param_docs:
            docstring += '\n        Parameters:\n' + '\n'.join(param_docs)
        
        docstring += '''
        
        Returns:
            API response as dictionary
        """'''
        
        # Build method body
        path_template = endpoint['path']
        
        # Extract path parameters
        path_params = [p for p in params if p.get('in') == 'path']
        query_params = [p for p in params if p.get('in') == 'query']
        body_param = next((p for p in params if p.get('in') == 'body'), None)
        
        # Build URL
        url_line = f'        url = f"{{self.base_url}}{path_template}"'
        
        # Build params dict
        params_code = ''
        if query_params:
            params_code = '        params = {}\n'
            for param in query_params:
                pname = sanitize_name(param['name'])
                params_code += f'        if {pname} is not None:\n'
                params_code += f'            params["{param["name"]}"] = {pname}\n'
        
        # Build request call
        method_lower = endpoint['method'].lower()
        request_args = []
        
        if query_params:
            request_args.append('params=params')
        
        if body_param:
            request_args.append('json=body')
        
        args_str = ', '.join(request_args)
        if args_str:
            args_str = ', ' + args_str
        
        request_line = f'        return self._request("{method_lower}", url{args_str})'
        
        # Complete method
        method_code = f'''
    def {method_name}({signature}) -> Dict[str, Any]:
{docstring}
{url_line}
{params_code}{request_line}
'''
        
        code += method_code
    
    return code


def main():
    # Load API spec
    with open('/mnt/user-data/uploads/tanss-api-10_10_0.yaml', 'r') as f:
        api_spec = yaml.safe_load(f)
    
    # Create output directory
    tools_dir = Path('tools')
    tools_dir.mkdir(exist_ok=True)
    
    # Group endpoints by tag
    from collections import defaultdict
    endpoints_by_tag = defaultdict(list)
    
    for path, methods in api_spec['paths'].items():
        for method, details in methods.items():
            if method in ['get', 'post', 'put', 'delete', 'patch']:
                tags = details.get('tags', ['untagged'])
                tag = tags[0] if tags else 'untagged'
                
                # Extract full endpoint info
                params = extract_parameters(details)
                
                endpoint_info = {
                    'path': path,
                    'method': method,
                    'tag': tag,
                    'summary': details.get('summary', ''),
                    'operationId': details.get('operationId', ''),
                    'parameters': params,
                    'responses': details.get('responses', {})
                }
                
                endpoints_by_tag[tag].append(endpoint_info)
    
    # Generate base tool class
    base_code = '''"""
Base tool class for TANSS API
"""
from typing import Any, Dict, Optional
import httpx


class BaseTool:
    """Base class for all TANSS API tools"""
    
    def __init__(self, base_url: str, api_token: str):
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.headers = {
            'Authorization': f'Bearer {api_token}',
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
'''
    
    with open(tools_dir / 'base.py', 'w') as f:
        f.write(base_code)
    
    # Generate tool class for each tag
    for tag, endpoints in endpoints_by_tag.items():
        class_name = sanitize_name(tag)
        filename = f"{class_name}.py"
        
        code = generate_tool_class(tag, endpoints)
        
        with open(tools_dir / filename, 'w') as f:
            f.write(code)
        
        print(f"Generated {filename} with {len(endpoints)} tools")
    
    # Generate __init__.py
    init_code = '"""TANSS API Tools"""\n\n'
    init_code += 'from .base import BaseTool\n\n'
    
    for tag in endpoints_by_tag.keys():
        class_name = ''.join(word.capitalize() for word in sanitize_name(tag).split('_'))
        module_name = sanitize_name(tag)
        init_code += f'from .{module_name} import {class_name}Tools\n'
    
    init_code += '\n__all__ = [\n'
    init_code += '    "BaseTool",\n'
    for tag in endpoints_by_tag.keys():
        class_name = ''.join(word.capitalize() for word in sanitize_name(tag).split('_'))
        init_code += f'    "{class_name}Tools",\n'
    init_code += ']\n'
    
    with open(tools_dir / '__init__.py', 'w') as f:
        f.write(init_code)
    
    # Save metadata
    metadata = {
        'total_endpoints': sum(len(eps) for eps in endpoints_by_tag.values()),
        'total_tags': len(endpoints_by_tag),
        'tags': {tag: len(eps) for tag, eps in endpoints_by_tag.items()}
    }
    
    with open('metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\nGeneration complete!")
    print(f"Total tags: {metadata['total_tags']}")
    print(f"Total endpoints: {metadata['total_endpoints']}")


if __name__ == '__main__':
    main()
