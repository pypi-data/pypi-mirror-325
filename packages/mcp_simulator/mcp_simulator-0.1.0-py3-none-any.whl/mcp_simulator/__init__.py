"""MCP server for lineup and projection simulation tools."""

import asyncio
from . import server

def main():
    """Main entry point for the package."""
    asyncio.run(server.main())

# Expose important items at package level
__all__ = ["main", "server"]
