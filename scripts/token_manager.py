#!/usr/bin/env python3
"""
TANSS API Token Management Utility
"""
import httpx
import json
from configparser import ConfigParser
from datetime import datetime, timedelta
from pathlib import Path


class TokenManager:
    """Manages TANSS API authentication tokens"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
    
    def login(self, username: str, password: str) -> dict:
        """
        Login to TANSS and get tokens
        
        Returns:
            dict with apiKey and refresh token
        """
        url = f"{self.base_url}/api/v1/login"
        
        with httpx.Client(timeout=30.0) as client:
            response = client.post(
                url,
                json={
                    'username': username,
                    'password': password
                }
            )
            response.raise_for_status()
            result = response.json()
            
            # Handle TANSS response format
            # Response structure: {'meta': {...}, 'content': {'apiKey': '...', 'refresh': '...', ...}}
            if 'content' in result:
                return result['content']
            
            # Fallback for different response formats
            return result
    
    def refresh_token(self, refresh_token: str) -> dict:
        """
        Refresh API token using refresh token
        
        Returns:
            dict with new apiKey and refresh token
        """
        # Any endpoint can be used with refresh token to get new tokens
        url = f"{self.base_url}/api/v1/employees"
        
        with httpx.Client(timeout=30.0) as client:
            response = client.get(
                url,
                headers={'Authorization': refresh_token}
            )
            response.raise_for_status()
            result = response.json()
            
            # Check if new tokens are in response
            if 'content' in result and 'apiKey' in result['content']:
                return result['content']
            
            return result
    
    def save_tokens(self, api_token: str, refresh_token: str, config_file: str = 'config.ini'):
        """Save tokens to config file"""
        config = ConfigParser()
        
        # Read existing config or create new
        if Path(config_file).exists():
            config.read(config_file)
        
        if 'tanss' not in config:
            config['tanss'] = {}
        
        # Remove 'Bearer ' prefix if present (TANSS includes it)
        api_token_clean = api_token.replace('Bearer ', '') if api_token.startswith('Bearer ') else api_token
        refresh_token_clean = refresh_token.replace('Bearer ', '') if refresh_token.startswith('Bearer ') else refresh_token
        
        config['tanss']['api_token'] = api_token_clean
        config['tanss']['refresh_token'] = refresh_token_clean
        
        with open(config_file, 'w') as f:
            config.write(f)
        
        print(f"✓ Tokens saved to {config_file}")


def load_config(config_file: str = 'config.ini'):
    """Load configuration from file"""
    config = ConfigParser()
    
    if not Path(config_file).exists():
        print(f"⚠ Config file {config_file} not found")
        print(f"Creating from config.ini.example...")
        
        if Path('config.ini.example').exists():
            with open('config.ini.example', 'r') as src:
                with open(config_file, 'w') as dst:
                    dst.write(src.read())
            config.read(config_file)
        else:
            print("✗ config.ini.example not found!")
            return None
    else:
        config.read(config_file)
    
    return config


def main():
    """Interactive token management"""
    import sys
    
    print("TANSS Token Management Utility")
    print("=" * 60)
    
    # Load config
    config = load_config('config.ini')
    
    if config is None:
        print("\n✗ Failed to load configuration")
        return
    
    base_url = config.get('tanss', 'base_url', fallback='https://api.tanss.de')
    
    manager = TokenManager(base_url)
    
    print(f"\nBase URL: {base_url}")
    print("\nOptions:")
    print("1. Login with username/password (from config.ini)")
    print("2. Login with username/password (interactive)")
    print("3. Refresh existing token")
    print("4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == '1':
        # Login using credentials from config.ini
        print("\n--- Login from config.ini ---")
        
        username = config.get('credentials', 'username', fallback='')
        password = config.get('credentials', 'password', fallback='')
        
        if not username or not password:
            print("✗ No credentials found in config.ini")
            print("\nPlease add credentials to config.ini:")
            print("[credentials]")
            print("username = your_username")
            print("password = your_password")
            return
        
        print(f"Username: {username}")
        print("Password: " + "*" * len(password))
        
        try:
            print("\nAuthenticating...")
            result = manager.login(username, password)
            
            # Handle TANSS response format
            if 'apiKey' in result and 'refresh' in result:
                api_key = result['apiKey']
                refresh_token = result['refresh']
                
                print("\n✓ Login successful!")
                print(f"\nEmployee ID: {result.get('employeeId', 'N/A')}")
                print(f"Employee Type: {result.get('employeeType', 'N/A')}")
                print(f"Token expires: {datetime.fromtimestamp(result.get('expire', 0)).strftime('%Y-%m-%d %H:%M:%S') if 'expire' in result else 'Unknown'}")
                print(f"\nAPI Token: {api_key[:50]}...")
                print(f"Refresh Token: {refresh_token[:50]}...")
                
                save = input("\nSave to config.ini? (y/n): ").strip().lower()
                if save == 'y':
                    manager.save_tokens(api_key, refresh_token)
                    
                    # Optionally clear credentials from config for security
                    clear = input("\nClear credentials from config.ini for security? (y/n): ").strip().lower()
                    if clear == 'y':
                        config.set('credentials', 'username', '')
                        config.set('credentials', 'password', '')
                        with open('config.ini', 'w') as f:
                            config.write(f)
                        print("✓ Credentials cleared from config.ini")
                    
                    print("\n✓ Configuration updated!")
                else:
                    print("\nTokens not saved.")
                    print("You can manually add them to config.ini:")
                    print(f"  api_token = {api_key.replace('Bearer ', '')}")
                    print(f"  refresh_token = {refresh_token.replace('Bearer ', '')}")
            else:
                print("\n✗ Unexpected response format")
                print(f"Response: {json.dumps(result, indent=2)}")
                
        except Exception as e:
            print(f"\n✗ Login failed: {e}")
            import traceback
            traceback.print_exc()
    
    elif choice == '2':
        # Interactive login
        print("\n--- Login (Interactive) ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        try:
            print("\nAuthenticating...")
            result = manager.login(username, password)
            
            # Handle TANSS response format
            if 'apiKey' in result and 'refresh' in result:
                api_key = result['apiKey']
                refresh_token = result['refresh']
                
                print("\n✓ Login successful!")
                print(f"\nEmployee ID: {result.get('employeeId', 'N/A')}")
                print(f"Employee Type: {result.get('employeeType', 'N/A')}")
                print(f"Token expires: {datetime.fromtimestamp(result.get('expire', 0)).strftime('%Y-%m-%d %H:%M:%S') if 'expire' in result else 'Unknown'}")
                print(f"\nAPI Token: {api_key[:50]}...")
                print(f"Refresh Token: {refresh_token[:50]}...")
                
                save = input("\nSave to config.ini? (y/n): ").strip().lower()
                if save == 'y':
                    manager.save_tokens(api_key, refresh_token)
                    print("\n✓ Configuration updated!")
                    
                    # Ask if they want to save credentials too
                    save_creds = input("\nSave credentials to config.ini for future logins? (y/n): ").strip().lower()
                    if save_creds == 'y':
                        if 'credentials' not in config:
                            config.add_section('credentials')
                        config.set('credentials', 'username', username)
                        config.set('credentials', 'password', password)
                        with open('config.ini', 'w') as f:
                            config.write(f)
                        print("✓ Credentials saved (remember to secure config.ini)")
                else:
                    print("\nTokens not saved.")
                    print("You can manually add them to config.ini:")
                    print(f"  api_token = {api_key.replace('Bearer ', '')}")
                    print(f"  refresh_token = {refresh_token.replace('Bearer ', '')}")
            else:
                print("\n✗ Unexpected response format")
                print(f"Response: {json.dumps(result, indent=2)}")
                
        except Exception as e:
            print(f"\n✗ Login failed: {e}")
            import traceback
            traceback.print_exc()
    
    elif choice == '3':
        # Refresh token
        print("\n--- Refresh Token ---")
        refresh_token = config.get('tanss', 'refresh_token', fallback='')
        
        if not refresh_token or refresh_token == 'YOUR_REFRESH_TOKEN_HERE':
            refresh_token = input("Enter refresh token: ").strip()
        else:
            print(f"Using refresh token from config: {refresh_token[:50]}...")
        
        # Add 'Bearer ' prefix if not present
        if not refresh_token.startswith('Bearer '):
            refresh_token = f'Bearer {refresh_token}'
        
        try:
            print("\nRefreshing token...")
            result = manager.refresh_token(refresh_token)
            
            # Check if new tokens in response
            if 'apiKey' in result:
                print("\n✓ Token refreshed!")
                print(f"New API Token: {result['apiKey'][:50]}...")
                print(f"New Refresh Token: {result.get('refresh', 'N/A')[:50]}...")
                
                save = input("\nSave to config.ini? (y/n): ").strip().lower()
                if save == 'y':
                    manager.save_tokens(result['apiKey'], result.get('refresh', refresh_token))
                    print("\n✓ Configuration updated!")
            else:
                print("\n✓ Token refresh request sent!")
                print(f"Response: {json.dumps(result, indent=2)}")
                print("\nNote: New tokens may be in response headers or meta section.")
            
        except Exception as e:
            print(f"\n✗ Refresh failed: {e}")
            print("\nYour refresh token may have expired. Please login again (option 1 or 2).")
    
    elif choice == '4':
        print("\nExiting...")
    
    else:
        print("\nInvalid choice!")


if __name__ == '__main__':
    main()
