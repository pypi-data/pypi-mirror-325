import json
import logging
from typing import Dict, List, Any
from contextlib import AsyncExitStack
from dotenv import load_dotenv
import os

from mcp.client.sse import sse_client
from mcp.client.session import ClientSession
from mcp.types import CallToolResult

from .types import Tool, ToolConfig, SecurityScheme, ApiKeySecurityScheme

logger = logging.getLogger(__name__)
load_dotenv()


class Client:
    """Client for managing MCP server connections and tools."""

    def __init__(self, hives: List[str]):
        self.hives = hives
        self.sessions: Dict[str, ClientSession] = {}
        self.exit_stack = AsyncExitStack()
        self.tools: List[Tool] = []
        self._tools_by_name: Dict[str, Tool] = {}

    async def connect(self) -> None:
        """Connect to all configured hives."""
        for server_url in self.hives:
            try:
                sse_transport = await self.exit_stack.enter_async_context(
                    sse_client(url=server_url)
                )
                stdio, write = sse_transport
                session = await self.exit_stack.enter_async_context(
                    ClientSession(stdio, write)
                )
                await session.initialize()
                self.sessions[server_url] = session
                logger.info(f"Connected to hive: {server_url}")
            except Exception as e:
                logger.error(f"Failed to connect to {server_url}: {e}")

        await self.setup_tools()

    async def setup_tools(self) -> List[Tool]:
        """Get and filter tools from all connected hives."""
        self.tools = []
        for server_url, session in self.sessions.items():
            try:
                response = await session.list_tools()
                tool_configs = await self._list_tool_configs(session, server_url)
                tool_configs_by_name = {
                    tool_config.name: tool_config for tool_config in tool_configs
                }
                params_to_exclude = await self._get_params_to_exclude(
                    session, server_url
                )

                filtered_tools = [
                    Tool(
                        name=tool.name,
                        description=tool.description,
                        input_schema=self._filter_tool_params(
                            tool.inputSchema, params_to_exclude
                        ),
                        hive=server_url,
                        security_schemes=[
                            SecurityScheme.from_dict(scheme)
                            for scheme in tool_configs_by_name[
                                tool.name
                            ].security_schemes
                        ],
                        host=tool_configs_by_name[tool.name].host,
                    )
                    for tool in response.tools
                    if tool.name not in {"list_tool_configs", "list_params_to_exclude"}
                ]
                self.tools.extend(filtered_tools)
            except Exception as e:
                logger.error(f"Error getting tools from {server_url}: {e}")

        self._tools_by_name = {tool.name: tool for tool in self.tools}
        return self.tools

    async def call_tool(
        self, tool_name: str, tool_args: Dict[str, Any]
    ) -> CallToolResult:
        """Call a tool with the given arguments."""
        tool = self._tools_by_name.get(tool_name)
        if not tool:
            raise ValueError(f"Tool {tool_name} not found")

        session = self.sessions[tool.hive]
        args = tool_args.copy()

        # Add host and auth information
        args["host__"] = os.environ.get(tool.host.get_env_var(), tool.host.default_url)

        if tool.security_schemes:
            security_scheme = tool.security_schemes[0]
            if isinstance(security_scheme, ApiKeySecurityScheme):
                security_scheme_data = security_scheme.to_dict()
                security_scheme_data["value"] = os.environ.get(
                    security_scheme.env_variable, "xxx"
                )
            security_scheme_data["key"] = security_scheme.name
            args["request_auth__"] = security_scheme_data

        return await session.call_tool(tool_name, args)

    async def cleanup(self) -> None:
        """Clean up all sessions."""
        await self.exit_stack.aclose()

    # Helper methods
    async def _list_tool_configs(
        self, session: ClientSession, server_url: str
    ) -> List[ToolConfig]:
        try:
            result = await session.call_tool("list_tool_configs", {})
            return (
                [ToolConfig(**json.loads(tool.text)) for tool in result.content]
                if result.content
                else []
            )
        except Exception as e:
            logger.warning(f"Could not get tool configs from {server_url}: {e}")
            return []

    async def _get_params_to_exclude(
        self, session: ClientSession, server_url: str
    ) -> List[str]:
        try:
            result = await session.call_tool("list_params_to_exclude", {})
            return [param.text for param in result.content] if result.content else []
        except Exception as e:
            logger.warning(f"Could not get params to exclude from {server_url}: {e}")
            return []

    @staticmethod
    def _filter_tool_params(schema: dict, params_to_exclude: List[str]) -> dict:
        filtered_schema = schema.copy()
        if "properties" in filtered_schema:
            filtered_schema["properties"] = {
                k: v
                for k, v in filtered_schema["properties"].items()
                if k not in params_to_exclude
            }
        return filtered_schema

    @staticmethod
    def _get_host_env_var_name(host_name: str) -> str:
        return f"{host_name.upper()}_SERVER_URL"

    @staticmethod
    def _get_security_env_var_name(host_name: str) -> str:
        return f"{host_name.upper()}_API_KEY"

    def get_required_env_vars(self) -> Dict[str, str]:
        """Get all required environment variables for all tools.

        Returns:
            Dict mapping environment variable names to their descriptions
        """
        env_vars = {}

        # Collect env vars from all tools
        for tool in self.tools:
            tool_env_vars = tool.get_required_env_vars()
            # Update without overwriting existing descriptions
            for var_name, description in tool_env_vars.items():
                if var_name not in env_vars:
                    env_vars[var_name] = description

        return env_vars
