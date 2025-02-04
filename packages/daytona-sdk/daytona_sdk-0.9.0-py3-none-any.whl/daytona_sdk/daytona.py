"""
Daytona SDK for Python

This module provides the main entry point for interacting with Daytona Server API.
"""

import uuid
import json
from typing import Optional, Literal, Dict, Any, List
from dataclasses import dataclass
from environs import Env
import time
from daytona_api_client import (
    Configuration,
    WorkspaceApi,
    ToolboxApi,
    ApiClient,
    CreateWorkspace,
    SessionExecuteRequest,
    SessionExecuteResponse
)

from .code_toolbox.workspace_python_code_toolbox import WorkspacePythonCodeToolbox
from .code_toolbox.workspace_ts_code_toolbox import WorkspaceTsCodeToolbox
from .workspace import Workspace


# Type definitions
CodeLanguage = Literal["python", "javascript", "typescript"]


@dataclass
class DaytonaConfig:
    """Configuration options for initializing the Daytona client.
    
    Args:
        api_key: API key for authentication with Daytona server
        server_url: URL of the Daytona server
        target: Target environment for workspaces
    """
    api_key: str
    server_url: str
    target: str

@dataclass
class WorkspaceResources:
    """Resources configuration for workspace"""
    cpu: Optional[int] = None
    memory: Optional[int] = None  # in MB
    disk: Optional[int] = None    # in GB
    gpu: Optional[int] = None

@dataclass
class CreateWorkspaceParams:
    """Parameters for creating a new workspace."""
    language: CodeLanguage
    id: Optional[str] = None
    name: Optional[str] = None
    image: Optional[str] = None
    os_user: Optional[str] = None
    env_vars: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None
    public: Optional[bool] = None
    target: Optional[str] = None
    resources: Optional[WorkspaceResources] = None


class Daytona:
    def __init__(self, config: Optional[DaytonaConfig] = None):
        """
        Initialize Daytona instance with optional configuration.
        If no config is provided, reads from environment variables using environs.

        Args:
            config: Optional DaytonaConfig object containing api_key, server_url, and target

        Raises:
            ValueError: If API key or Server URL is not provided either through config or environment variables
        """
        if config is None:
            # Initialize env - it automatically reads from .env and .env.local
            env = Env()
            env.read_env()  # reads .env
            # reads .env.local and overrides values
            env.read_env(".env.local", override=True)

            self.api_key = env.str("DAYTONA_API_KEY")
            self.server_url = env.str("DAYTONA_SERVER_URL")
            self.target = env.str("DAYTONA_TARGET", "local")
        else:
            self.api_key = config.api_key
            self.server_url = config.server_url
            self.target = config.target

        if not self.api_key:
            raise ValueError("API key is required")

        if not self.server_url:
            raise ValueError("Server URL is required")

        # Create API configuration without api_key
        configuration = Configuration(host=self.server_url)
        api_client = ApiClient(configuration)
        api_client.default_headers["Authorization"] = f"Bearer {self.api_key}"

        # Initialize API clients with the api_client instance
        self.workspace_api = WorkspaceApi(api_client)
        self.toolbox_api = ToolboxApi(api_client)

    def create(self, params: Optional[CreateWorkspaceParams] = None) -> Workspace:
        """Creates a new workspace and waits for it to start.
        
        Args:
            params: Optional parameters for workspace creation. If not provided, 
                   defaults to Python language.
            
        Returns:
            The created workspace instance
        """
        # If no params provided, create default params for Python
        if params is None:
            params = CreateWorkspaceParams(language="python")

        workspace_id = params.id if params.id else f"sandbox-{str(uuid.uuid4())[:8]}"
        code_toolbox = self._get_code_toolbox(params)

        try:
            # Create workspace using dictionary
            workspace_data = CreateWorkspace(
                id=workspace_id,
                name=params.name if params.name else workspace_id,
                image=params.image,
                user=params.os_user if params.os_user else "daytona",
                env_vars=params.env_vars if params.env_vars else {},
                labels=params.labels,
                public=params.public,
                target=params.target if params.target else self.target,
            )

            if params.resources:
                workspace_data.cpu = params.resources.cpu
                workspace_data.memory = params.resources.memory
                workspace_data.disk = params.resources.disk
                workspace_data.gpu = params.resources.gpu

            response = self.workspace_api.create_workspace(create_workspace=workspace_data)
            workspace = Workspace(
                workspace_id,
                response,
                self.workspace_api,
                self.toolbox_api,
                code_toolbox
            )

            # Wait for workspace to start
            try:
                workspace.wait_for_workspace_start()
            finally:
                # If not Daytona SaaS, we don't need to handle pulling image state
                pass

            return workspace

        except Exception as e:
            try:
                self.workspace_api.remove_workspace(workspace_id=workspace_id)
            except:
                pass
            raise Exception(f"Failed to create workspace: {str(e)}") from e

    def _get_code_toolbox(self, params: Optional[CreateWorkspaceParams] = None):
        """Helper method to get the appropriate code toolbox
        
        Args:
            params: Optional workspace parameters. If not provided, defaults to Python toolbox.
            
        Returns:
            The appropriate code toolbox instance
        """
        if not params:
            return WorkspacePythonCodeToolbox()

        match params.language:
            case "javascript" | "typescript":
                return WorkspaceTsCodeToolbox()
            case "python":
                return WorkspacePythonCodeToolbox()
            case _:
                raise ValueError(f"Unsupported language: {params.language}")
            
    def remove(self, workspace: Workspace) -> None:
        """Removes a workspace.
        
        Args:
            workspace: The workspace to remove
        """
        return self.workspace_api.delete_workspace(workspace_id=workspace.id, force=True)

    def get_current_workspace(self, workspace_id: str) -> Workspace:
        """
        Get a workspace by its ID.

        Args:
            workspace_id: The ID of the workspace to retrieve

        Returns:
            Workspace: The workspace instance

        Raises:
            ValueError: If workspace_id is not provided
        """
        if not workspace_id:
            raise ValueError("workspace_id is required")

        # Get the workspace instance
        workspace_instance = self.workspace_api.get_workspace(workspace_id=workspace_id)

        # Create and return workspace with Python code toolbox as default
        code_toolbox = WorkspacePythonCodeToolbox()
        return Workspace(
            workspace_id,
            workspace_instance,
            self.workspace_api,
            self.toolbox_api,
            code_toolbox
        )
    
    def list(self) -> List[Workspace]:
        """List all workspaces."""
        workspaces = self.workspace_api.list_workspaces()
        return [
            Workspace(
                workspace.id,
                workspace,
                self.workspace_api,
                self.toolbox_api,
                self._get_code_toolbox(
                    CreateWorkspaceParams(
                        language=self._validate_language_label(workspace.labels.get("code-toolbox-language"))
                    )
                )
            )
            for workspace in workspaces
        ]

    def _validate_language_label(self, language: Optional[str]) -> CodeLanguage:
        """Validate the code-toolbox-language label.
        
        Args:
            language: The language label to validate
            
        Returns:
            CodeLanguage: The validated language, defaults to "python" if None
            
        Raises:
            ValueError: If the language is not supported
        """
        if not language:
            return "python"
        
        if language not in ["python", "javascript", "typescript"]:
            raise ValueError(f"Invalid code-toolbox-language: {language}")
            
        return language  # type: ignore
    
    # def resize(self, workspace: Workspace, resources: WorkspaceResources) -> None:
    #     """Resizes a workspace.
        
    #     Args:
    #         workspace: The workspace to resize
    #         resources: The new resources to set
    #     """
    #     self.workspace_api. (workspace_id=workspace.id, resources=resources)
    
    def start(self, workspace: Workspace) -> None:
        """Starts a workspace and waits for it to be ready.
        
        Args:
            workspace: The workspace to start
        """
        workspace.start()
        workspace.wait_for_workspace_start()
    
    def stop(self, workspace: Workspace) -> None:
        """Stops a workspace and waits for it to be stopped.
        
        Args:
            workspace: The workspace to stop
        """
        workspace.stop()
        workspace.wait_for_workspace_stop()

# Export these at module level
__all__ = [
    "Daytona",
    "DaytonaConfig",
    "CreateWorkspaceParams",
    "CodeLanguage",
    "Workspace",
    "SessionExecuteRequest",
    "SessionExecuteResponse"
]
