#!/usr/bin/env python3
"""
TANSS API MCP Server
Supports both stdio and SSE (Server-Sent Events) transport modes

Author: Sebastian Michel
Company: ProNet Systems GmbH
Website: https://www.pronet-systems.de
Version: 1.0.0
"""
import asyncio
import json
import logging
from typing import Any, Dict, List, Optional
from configparser import ConfigParser
from pathlib import Path

# Version and author information
__version__ = "1.0.0"
__author__ = "Sebastian Michel"
__company__ = "ProNet Systems GmbH"
__website__ = "https://www.pronet-systems.de"

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server.sse import SseServerTransport
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
    ListToolsResult
)

# SSE-specific imports (only used in SSE mode)
try:
    from starlette.applications import Starlette
    from starlette.routing import Route, Mount
    from starlette.responses import Response
    from starlette.middleware.cors import CORSMiddleware
    import uvicorn
    SSE_AVAILABLE = True
except ImportError:
    SSE_AVAILABLE = False

# Import all tool classes
from tools import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('tanss-mcp-server')


class TANSSMCPServer:
    """MCP Server for TANSS API"""
    
    def __init__(self, config_path: str = "config.ini"):
        self.config = ConfigParser()
        self.config.read(config_path)

        # Load tool name mappings
        self.tool_name_mappings = {}
        self.reverse_name_mappings = {}
        try:
            with open('tool_names.json', 'r') as f:
                import json
                mappings_data = json.load(f)
                self.tool_name_mappings = {
                    k: v for k, v in mappings_data.get('mappings', {}).items()
                    if not k.startswith('_comment')
                }
                # Create reverse mapping (friendly name -> technical name)
                self.reverse_name_mappings = {v: k for k, v in self.tool_name_mappings.items()}
        except FileNotFoundError:
            logger.warning("tool_names.json not found, using technical names")
        
        # Load configuration
        self.base_url = self.config.get('tanss', 'base_url', fallback='https://api.tanss.de')
        self.api_token = self.config.get('tanss', 'api_token', fallback='')
        
        if not self.api_token:
            logger.warning("No API token configured. Set it in config.ini")
        
        # Load role-specific tokens
        self.erp_api_token = self.config.get('tanss', 'erp_api_token', fallback='')
        self.phone_api_token = self.config.get('tanss', 'phone_api_token', fallback='')
        self.remote_support_api_token = self.config.get('tanss', 'remote_support_api_token', fallback='')
        self.monitoring_api_token = self.config.get('tanss', 'monitoring_api_token', fallback='')
        self.device_management_api_token = self.config.get('tanss', 'device_management_api_token', fallback='')
        self.timestamp_api_token = self.config.get('tanss', 'timestamp_api_token', fallback='')
        
        # Initialize MCP server
        self.server = Server("tanss-mcp-server")
        
        # Initialize all tool instances with appropriate tokens
        self.tool_instances = {
            'security': SecurityTools(self.base_url, self.api_token),
            'tickets': TicketsTools(self.base_url, self.api_token),
            'ticket_lists': TicketListsTools(self.base_url, self.api_token),
            'ticket_content': TicketContentTools(self.base_url, self.api_token),
            'ticket_states': TicketStatesTools(self.base_url, self.api_token),
            'calls': CallsTools(self.base_url, self.api_token, self.phone_api_token),  # Use phone token
            'calls_user_context': CallsUserContextTools(self.base_url, self.api_token),
            'remote_supports': RemoteSupportsTools(self.base_url, self.api_token, self.remote_support_api_token),  # Use remote support token
            'monitoring': MonitoringTools(self.base_url, self.api_token, self.monitoring_api_token),  # Use monitoring token
            'erp': ErpTools(self.base_url, self.api_token, self.erp_api_token),  # Use ERP token
            'timestamp': TimestampTools(self.base_url, self.api_token, self.timestamp_api_token),  # Optional timestamp token
            'chats': ChatsTools(self.base_url, self.api_token),
            'offer': OfferTools(self.base_url, self.api_token),
            'availability': AvailabilityTools(self.base_url, self.api_token),
            'employees': EmployeesTools(self.base_url, self.api_token),
            'mails': MailsTools(self.base_url, self.api_token),
            'tags': TagsTools(self.base_url, self.api_token),
            'callback': CallbackTools(self.base_url, self.api_token),
            'search': SearchTools(self.base_url, self.api_token),
            'checklists': ChecklistsTools(self.base_url, self.api_token),
            'supports': SupportsTools(self.base_url, self.api_token),
            'timers': TimersTools(self.base_url, self.api_token),
            'pc': PcTools(self.base_url, self.api_token, self.device_management_api_token),  # Optional device mgmt token
            'periphery': PeripheryTools(self.base_url, self.api_token, self.device_management_api_token),
            'components': ComponentsTools(self.base_url, self.api_token, self.device_management_api_token),
            'services': ServicesTools(self.base_url, self.api_token, self.device_management_api_token),
            'ips': IpsTools(self.base_url, self.api_token, self.device_management_api_token),
            'company': CompanyTools(self.base_url, self.api_token),
            'company_category': CompanyCategoryTools(self.base_url, self.api_token),
            'documents': DocumentsTools(self.base_url, self.api_token),
            'webhooks': WebhooksTools(self.base_url, self.api_token),
            'ticket_board': TicketBoardTools(self.base_url, self.api_token),
            'operating_systems': OperatingSystemsTools(self.base_url, self.api_token, self.device_management_api_token),
            'manufacturer': ManufacturerTools(self.base_url, self.api_token, self.device_management_api_token),
            'cpus': CpusTools(self.base_url, self.api_token, self.device_management_api_token),
            'hddtypes': HddtypesTools(self.base_url, self.api_token, self.device_management_api_token),
            'identify': IdentifyTools(self.base_url, self.api_token),
            'emailaccounts': EmailaccountsTools(self.base_url, self.api_token),
            'vacationrequests': VacationrequestsTools(self.base_url, self.api_token),
            'activityfeed': ActivityfeedTools(self.base_url, self.api_token),
            'domains': DomainsTools(self.base_url, self.api_token),
        }
        
        # Build tool catalog
        self._build_tool_catalog()
        
        # Register handlers
        self._register_handlers()
        
        logger.info("TANSS MCP Server initialized")
        
        # Log which role-specific tokens are configured
        if self.erp_api_token and self.erp_api_token != 'YOUR_ERP_TOKEN_HERE':
            logger.info("ERP API token configured")
        if self.phone_api_token and self.phone_api_token != 'YOUR_PHONE_TOKEN_HERE':
            logger.info("Phone API token configured")
        if self.remote_support_api_token and self.remote_support_api_token != 'YOUR_REMOTE_SUPPORT_TOKEN_HERE':
            logger.info("Remote Support API token configured")
        if self.monitoring_api_token and self.monitoring_api_token != 'YOUR_MONITORING_TOKEN_HERE':
            logger.info("Monitoring API token configured")
        if self.device_management_api_token and self.device_management_api_token != 'YOUR_DEVICE_MANAGEMENT_TOKEN_HERE':
            logger.info("Device Management API token configured")
        if self.timestamp_api_token and self.timestamp_api_token != 'YOUR_TIMESTAMP_TOKEN_HERE':
            logger.info("Timestamp API token configured")
    
    def _build_tool_catalog(self):
        """Build catalog of all available tools"""
        self.tools = []
        
        for category, instance in self.tool_instances.items():
            # Get all methods from the tool instance
            methods = [method for method in dir(instance) 
                      if callable(getattr(instance, method)) 
                      and not method.startswith('_')]
            
            for method_name in methods:
                method = getattr(instance, method_name)
                
                # Get method docstring
                doc = method.__doc__ or f"{category} - {method_name}"
                
                # Extract description from docstring
                lines = doc.strip().split('\n')
                description = lines[0].strip() if lines else method_name
                
                # Parse parameters from method signature
                import inspect
                sig = inspect.signature(method)
                
                input_schema = {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
                
                for param_name, param in sig.parameters.items():
                    if param_name == 'self':
                        continue
                    
                    # Determine parameter type
                    param_type = "string"
                    if param.annotation != inspect.Parameter.empty:
                        annotation_str = str(param.annotation)
                        if 'int' in annotation_str:
                            param_type = "integer"
                        elif 'bool' in annotation_str:
                            param_type = "boolean"
                        elif 'float' in annotation_str:
                            param_type = "number"
                        elif 'Dict' in annotation_str or 'dict' in annotation_str:
                            param_type = "object"
                        elif 'List' in annotation_str or 'list' in annotation_str:
                            param_type = "array"
                    
                    input_schema["properties"][param_name] = {
                        "type": param_type,
                        "description": f"{param_name} parameter"
                    }
                    
                    # Check if required (no default value)
                    if param.default == inspect.Parameter.empty:
                        input_schema["required"].append(param_name)
                
                # Generate technical name
                technical_name = f"{category}_{method_name}"

                # Use friendly name if available, otherwise use technical name
                display_name = self.tool_name_mappings.get(technical_name, technical_name)

                tool = Tool(
                    name=display_name,
                    description=description[:200],  # Limit description length
                    inputSchema=input_schema
                )

                self.tools.append(tool)
        
        logger.info(f"Built catalog with {len(self.tools)} tools")
    
    def _register_handlers(self):
        """Register MCP handlers"""
        
        @self.server.list_tools()
        async def list_tools() -> ListToolsResult:
            """List all available tools"""
            return ListToolsResult(tools=self.tools)
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> CallToolResult:
            """Execute a tool"""
            try:
                # If friendly name is used, convert to technical name
                technical_name = self.reverse_name_mappings.get(name, name)

                # Parse tool name - match against known categories from longest to shortest
                category = None
                method_name = None

                # Sort categories by length (longest first) to match multi-word categories first
                sorted_categories = sorted(self.tool_instances.keys(), key=len, reverse=True)

                for cat in sorted_categories:
                    if technical_name.startswith(cat + '_'):
                        category = cat
                        method_name = technical_name[len(cat) + 1:]  # Remove category and underscore
                        break

                if not category or not method_name:
                    return CallToolResult(
                        content=[TextContent(
                            type="text",
                            text=f"Invalid tool name format: {name}"
                        )],
                        isError=True
                    )

                # Get tool instance
                if category not in self.tool_instances:
                    return CallToolResult(
                        content=[TextContent(
                            type="text",
                            text=f"Unknown tool category: {category}"
                        )],
                        isError=True
                    )
                
                instance = self.tool_instances[category]
                
                # Get method
                if not hasattr(instance, method_name):
                    return CallToolResult(
                        content=[TextContent(
                            type="text",
                            text=f"Unknown method: {method_name} in {category}"
                        )],
                        isError=True
                    )
                
                method = getattr(instance, method_name)
                
                # Call method
                result = method(**arguments)
                
                # Format result
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text=json.dumps(result, indent=2)
                    )]
                )
                
            except Exception as e:
                logger.error(f"Error calling tool {name}: {str(e)}", exc_info=True)
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text=f"Error: {str(e)}"
                    )],
                    isError=True
                )

    def _print_banner(self, mode: str, **kwargs):
        """Print startup banner with author and version information"""
        print()
        print("=" * 70)
        print("  TANSS MCP Server")
        print("=" * 70)
        print(f"  Version:  {__version__}")
        print(f"  Mode:     {mode.upper()}")
        print()
        print(f"  Author:   {__author__}")
        print(f"  Company:  {__company__}")
        print(f"  Website:  {__website__}")
        print("=" * 70)
        if kwargs:
            for key, value in kwargs.items():
                print(f"  {key.capitalize():10} {value}")
        print("=" * 70)
        print()

    async def run_stdio(self):
        """Run the MCP server using stdio transport"""
        self._print_banner("stdio")
        logger.info("TANSS MCP Server starting in stdio mode...")
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )

    def run_sse(self, host: str = "127.0.0.1", port: int = 8000, reload: bool = False, log_level: str = "info"):
        """Run the MCP server using SSE transport"""
        if not SSE_AVAILABLE:
            raise RuntimeError("SSE mode requires starlette and uvicorn. Install with: pip install starlette uvicorn")

        # Print banner with SSE details
        self._print_banner(
            "sse",
            host=host,
            port=port,
            sse_endpoint=f"http://{host}:{port}/sse",
            messages=f"http://{host}:{port}/messages",
            tools=len(self.tools),
            reload=reload
        )

        logger.info("TANSS MCP Server starting in SSE mode...")

        # Create SSE transport
        sse_transport = SseServerTransport("/messages")

        # Store reference for handlers
        mcp_server = self

        async def handle_sse(request):
            """Handle SSE connections"""
            async with sse_transport.connect_sse(
                request.scope,
                request.receive,
                request._send,
            ) as streams:
                await mcp_server.server.run(
                    streams[0],
                    streams[1],
                    mcp_server.server.create_initialization_options()
                )
            return Response()

        # Create Starlette app
        app = Starlette(
            routes=[
                Route("/sse", endpoint=handle_sse),
                Mount("/messages", app=sse_transport.handle_post_message),
            ]
        )

        # Add CORS middleware for web clients
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Configure appropriately for production
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Run server
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level=log_level,
            reload=reload
        )


def main():
    """Main entry point"""
    import sys
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='TANSS MCP Server')
    parser.add_argument(
        '--mode',
        choices=['stdio', 'sse'],
        default='sse',
        help='Server transport mode (default: stdio)'
    )
    parser.add_argument(
        '--config',
        default='config.ini',
        help='Path to configuration file (default: config.ini)'
    )
    parser.add_argument(
        '--host',
        default=None,
        help='SSE server host (default: from config or 127.0.0.1)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=None,
        help='SSE server port (default: from config or 8000)'
    )
    parser.add_argument(
        '--reload',
        action='store_true',
        help='Enable auto-reload in SSE mode (default: false)'
    )
    parser.add_argument(
        '--log-level',
        default='info',
        choices=['debug', 'info', 'warning', 'error'],
        help='Logging level (default: info)'
    )

    args = parser.parse_args()

    # Create server
    server = TANSSMCPServer(args.config)

    # Run server based on mode
    if args.mode == 'stdio':
        asyncio.run(server.run_stdio())
    elif args.mode == 'sse':
        # Load SSE config from file if not specified on command line
        config = ConfigParser()
        config.read(args.config)

        host = args.host or config.get('sse', 'host', fallback='127.0.0.1')
        port = args.port or config.getint('sse', 'port', fallback=8000)
        reload = args.reload or config.getboolean('sse', 'reload', fallback=False)

        server.run_sse(
            host=host,
            port=port,
            reload=reload,
            log_level=args.log_level
        )


if __name__ == "__main__":
    main()
