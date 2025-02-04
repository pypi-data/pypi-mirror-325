from dataclasses import dataclass
from typing import Dict, List, Any
from abc import ABC, abstractmethod


@dataclass
class Host:
    name: str
    default_url: str

    def get_env_var(self) -> str:
        return f"{self.name.upper()}_URL"


@dataclass
class SecurityScheme(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, json_data) -> "SecurityScheme":
        if json_data.get("type") == "apiKey":
            return ApiKeySecurityScheme.from_dict(json_data)
        raise ValueError(f"Unsupported security scheme type: {json_data.get('type')}")

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass


@dataclass
class ApiKeySecurityScheme(SecurityScheme):
    id: str
    type: str
    name: str
    in_field: str
    env_variable: str

    @classmethod
    def from_dict(cls, json_data) -> "ApiKeySecurityScheme":
        data = json_data.copy()
        data["type"] = "apiKey"
        data["in_field"] = data["in"]
        data["env_variable"] = data["envVariable"]
        del data["in"]
        del data["envVariable"]
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "in": self.in_field,
        }


@dataclass
class Tool:
    name: str
    description: str
    input_schema: dict
    hive: str
    security_schemes: List[SecurityScheme]
    host: Host

    def get_required_env_vars(self) -> Dict[str, str]:
        """Get all required environment variables for this tool.

        Returns:
            Dict mapping environment variable names to their descriptions
        """
        env_vars = {}

        env_vars[self.host.get_env_var()] = f"Server URL for {self.host.name}"

        # Add security scheme environment variables
        for scheme in self.security_schemes:
            if scheme.type == "apiKey":
                env_vars[scheme.env_variable] = f"API key for {self.host.name}"

        return env_vars

    def to_llm_tool(self):
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.input_schema,
        }


@dataclass
class ToolConfig:
    id: str
    name: str
    security_schemes: List[Dict[str, Any]]
    host: Host

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.name = kwargs["name"]
        self.security_schemes = kwargs["security_schemes"]
        self.host = Host(**kwargs["host"])
