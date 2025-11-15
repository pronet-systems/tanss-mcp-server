# TANSS MCP Server

A comprehensive Model Context Protocol (MCP) server for the TANSS API, providing seamless integration with AI assistants like Claude or n8n.

**Version:** 1.0.0  
**Author:** Sebastian Michel  
**Company:** ProNet Systems GmbH  
**Website:** https://www.pronet-systems.de

---

## What is this?

The TANSS MCP Server bridges the gap between AI assistants (like Claude/n8n) and the TANSS ticket management system. It exposes **238 API endpoints** through **237 tools** that can be called by AI assistants to:

- 🎫 Create and manage tickets
- 📞 Handle phone calls and call assignments
- 💬 Manage chats and communications
- 🖥️ Track IT assets (PCs, peripherals, components)
- 👥 Manage employees and companies
- ⏱️ Track time and timestamps
- 📊 Create offers and invoices
- 🔧 Handle remote support sessions
- 📈 Monitor systems and devices
- And much more!

---

## Features

✅ **238 API endpoints** covering all TANSS functionality
✅ **237 tools** (e.g., `create_ticket`)
✅ **Dual transport modes**: stdio and SSE (HTTP)
✅ **Role-based authentication**: Support for 6 different token types
✅ **Automatic token management**: Bearer prefix handling and role-specific token prioritization
---

## Quick Start

### Prerequisites

- Python 3.8+
- TANSS account with API access
- API token from TANSS

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd tanss-mcp
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure the server**

Create `config.ini` from the example:
```bash
cp config.ini.example config.ini
```

Edit `config.ini` and add your TANSS credentials:
```ini
[tanss]
base_url = https://your-tanss-instance.com/backend/
api_token = your_api_token_here

[credentials]
username = your_username
password = your_password
```

4. **Start the server**

**For Claude Desktop (stdio mode):**
```bash
python3 server.py --mode stdio
```

**For web clients (SSE mode):**
```bash
python3 server.py --mode sse --host 0.0.0.0 --port 3001
```

---

## Configuration

### Basic Configuration

Minimal `config.ini`:
```ini
[tanss]
base_url = https://your-tanss.com/backend/
api_token = your_access_token

[sse]
host = 127.0.0.1
port = 3001
```

### Advanced Configuration with Role-Specific Tokens

For enhanced security and permissions, configure role-specific tokens:

```ini
[tanss]
base_url = https://your-tanss.com/backend/
api_token = your_main_token

# Optional: Role-specific tokens for specialized operations
erp_api_token = Bearer your_erp_token
phone_api_token = Bearer your_phone_token
remote_support_api_token = Bearer your_remote_support_token
monitoring_api_token = Bearer your_monitoring_token
device_management_api_token = Bearer your_device_mgmt_token
timestamp_api_token = Bearer your_timestamp_token

[sse]
host = 192.168.0.153
port = 3001
reload = false
log_level = info

[credentials]
username = your_username
password = your_password
```

---

## Usage

### With Claude Desktop

Add to your Claude Desktop MCP settings (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "tanss": {
      "command": "python3",
      "args": ["/absolute/path/to/tanss-mcp/server.py"],
      "cwd": "/absolute/path/to/tanss-mcp"
    }
  }
}
```

Restart Claude Desktop, and you'll have access to all TANSS tools!

### As SSE Server

```bash
# Start server
python3 server.py --mode sse --host 0.0.0.0 --port 3001

# The server will be available at:
# SSE endpoint: http://your-host:3001/sse
# Messages endpoint: http://your-host:3001/messages
```

### Getting Your API Token

Use the `login` tool or the test script:

```bash
# Start SSE server first
python3 server.py --mode sse

# In another terminal, test login
python3 test_login.py
```

This will generate access and refresh tokens you can use in `config.ini`.

---

## Available Tools

The server provides **237 human-friendly tools** across **41 categories**.

### Most Common Tools

#### 🎫 Ticket Management (37 tools)
- `create_ticket` - Create a new ticket
- `get_ticket` - Get ticket details
- `update_ticket` - Update an existing ticket
- `delete_ticket` - Delete a ticket
- `get_my_tickets` - Get your assigned tickets
- `get_all_tickets` - Get all tickets
- `get_company_tickets` - Get tickets for a company
- `add_ticket_comment` - Add a comment to a ticket
- `get_ticket_history` - View ticket change history
- `upload_ticket_file` - Upload a file to a ticket

#### ⏱️ Time Tracking (15 tools)
- `create_timestamp` - Clock in/out or log time
- `get_timestamps` - Get time records
- `close_day` - Close the day for time tracking
- `get_timestamp_statistics` - Get time statistics

#### 💬 Chats (10 tools)
- `create_chat` - Start a new chat
- `send_chat_message` - Send a message
- `close_chat` - Close a chat
- `reopen_chat` - Reopen a closed chat
- `add_chat_participant` - Add someone to a chat

#### 📞 Phone Calls (8 tools)
- `create_call` - Log a phone call
- `get_my_calls` - Get your calls
- `identify_caller` - Identify a caller by phone number
- `assign_call_to_employee` - Assign a call

#### 🔧 Remote Support (9 tools)
- `create_remote_support` - Create a remote support session
- `list_remote_supports` - List all remote support sessions
- `assign_device_to_remote_support` - Link a device
- `assign_employee_to_remote_support` - Assign a technician

#### 💼 ERP Integration (15 tools)
- `get_company_employees` - Get employees of a company
- `get_company_departments` - Get departments
- `get_ticket_types` - Get available ticket types
- `get_ticket_statuses` - Get available ticket statuses
- `create_invoice` - Create an invoice
- `create_customer` - Create a customer

#### 🖥️ IT Asset Management
- `create_pc` / `update_pc` / `delete_pc` - Manage computers
- `create_peripheral` / `update_peripheral` - Manage peripherals
- `create_component` / `update_component` - Manage components
- `get_operating_system` - Get OS information

#### 📋 Offers & Quotes (13 tools)
- `create_offer` - Create a new offer/quote
- `update_offer` - Update an offer
- `get_offer_template` - Get offer templates

#### 🔐 Authentication
- `login` - Login and get API tokens

### Complete Tool List


**Total Tools:** 237

| Tool Name | Category |
|-----------|----------|
| `get_ticket` | Ticket Operations |
| `create_ticket` | Ticket Operations |
| `update_ticket` | Ticket Operations |
| `delete_ticket` | Ticket Operations |
| `get_ticket_history` | Ticket Operations |
| `add_ticket_comment` | Ticket Operations |
| `get_my_tickets` | Ticket Lists |
| `get_all_tickets` | Ticket Lists |
| `get_company_tickets` | Ticket Lists |
| `get_technician_tickets` | Ticket Lists |
| `get_repair_tickets` | Ticket Lists |
| `get_project_tickets` | Ticket Lists |
| `get_tickets_by_role` | Ticket Lists |
| `get_unidentified_tickets` | Ticket Lists |
| `get_admin_tickets` | Ticket Lists |
| `update_ticket_list` | Ticket Lists |
| `get_ticket_document` | Ticket Content |
| `get_ticket_screenshot` | Ticket Content |
| `upload_ticket_file` | Ticket Content |
| `get_ticket_states` | Ticket States |
| `create_ticket_state` | Ticket States |
| `update_ticket_state` | Ticket States |
| `delete_ticket_state` | Ticket States |
| `get_call` | Phone Calls |
| `create_call` | Phone Calls |
| `update_call` | Phone Calls |
| `get_call_assignments` | Phone Calls |
| `assign_call_to_employee` | Phone Calls |
| `unassign_call_from_employee` | Phone Calls |
| `identify_caller` | Phone Calls |
| `send_call_notification` | Phone Calls |
| `get_my_calls` | User Phone Calls |
| `update_my_call` | User Phone Calls |
| `identify_my_caller` | User Phone Calls |
| `get_remote_support` | Remote Support |
| `create_remote_support` | Remote Support |
| `list_remote_supports` | Remote Support |
| `update_remote_support` | Remote Support |
| `delete_remote_support` | Remote Support |
| `get_remote_support_devices` | Remote Support |
| `assign_device_to_remote_support` | Remote Support |
| `unassign_device_from_remote_support` | Remote Support |
| `get_remote_support_employees` | Remote Support |
| `assign_employee_to_remote_support` | Remote Support |
| `unassign_employee_from_remote_support` | Remote Support |
| `get_monitoring_ticket` | Monitoring |
| `create_monitoring_ticket` | Monitoring |
| `update_monitoring_ticket` | Monitoring |
| `get_monitoring_groups` | Monitoring |
| `assign_monitoring_group` | Monitoring |
| `unassign_monitoring_group` | Monitoring |
| `get_tickets_from_monitoring_group` | Monitoring |
| `get_company_departments` | ERP Integration |
| `get_company_employees` | ERP Integration |
| `get_department_employees` | ERP Integration |
| `get_employee_departments` | ERP Integration |
| `search_company_by_id` | ERP Integration |
| `get_ticket_statuses` | ERP Integration |
| `get_ticket_types` | ERP Integration |
| `get_company_categories` | ERP Integration |
| `create_company_category` | ERP Integration |
| `get_customers` | ERP Integration |
| `create_customer` | ERP Integration |
| `get_invoices` | ERP Integration |
| `create_invoice` | ERP Integration |
| `create_erp_ticket` | ERP Integration |
| `upload_ticket_file_erp` | ERP Integration |
| `get_timestamps` | Time Tracking |
| `create_timestamp` | Time Tracking |
| `update_timestamp` | Time Tracking |
| `get_timestamp_info` | Time Tracking |
| `get_timestamp_statistics` | Time Tracking |
| `get_pause_configs` | Time Tracking |
| `create_pause_config` | Time Tracking |
| `update_pause_config` | Time Tracking |
| `delete_pause_config` | Time Tracking |
| `get_day_closing` | Time Tracking |
| `create_day_closing` | Time Tracking |
| `delete_day_closing` | Time Tracking |
| `close_day` | Time Tracking |
| `update_day` | Time Tracking |
| `set_employee_initial_balance` | Time Tracking |
| `get_chat` | Chats |
| `create_chat` | Chats |
| `update_chat` | Chats |
| `get_chat_close_requests` | Chats |
| `close_chat` | Chats |
| `update_chat_close` | Chats |
| `reopen_chat` | Chats |
| `send_chat_message` | Chats |
| `add_chat_participant` | Chats |
| `remove_chat_participant` | Chats |
| `get_offer` | Offers |
| `create_offer` | Offers |
| `update_offer` | Offers |
| `update_offers` | Offers |
| `delete_offer` | Offers |
| `get_offer_template` | Offers |
| `create_offer_template` | Offers |
| `update_offer_template` | Offers |
| `delete_offer_template` | Offers |
| `get_erp_selection` | Offers |
| `create_erp_selection` | Offers |
| `update_erp_selection` | Offers |
| `delete_erp_selection` | Offers |
| `get_material_picker` | Offers |
| `get_availability` | Availability |
| `get_technicians` | Employees |
| `create_employee` | Employees |
| `get_tag` | Tags |
| `create_tag` | Tags |
| `update_tag` | Tags |
| `delete_tag` | Tags |
| `get_tag_assignments` | Tags |
| `assign_tag` | Tags |
| `update_tag_assignment` | Tags |
| `unassign_tag` | Tags |
| `get_tag_assignment_log` | Tags |
| `get_callback` | Callbacks |
| `create_callback` | Callbacks |
| `update_callback` | Callbacks |
| `search` | Search |
| `get_checklist_assignments` | Checklists |
| `assign_checklist` | Checklists |
| `unassign_checklist` | Checklists |
| `get_checklist_process` | Checklists |
| `check_checklist_item` | Checklists |
| `get_support_session` | Support Sessions |
| `create_support_session` | Support Sessions |
| `update_support_session` | Support Sessions |
| `update_support_list` | Support Sessions |
| `add_support_signature` | Support Sessions |
| `get_timer` | Timers |
| `create_timer` | Timers |
| `update_timer` | Timers |
| `delete_timer` | Timers |
| `get_timer_notes` | Timers |
| `update_timer_notes` | Timers |
| `delete_timer_notes` | Timers |
| `get_pc` | PCs/Computers |
| `create_pc` | PCs/Computers |
| `update_pc` | PCs/Computers |
| `delete_pc` | PCs/Computers |
| `get_peripheral` | Peripherals |
| `create_peripheral` | Peripherals |
| `update_peripheral` | Peripherals |
| `delete_peripheral` | Peripherals |
| `get_peripheral_types` | Peripherals |
| `create_peripheral_type` | Peripherals |
| `update_peripheral_type` | Peripherals |
| `delete_peripheral_type` | Peripherals |
| `install_builtin_peripheral` | Peripherals |
| `get_component` | Components |
| `create_component` | Components |
| `update_component` | Components |
| `delete_component` | Components |
| `get_component_types` | Components |
| `create_component_type` | Components |
| `update_component_type` | Components |
| `delete_component_type` | Components |
| `get_service` | Services |
| `create_service` | Services |
| `update_service` | Services |
| `delete_service` | Services |
| `get_ip_addresses` | IP Addresses |
| `create_ip_address` | IP Addresses |
| `update_ip_address` | IP Addresses |
| `delete_ip_address` | IP Addresses |
| `create_company` | Companies |
| `get_company_employees_list` | Companies |
| `get_company_category` | Company Categories |
| `create_company_category` | Company Categories |
| `update_company_category` | Company Categories |
| `delete_company_category` | Company Categories |
| `get_company_category_types` | Company Categories |
| `create_company_category_type` | Company Categories |
| `update_company_category_type` | Company Categories |
| `delete_company_category_type` | Company Categories |
| `get_document` | Documents |
| `create_document` | Documents |
| `upload_document` | Documents |
| `update_document` | Documents |
| `delete_document` | Documents |
| `get_webhook_rules` | Webhooks |
| `create_webhook_rule` | Webhooks |
| `update_webhook_rule` | Webhooks |
| `delete_webhook_rule` | Webhooks |
| `test_webhook` | Webhooks |
| `get_ticket_board` | Ticket Board |
| `get_ticket_board_project` | Ticket Board |
| `get_ticket_board_panel` | Ticket Board |
| `create_ticket_board_panel` | Ticket Board |
| `update_ticket_board_panel` | Ticket Board |
| `delete_ticket_board_panel` | Ticket Board |
| `get_project_registers` | Ticket Board |
| `get_panel_registers` | Ticket Board |
| `get_global_panels` | Ticket Board |
| `get_operating_system` | Operating Systems |
| `create_operating_system` | Operating Systems |
| `update_operating_system` | Operating Systems |
| `delete_operating_system` | Operating Systems |
| `get_manufacturer` | Manufacturers |
| `create_manufacturer` | Manufacturers |
| `update_manufacturer` | Manufacturers |
| `delete_manufacturer` | Manufacturers |
| `get_cpu` | CPUs |
| `create_cpu` | CPUs |
| `update_cpu` | CPUs |
| `delete_cpu` | CPUs |
| `get_hdd_type` | HDD Types |
| `create_hdd_type` | HDD Types |
| `update_hdd_type` | HDD Types |
| `delete_hdd_type` | HDD Types |
| `identify` | Identification |
| `get_email_account` | Email Accounts |
| `create_email_account` | Email Accounts |
| `update_email_account` | Email Accounts |
| `delete_email_account` | Email Accounts |
| `get_company_email_accounts` | Email Accounts |
| `get_email_account_types` | Email Accounts |
| `create_vacation_request` | Vacation Requests |
| `update_vacation_request` | Vacation Requests |
| `delete_vacation_request` | Vacation Requests |
| `update_vacation_request_list` | Vacation Requests |
| `get_vacation_days` | Vacation Requests |
| `set_vacation_days` | Vacation Requests |
| `get_vacation_additional_types` | Vacation Requests |
| `get_unseen_events` | Activity Feed |
| `mark_all_events_seen` | Activity Feed |
| `update_event` | Activity Feed |
| `get_domain` | Domains |
| `create_domain` | Domains |
| `update_domain` | Domains |
| `delete_domain` | Domains |
| `get_company_domains` | Domains |
| `login` | Authentication |
| `test_smtp` | Mail Testing |


### Tool Categories

| Category | Tools | Description |
|----------|-------|-------------|
| Tickets | 6 | Core ticket operations |
| Ticket Lists | 10 | Ticket filtering and views |
| Ticket Content | 3 | File uploads and screenshots |
| Ticket States | 4 | Ticket state management |
| Calls | 8 | Phone call management |
| Remote Support | 11 | Remote support sessions |
| Monitoring | 7 | System monitoring |
| ERP | 15 | ERP integration |
| Timestamp | 15 | Time tracking |
| Chats | 10 | Chat management |
| Offers | 14 | Offers and quotes |
| Tags | 9 | Tag management |
| Checklists | 5 | Checklist operations |
| Documents | 5 | Document management |
| Webhooks | 5 | Webhook configuration |
| Company | 2 | Company management |
| Employees | 2 | Employee operations |
| ... | ... | And 24 more categories |

---

## API Documentation

This MCP server implements the **TANSS API v10.10.0**.

**Official TANSS API Documentation:**
🔗 https://api-doc.tanss.de/#section/Documentation-of-the-TANSS-API.-Version:-10.10.0

The API documentation provides:
- Detailed endpoint specifications
- Request/response schemas
- Authentication requirements
- Parameter descriptions
- Example requests and responses

---

## Architecture

### Authentication Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        MCP Client                               │
│                    (Claude, etc.)                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ MCP Protocol
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    TANSS MCP Server                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Tool Catalog (237 tools)                                │  │
│  │  - create_ticket                                         │  │
│  │  - get_my_tickets                                        │  │
│  │  - create_remote_support                                 │  │
│  │  - ...                                                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Token Manager                                           │  │
│  │  - Main API Token                                        │  │
│  │  - Role-specific Tokens (ERP, Phone, etc.)              │  │
│  │  - Automatic Bearer prefix handling                      │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP + Custom apiToken header
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                        TANSS API                                │
│                     (v10.10.0)                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Token Priority

When making API calls, the server uses this token priority:
1. **Role-specific token** (if configured for that endpoint category)
2. **Main API token** (fallback)

Example:
- ERP endpoints use `erp_api_token` if configured, otherwise `api_token`
- Ticket endpoints always use `api_token`

### Custom Authentication Header

TANSS uses a **custom authentication header** instead of the standard `Authorization` header:

```python
headers = {
    'apiToken': 'Bearer <token>',  # TANSS-specific
    'Content-Type': 'application/json'
}
```

The server handles this automatically.

---

## Command-Line Options

```bash
python3 server.py --help
```

### Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--mode` | `stdio`, `sse` | `sse` | Transport mode |
| `--config` | path | `config.ini` | Config file path |
| `--host` | hostname | `127.0.0.1` | SSE server host |
| `--port` | number | `8000` | SSE server port |
| `--reload` | flag | `false` | Auto-reload on changes |
| `--log-level` | `debug`, `info`, `warning`, `error` | `info` | Logging level |

### Examples

```bash
# stdio mode (default for Claude Desktop)
python3 server.py --mode stdio

# SSE mode for local development
python3 server.py --mode sse

# SSE mode for network access
python3 server.py --mode sse --host 0.0.0.0 --port 3001

# Development mode with auto-reload
python3 server.py --mode sse --reload --log-level debug
```

---

## Security Notes

⚠️ **Important Security Considerations:**

- Use environment variables for tokens in production
- Rotate API tokens regularly
- Monitor token expiration dates
- Configure CORS properly for SSE mode in production
- Use HTTPS for production deployments

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## Support

**Author:** Sebastian Michel
**Company:** ProNet Systems GmbH
**Website:** https://www.pronet-systems.de

- Consult the official [TANSS API Documentation](https://api-doc.tanss.de/#section/Documentation-of-the-TANSS-API.-Version:-10.10.0)

---

**Made with ❤️ by ProNet Systems GmbH**
