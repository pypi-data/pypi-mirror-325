# Lineup Simulator MCP Server

A Model Context Protocol (MCP) server that provides tools for working with NFL lineup and projection data.

## Features

This MCP server exposes two main tools:

1. `show_lineup`: Display details for a specific lineup by index
   - Input: `index` (integer) - The index of the lineup to display (0-based)
   - Output: String containing the lineup details

2. `search_projections`: Search NFL projections for players by name
   - Input: `search_term` (string) - The player name to search for (case-insensitive)
   - Output: String containing matching player(s) details

## Installation

The server requires Python 3.10 or higher. You can install it directly from TestPyPI using [uv](https://docs.astral.sh/uv/):

```bash
uv pip install --index testpypi mcp_simulator
```

For development setup:

```bash
# Clone the repository
git clone <repository-url>
cd mcp_simulator

# Create and activate environment
uv sync
```

## Usage

### Running with uvx

After installation, you can run the server using the `uvx` command:

```bash
uvx
```

### Claude Desktop Integration

To use the MCP server with Claude Desktop, you need to modify your Claude Desktop configuration file. The file is located at:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following configuration to the `mcpServers` section:

```json
{
  "mcpServers": {
    "lineup-simulator": {
      "command": "uvx",
      "args": []
    }
  }
}
```

Note: Make sure to back up your configuration file before making changes.

### Development Mode

For development and testing:

```bash
cd mcp_simulator
uv sync
uv run uvx
```

## Data Sources

The server expects two CSV files in the project root's `csvs` directory:

- `lineup_pool_5k.csv`: Contains lineup data
- `nfl_projections.csv`: Contains NFL player projections

## Example Usage

Once configured in Claude Desktop, you can use the tools like this:

```
# Show a specific lineup
Tool: show_lineup
Input: {"index": 0}

# Search for a player
Tool: search_projections
Input: {"search_term": "Brady"}
```

The server communicates with Claude Desktop using the MCP protocol over stdio, allowing seamless integration with the Claude AI assistant.

## Project Structure

```
mcp_simulator/
├── README.md
├── pyproject.toml
└── src/
    └── mcp_simulator/
        ├── __init__.py
        └── server.py
```

## Dependencies

- Python >=3.10
- mcp[cli]
- pandas

## Development

The server is built using the MCP Python SDK's FastMCP framework. For more information about MCP development, see the [MCP documentation](https://modelcontextprotocol.io).
