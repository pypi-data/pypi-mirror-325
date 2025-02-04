# MCP Hive Python SDK 🐝

MCP Hive is your hub for all LLM tools, providing a unified interface to connect with and utilize various AI tools and services. This Python SDK makes it easy to create intelligent agents that can interact with multiple tools through natural language.

## 🌟 Features

- **Multi-Hive Support**: Connect to multiple MCP hives simultaneously
- **Automatic Tool Discovery**: Dynamically discover and configure available tools
- **Rich Console Interface**: Beautiful CLI interface with real-time updates
- **Secure Credentials**: Safe handling of API keys and authentication
- **Claude Integration**: Built-in support for Anthropic's Claude LLM
- **Extensible**: Easy to add new tools and capabilities

## 🚀 Installation

```bash
pip install mcp-hive
```

## 🔧 Quick Start

```python
from mcp_hive import Agent, Client

client = Client(hives=["http://mcp-hive-alb-tmp1-abc-294122034.us-east-1.elb.amazonaws.com/sse"])
agent = Agent(client=client, mode="cli", model="claude-3-5-sonnet-20240620")
agent.configure_behavior("You are a helpful assistant that can answer questions and help with tasks")
asyncio.run(agent.run())
```

## 📚 Documentation

For more detailed information, including advanced features and best practices, please refer to the [MCP Hive Documentation](https://docs.mcp-hive.com).

## 🤝 Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## 📄 License

This project is open-sourced under the MIT License - see the [LICENSE](LICENSE) file for details.
