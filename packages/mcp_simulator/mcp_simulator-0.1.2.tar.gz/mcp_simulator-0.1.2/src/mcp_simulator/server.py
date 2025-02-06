#!/usr/bin/env python3
import os
import sys
import pandas as pd
import logging
from pathlib import Path
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

# reconfigure UnicodeEncodeError prone default (i.e. windows-1252) to utf-8
if sys.platform == "win32" and os.environ.get('PYTHONIOENCODING') is None:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

logger = logging.getLogger('mcp_lineup_simulator')
logger.info("Starting MCP Lineup Simulator Server")

def create_server():
    # Create a named server
    server = Server("lineup-simulator")

    # Helper function
    def load_csv(filepath: str) -> pd.DataFrame:
        """Load a CSV file into a pandas DataFrame"""
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise ValueError(f"Error loading {filepath}: {e}")

    # Initialize paths
    CURRENT_DIR = Path(__file__).parent.parent.parent.parent
    LINEUP_CSV = CURRENT_DIR / "csvs" / "lineup_pool_5k.csv"
    PROJECTIONS_CSV = CURRENT_DIR / "csvs" / "nfl_projections.csv"

    @server.list_tools()
    async def handle_list_tools() -> list[types.Tool]:
        """List available tools"""
        return [
            types.Tool(
                name="show_lineup",
                description="Display details for the lineup at the given index",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "index": {"type": "integer", "description": "The index of the lineup to display (0-based)"},
                    },
                    "required": ["index"],
                },
            ),
            types.Tool(
                name="search_projections",
                description="Search NFL projections for a player by name",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "search_term": {"type": "string", "description": "The player name to search for (case-insensitive)"},
                    },
                    "required": ["search_term"],
                },
            ),
        ]

    @server.call_tool()
    async def handle_call_tool(
        name: str, arguments: dict[str, any] | None
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        """Handle tool execution requests"""
        try:
            if not arguments:
                raise ValueError("Missing arguments")

            if name == "show_lineup":
                index = arguments["index"]
                df = load_csv(LINEUP_CSV)
                if index < 0 or index >= len(df):
                    raise ValueError(f"Lineup index {index} out of range (0-{len(df)-1})")
                
                row = df.iloc[index]
                return [types.TextContent(type="text", text=str(row))]

            elif name == "search_projections":
                search_term = arguments["search_term"]
                df = load_csv(PROJECTIONS_CSV)
                results = df[df['Name'].str.contains(search_term, case=False, na=False)]
                
                if results.empty:
                    return [types.TextContent(type="text", text="No matching players found.")]
                
                return [types.TextContent(type="text", text=f"Found {len(results)} matching player(s):\n{results.head().to_string()}")]

            else:
                raise ValueError(f"Unknown tool: {name}")

        except Exception as e:
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]

    return server

async def main():
    """Main entry point for the server."""
    server = create_server()
    
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        logger.info("Server running with stdio transport")
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="lineup-simulator",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
