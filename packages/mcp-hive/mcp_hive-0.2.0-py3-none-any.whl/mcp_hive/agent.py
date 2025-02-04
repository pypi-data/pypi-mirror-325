import logging
from typing import List, Optional, Dict
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.control import Control
from rich.table import Table
import json
import os
from dotenv import load_dotenv

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import (
    HumanMessage,
    BaseMessage,
    SystemMessage,
    ToolMessage,
)
from langchain_anthropic import ChatAnthropic

from .client import Client

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Agent:
    """Agent for interacting with MCP tools using LLMs."""

    def __init__(
        self,
        client: Client,
        mode: str = "cli",
        model: str = "claude-3-5-sonnet-20240620",
        system_prompt: Optional[str] = None,
    ):
        """Initialize the Agent.

        Args:
            client: MCP Hive Client instance
            mode: Operation mode ('cli' or 'server')
            model: LLM model to use
            system_prompt: Custom system prompt
        """
        self.client = client
        self.mode = mode
        self.model_name = model
        self.console = Console()

        # Load environment variables
        load_dotenv()

        # Initialize LLM
        self.llm: BaseChatModel = ChatAnthropic(
            model=self.model_name,
            temperature=0.2,
            max_tokens=8192,
        )

        # Initialize chat history with system prompt
        self.system_prompt = system_prompt or (
            "You are an expert assistant. Your goal is to help the user with their query."
        )
        self.chat_history: List[BaseMessage] = [
            SystemMessage(content=self.system_prompt)
        ]

    def _validate_environment(self) -> bool:
        """Validate all required environment variables are set.

        Returns:
            bool: True if all required variables are set, False otherwise
        """
        missing_vars: Dict[str, str] = {}

        # Check Anthropic API key (LLM-specific requirement)
        if not os.getenv("ANTHROPIC_API_KEY"):
            missing_vars["ANTHROPIC_API_KEY"] = "Required for Claude LLM access"

        # Get required variables from client (tool-specific requirements)
        client_env_vars = self.client.get_required_env_vars()
        for var_name, description in client_env_vars.items():
            if not os.getenv(var_name):
                missing_vars[var_name] = description

        if missing_vars:
            self._print_missing_env_vars(missing_vars)
            return False
        return True

    def _print_missing_env_vars(self, missing_vars: Dict[str, str]) -> None:
        """Print a formatted message about missing environment variables.

        Args:
            missing_vars: Dictionary of missing variable names and their descriptions
        """
        self.console.print("\n[bold red]⚠️  Missing Required Environment Variables[/]\n")

        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Variable Name")
        table.add_column("Description")

        for var_name, description in missing_vars.items():
            table.add_row(f"[yellow]{var_name}[/]", description)

        self.console.print(table)

        self.console.print(
            "\n[bold green]Please create or update your .env file with the following format:[/]\n"
        )

        env_example = "\n".join(
            f"{var_name}=your_{var_name.lower()}_here" for var_name in missing_vars
        )

        self.console.print(
            Panel(
                env_example,
                title="[bold blue].env file[/]",
                border_style="blue",
                padding=(1, 2),
            )
        )

        self.console.print(
            "\n[italic]Make sure to keep your .env file secure and never commit it to version control.[/]\n"
        )

    def configure_behavior(self, system_prompt: str) -> None:
        """Update the agent's system prompt.

        Args:
            system_prompt: New system prompt for the agent
        """
        self.system_prompt = system_prompt
        self.chat_history = [SystemMessage(content=system_prompt)]

    @staticmethod
    def _print_banner():
        """Print the MCP HIVE banner."""
        banner = """
\033[3m\033[38;2;66;139;202m\
███╗   ███╗ ██████╗██████╗     ██╗  ██╗██╗██╗   ██╗███████╗
████╗ ████║██╔════╝██╔══██╗    ██║  ██║██║██║   ██║██╔════╝
██╔████╔██║██║     ██████╔╝    ███████║██║██║   ██║█████╗  
██║╚██╔╝██║██║     ██╔═══╝     ██╔══██║██║╚██╗ ██╔╝██╔══╝  
██║ ╚═╝ ██║╚██████╗██║         ██║  ██║██║ ╚████╔╝ ███████╗
╚═╝     ╚═╝ ╚═════╝╚═╝         ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝\033[0m
                                                            
\033[3m\033[38;2;114;159;207m        🐝 The hub for all your LLM tools 🐝\033[0m
        """
        print(banner)

    async def process_query(self, query: str) -> None:
        """Process a user query using LLM and available tools.

        Args:
            query: User's input query
        """
        self.chat_history.append(HumanMessage(content=query))

        # Create a Live display context for real-time updates
        with Live("", auto_refresh=True, console=self.console) as live:
            complete_response = []
            while True:
                if len(complete_response) == 0:
                    complete_response.append("[dim]Thinking...[/]")
                else:
                    complete_response.append("[dim]Processing tool results...[/]")

                panel = Panel(
                    "\n".join(complete_response),
                    title="[bold purple]🤖 Assistant[/]",
                    border_style="purple",
                    padding=(1, 2),
                )
                live.update(panel)

                # Get LLM response
                ai_msg = await self.llm.ainvoke(self.chat_history)
                self.chat_history.append(ai_msg)

                # Handle regular message content
                if ai_msg.content:
                    content = (
                        ai_msg.content[0].get("text", "")
                        if isinstance(ai_msg.content, list)
                        else ai_msg.content
                    )
                    complete_response[-1] = content

                # Process tool calls
                for tool_call in ai_msg.tool_calls:
                    tool_args = json.dumps(tool_call["args"], indent=2)

                    # Show tool call progress
                    tool_section = (
                        f"\n🔧 [yellow]Tool:[/] {tool_call['name']}\n"
                        f"[dim]Arguments:[/]\n```\n{tool_args}\n```\n"
                        f"[dim]Running tool [green]{tool_call['name']}...[/]"
                    )
                    complete_response.append(tool_section)
                    live.update(
                        Panel(
                            "\n".join(complete_response),
                            title="[bold purple]🤖 Assistant[/]",
                            border_style="purple",
                            padding=(1, 2),
                        )
                    )

                    # Execute tool call
                    try:
                        result = await self.client.call_tool(
                            tool_call["name"], tool_call["args"]
                        )
                        logger.info(f"Tool call result: {result}")
                        tool_msg = ToolMessage(
                            content=result.content,
                            name=tool_call["name"],
                            tool_call_id=tool_call["id"],
                        )
                        success = not (
                            result.content[0].type == "text"
                            and result.content[0].text.startswith(
                                "Error executing tool"
                            )
                        )
                    except Exception as e:
                        logger.error(f"Error calling tool {tool_call['name']}: {e}")
                        tool_msg = ToolMessage(
                            content=f"Error calling tool {tool_call['name']}: {str(e)}",
                            name=tool_call["name"],
                            tool_call_id=tool_call["id"],
                        )
                        success = False

                    self.chat_history.append(tool_msg)

                    # Update tool call status
                    status_message = (
                        "[green]✓ Succeeded[/]" if success else "[red]✗ Failed[/]"
                    )
                    tool_section = (
                        f"\n🔧 [yellow]Tool:[/] {tool_call['name']}\n"
                        f"[dim]Arguments:[/]\n```\n{tool_args}\n```\n"
                        f"{status_message}"
                    )
                    complete_response[-1] = tool_section
                    live.update(
                        Panel(
                            "\n".join(complete_response),
                            title="[bold purple]🤖 Assistant[/]",
                            border_style="purple",
                            padding=(1, 2),
                        )
                    )

                if len(ai_msg.tool_calls) == 0:
                    # If no tool calls, display message and break
                    live.update(
                        Panel(
                            "\n".join(complete_response),
                            title="[bold purple]🤖 Assistant[/]",
                            border_style="purple",
                            padding=(1, 2),
                        )
                    )
                    break

    async def cli_chat_loop(self) -> None:
        """Run an interactive CLI chat loop."""
        self._print_banner()

        self.console.print(
            Panel(
                "[bold green]Welcome to the Interactive Chat![/]\n"
                "[italic]Type 'exit' or 'quit' to end the conversation[/]",
                title="[bold blue]Chat Started[/]",
                border_style="blue",
            )
        )

        while True:
            try:
                query = self.console.input("\n[bold blue]You 💭:[/] ").strip()
                if query.lower() in ["quit", "exit"]:
                    self.console.print("\n[bold red]Goodbye! 👋[/]")
                    break

                # Move cursor up and remove input prompt
                self.console.print(Control.move(0, -1), end="")

                # Display user message
                self.console.print(
                    Panel(
                        query,
                        title="[bold blue]You[/]",
                        border_style="blue",
                        padding=(1, 2),
                    )
                )

                await self.process_query(query)
            except Exception as e:
                logger.error(f"Error in chat loop: {e}")
                self.console.print(f"[bold red]Error:[/] {str(e)}")

    async def run(self) -> None:
        """Run the agent in the specified mode."""
        try:
            # Connect to hives and set up tools only if validation passes
            await self.client.connect()

            # Validate environment variables first
            if not self._validate_environment():
                return

            # Bind tools to LLM
            llm_tools = [tool.to_llm_tool() for tool in self.client.tools]
            self.llm = self.llm.bind_tools(llm_tools)

            if self.mode == "cli":
                await self.cli_chat_loop()
            elif self.mode == "server":
                raise NotImplementedError("Server mode not yet implemented")
            else:
                raise ValueError(f"Unknown mode: {self.mode}")
        finally:
            await self.client.cleanup()


def create_agent(
    hives: List[str],
    mode: str = "cli",
    model: str = "claude-3-5-sonnet-20240620",
    system_prompt: Optional[str] = None,
) -> Agent:
    """Create a new MCP Agent with the specified configuration.

    Args:
        hives: List of MCP hive URLs
        mode: Operation mode ('cli' or 'server')
        model: LLM model to use
        system_prompt: Custom system prompt

    Returns:
        Configured Agent instance
    """
    client = Client(hives=hives)
    return Agent(
        client=client,
        mode=mode,
        model=model,
        system_prompt=system_prompt,
    )
