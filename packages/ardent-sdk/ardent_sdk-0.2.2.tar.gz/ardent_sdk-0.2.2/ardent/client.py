import httpx
import time
import hmac
import hashlib
from uuid import uuid4
from typing import Dict, Any, Optional, List
from .exceptions import ArdentAPIError, ArdentAuthError, ArdentValidationError
import json

class ArdentClient:
    def __init__(
        self, 
        public_key: str,
        secret_key: str,
        base_url: str = "https://ardentbackendwebappfinal.azurewebsites.net"
    ):
        if not public_key or not secret_key:
            raise ArdentValidationError("Both public and secret keys are required")
            
        self.public_key = public_key
        self.secret_key = secret_key
        self.base_url = base_url.rstrip('/')
        self.session_id = str(uuid4())
        self._client = httpx.Client(timeout=3000.0)

    def _sign_request(self, method: str, path: str, body: str = "") -> Dict[str, str]:
        timestamp = str(int(time.time()))
        message = f"{timestamp}{method}{path}{body}"
        
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
        return {
            "X-API-Key": self.public_key,
            "X-Signature": signature,
            "X-Timestamp": timestamp,
            "X-Session-ID": self.session_id,
            "Content-Type": "application/json"
        }

    def create_job(self, message: str) -> Dict[str, Any]:
        path = "/v1/jobs/createJob"
        body = {
            "userMessage": message,
        }
        
        try:
            json_body = json.dumps(body, separators=(',', ':'))
            
            headers = self._sign_request(
                method="POST",
                path=path,
                body=json_body
            )
            
            response = self._client.post(
                f"{self.base_url}{path}",
                headers=headers,
                json=body
            )


            
            response.raise_for_status()
            
            if response.status_code == 201:  # Handle 201 Created specifically
                response_data = response.json()
                if not response_data:
                    raise ArdentAPIError("API returned empty response")
                
                # Ensure required fields are present
                required_fields = ['id', 'files_share_name', 'userID']
                if not all(field in response_data for field in required_fields):
                    # Generate an ID if missing
                    if 'id' not in response_data:
                        response_data['id'] = str(uuid4())
                    # Use empty string for missing share name
                    if 'files_share_name' not in response_data:
                        response_data['files_share_name'] = ''
                    # Use provided userID if missing

                        
                return response_data
                
            return response.json()
            
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ArdentAuthError("Invalid API key or signature")
            raise ArdentAPIError(
                f"API request failed: {str(e)}", 
                status_code=e.response.status_code,
                response=e.response
            )
        except json.JSONDecodeError as e:
            raise ArdentAPIError(f"Invalid JSON response from API: {str(e)}")

    def execute_job(
        self, 
        jobID: str, 
        message: str, 
        files_share_name: str, 
        userID: str,
        safe_mode: bool = False
    ) -> Dict[str, Any]:
        """Execute a job with the given parameters."""
        path = "/v1/jobs/APIChat"  # Updated endpoint path
        body = {
            "jobID": jobID,
            "userMessage": message,
            "files_share_name": files_share_name,
            "userID": userID,
            "safeMode": safe_mode
        }
        
        try:
            json_body = json.dumps(body, separators=(',', ':'))
            headers = self._sign_request(
                method="POST",
                path=path,
                body=json_body
            )
            
            response = self._client.post(
                f"{self.base_url}{path}",
                headers=headers,
                json=body
            )
            response.raise_for_status()
            return response.json()
            
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ArdentAuthError("Invalid API key or signature")
            elif e.response.status_code == 402:
                raise ArdentAPIError("Out of credits")
            elif e.response.status_code == 403:
                raise ArdentAuthError("Missing required scope: job:execute")
            raise ArdentAPIError(
                f"API request failed: {str(e)}", 
                status_code=e.response.status_code,
                response=e.response
            )

    def create_and_execute_job(
        self, 
        message: str,
        safe_mode: bool = False
    ) -> Dict[str, Any]:
        """Create and execute a job in one operation."""
        # First create the job
        path = "/v1/jobs/createJob"
        create_body = {
            "userMessage": message,
        }
        
        try:
            # Create job
            json_body = json.dumps(create_body, separators=(',', ':'))
            headers = self._sign_request(
                method="POST",
                path=path,
                body=json_body
            )
            
            create_response = self._client.post(
                f"{self.base_url}{path}",
                headers=headers,
                json=create_body
            )
            create_response.raise_for_status()
            job = create_response.json()
            
            if not job:
                raise ArdentAPIError("Job creation failed - empty response")
                
            # Then execute the job
            execute_path = "/v1/jobs/APIChat"
            execute_body = {
                "jobID": job["id"],
                "userMessage": message,
                "files_share_name": job["files_share_name"],
                "safeMode": safe_mode
            }
            
            json_body = json.dumps(execute_body, separators=(',', ':'))
            headers = self._sign_request(
                method="POST",
                path=execute_path,
                body=json_body
            )
            
            execute_response = self._client.post(
                f"{self.base_url}{execute_path}",
                headers=headers,
                json=execute_body
            )
            execute_response.raise_for_status()
            return execute_response.json()
            
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ArdentAuthError("Invalid API key or signature")
            elif e.response.status_code == 402:
                raise ArdentAPIError("Out of credits")
            elif e.response.status_code == 403:
                raise ArdentAuthError("Missing required scope: job:execute")
            raise ArdentAPIError(
                f"API request failed: {str(e)}", 
                status_code=e.response.status_code,
                response=e.response
            )
        
    def _validate_mongodb_structure(self, databases: List[Dict]) -> None:
        """Validate MongoDB databases and collections structure"""
        if not isinstance(databases, list):
            raise ArdentValidationError("'databases' must be a list")
        
        for db in databases:
            # Validate database structure
            if not isinstance(db, dict):
                raise ArdentValidationError("Each database must be a dictionary")
            
            if 'name' not in db:
                raise ArdentValidationError("Each database must have a 'name' field")
            if not isinstance(db['name'], str):
                raise ArdentValidationError("Database name must be a string")
            
            if 'collections' not in db:
                raise ArdentValidationError("Each database must have a 'collections' field")
            if not isinstance(db['collections'], list):
                raise ArdentValidationError("'collections' must be a list")
            
            # Validate collections structure
            for collection in db['collections']:
                if not isinstance(collection, dict):
                    raise ArdentValidationError("Each collection must be a dictionary")
                if 'name' not in collection:
                    raise ArdentValidationError("Each collection must have a 'name' field")
                if not isinstance(collection['name'], str):
                    raise ArdentValidationError("Collection name must be a string")

    def set_config(
        self,
        config_type: str,
        id: Optional[str] = None,
        **config_params: Any
    ) -> Dict[str, Any]:
        """
        Set configuration for various data sources.
        
        Args:
            config_type: The type of configuration ('mongodb', 'postgreSQL', etc.)
            id: Optional unique identifier for the configuration. If not provided, one will be generated.
            **config_params: Configuration parameters specific to the type
        """
        # Generate UUID if not provided
        if id is None:
            id = str(uuid4())

        # Combined mapping of config types to their endpoints and required parameters
        config_types = {
            "mongodb": {
                "endpoint": "/v1/configs/setMDBConfig",
                "required_params": ["connection_string", "databases"],
                "structure": {
                    "connection_string": str,
                    "databases": list,  # List of {name: str, collections: [{name: str}]}
                }
            },
            "postgreSQL": {
                "endpoint": "/v1/configs/setpostgreSQLConfig",
                "required_params": ["databases", "Hostname", "Port", "username", "password"],
                "structure": {
                    "Hostname": str,
                    "Port": str,
                    "username": str,
                    "password": str,
                    "databases": list,  # List of {name: str}
                }
            },
            "supabase": {
                "endpoint": "/v1/configs/setSupabaseConfig",
                "required_params": ["project_url", "api_key", "databases"],
                "structure": {
                    "project_url": str,
                    "api_key": str,
                    "databases": list,  # List of {name: str, tables: [{name: str}]}
                }
            },
            "airflow": {
                "endpoint": "/v1/configs/setAirflowConfig",
                "required_params": ["github_token", "repo", "dag_path", "host", "username", "password"],
                "structure": {
                    "github_token": str,
                    "repo": str,
                    "dag_path": str,
                    "host": str,
                    "username": str,
                    "password": str,
                }
            },
            "azureSQLServer": {
                "endpoint": "/v1/configs/setAzureSQLConfig",
                "required_params": ["server", "username", "password", "version", "databases"],
                "structure": {
                    "server": str,
                    "username": str,
                    "password": str,
                    "version": str,
                    "databases": list,  # List of {name: str}
                }
            },
            "snowflake": {
                "endpoint": "/v1/configs/setSnowflakeConfig",
                "required_params": ["account", "user", "password", "warehouse", "databases"],
                "structure": {
                    "account": str,
                    "user": str,
                    "password": str,
                    "warehouse": str,
                    "databases": list,  # List of {name: str}
                }
            },
            "databricks": {
                "endpoint": "/v1/configs/setDatabricksConfig",
                "required_params": ["server_hostname", "http_path", "access_token", "catalogs"],
                "structure": {
                    "server_hostname": str,
                    "http_path": str,
                    "access_token": str,
                    "catalogs": list,  # List of {name: str, databases: [{name: str, tables: [{name: str}]}]}
                }
            },
            "mysql": {
                "endpoint": "/v1/configs/setMySQLConfig",
                "required_params": ["host", "port", "username", "password", "databases"],
                "structure": {
                    "host": str,
                    "port": str,
                    "username": str,
                    "password": str,
                    "databases": list,  # List of {name: str}
                }
            },
            "databricksJobs": {
                "endpoint": "/v1/configs/setDatabricksJobsConfig",
                "required_params": ["workspace_url", "access_token", "github_token", "repo", "repo_path"],
                "structure": {
                    "workspace_url": str,
                    "access_token": str,
                    "github_token": str,
                    "repo": str,
                    "repo_path": str,
                }
            },
            "tigerbeetle": {
                "endpoint": "/v1/configs/setTigerBeetleConfig",
                "required_params": ["cluster_id", "replica_addresses"],
                "structure": {
                    "cluster_id": str,
                    "replica_addresses": list,  # List of strings
                }
            }
        }

        # Validate config type
        if config_type not in config_types:
            raise ArdentValidationError(f"Invalid configuration type: {config_type}")
        
        config_info = config_types[config_type]
        path = config_info["endpoint"]
        
        # Validate required parameters
        missing_params = [param for param in config_info["required_params"] 
                         if param not in config_params]
        if missing_params:
            raise ArdentValidationError(
                f"Missing required parameters for {config_type}: {', '.join(missing_params)}"
            )
        
        # Validate parameter types against structure
        for param, expected_type in config_info["structure"].items():
            if param in config_params:
                value = config_params[param]
                if not isinstance(value, expected_type):
                    raise ArdentValidationError(
                        f"Invalid type for parameter '{param}' in {config_type} config. "
                        f"Expected {expected_type.__name__}, got {type(value).__name__}"
                    )

            # Additional structure validation for MongoDB databases
            if config_type == "mongodb" and param == "databases":
                self._validate_mongodb_structure(value)

        # Construct request body
        body = {
            "Config": {
                "type": config_type,
                "id": id,
                **config_params
            }
        }
        
        try:
            json_body = json.dumps(body, separators=(',', ':'))
            headers = self._sign_request(
                method="POST",
                path=path,
                body=json_body
            )
            
            response = self._client.post(
                f"{self.base_url}{path}",
                headers=headers,
                json=body
            )
            response.raise_for_status()
            return response.json()
            
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ArdentAuthError("Invalid API key or signature")
            raise ArdentAPIError(
                f"API request failed: {str(e)}", 
                status_code=e.response.status_code,
                response=e.response
            )

    def delete_config(self, config_id: str) -> Dict[str, Any]:
        """
        Delete a configuration by its ID.
        
        Args:
            config_id: The ID of the configuration to delete
        """
        path = "/v1/configs/deleteConfig"
        body = {
            "id": config_id
        }
        
        try:
            json_body = json.dumps(body, separators=(',', ':'))
            headers = self._sign_request(
                method="DELETE",
                path=path,
                body=json_body
            )
            
            response = self._client.request(
                "DELETE",
                f"{self.base_url}{path}",
                headers=headers,
                json=body
            )
            response.raise_for_status()
            return response.json()
            
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ArdentAuthError("Invalid API key or signature")
            elif e.response.status_code == 403:
                raise ArdentAuthError("Missing required scope: config:write")
            elif e.response.status_code == 404:
                raise ArdentAPIError("Configuration not found")
            raise ArdentAPIError(
                f"API request failed: {str(e)}", 
                status_code=e.response.status_code,
                response=e.response
            )

    def close(self):
        """Close the underlying HTTP client and clean up resources."""
        if hasattr(self, '_client'):
            self._client.close()