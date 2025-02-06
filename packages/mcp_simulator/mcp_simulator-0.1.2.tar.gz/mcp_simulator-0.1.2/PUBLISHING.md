# Publishing Guide

This document outlines the process for publishing the MCP simulator package to both TestPyPI and PyPI.

## Environment Setup

The package uses separate environment files for test and production publishing:

- `.env.test` - Contains TestPyPI credentials
- `.env` - Contains production PyPI credentials

Example environment file structure:
```
UV_PUBLISH_TOKEN=your-token-here
```

## Building the Package

Build the distribution files:

```bash
uv build --no-sources
```

This will create distribution files in the `dist/` directory.

## Publishing

Note: Publishing commands are shown in bash/zsh syntax for Unix-like systems (macOS/Linux).

### To TestPyPI

For testing purposes, publish to TestPyPI using:

```bash
# Unix/Linux/macOS
export UV_PUBLISH_TOKEN=$(cat .env.test | grep UV_PUBLISH_TOKEN | cut -d '=' -f2)
uv publish --publish-url https://test.pypi.org/legacy/ dist/*

# Windows PowerShell
$env:UV_PUBLISH_TOKEN = (Get-Content .env.test | Select-String UV_PUBLISH_TOKEN).Line.Split('=')[1]
uv publish --publish-url https://test.pypi.org/legacy/ dist/*
```

Verify the test installation:
```bash
uv pip install --index https://test.pypi.org/simple/ mcp_simulator
```

### To PyPI

Once testing is complete, publish to production PyPI:

```bash
# Unix/Linux/macOS
export UV_PUBLISH_TOKEN=$(cat .env | grep UV_PUBLISH_TOKEN | cut -d '=' -f2)
uv publish --publish-url https://upload.pypi.org/legacy/ dist/*

# Windows PowerShell
$env:UV_PUBLISH_TOKEN = (Get-Content .env | Select-String UV_PUBLISH_TOKEN).Line.Split('=')[1]
uv publish --publish-url https://upload.pypi.org/legacy/ dist/*
```

## Running the Server

### On Windows

To run the server with environment variables:

```powershell
# PowerShell
$env:UV_ENV_FILE=".env"
uv run uvx

# Command Prompt
set UV_ENV_FILE=.env
uv run uvx
```

For development, you might want to use the test environment:
```powershell
$env:UV_ENV_FILE=".env.test"
uv run uvx
```

## Version Management

1. Update the version in `pyproject.toml` before publishing
2. Build and test with TestPyPI first
3. Once verified, either:
   - Create a new GitHub release to trigger automatic publishing to PyPI
   - Or manually publish to production PyPI using the commands above

## Automated Publishing

The package uses GitHub Actions for automated publishing to PyPI. When you create and publish a new release on GitHub, it will:

1. Build the package using uv
2. Publish to PyPI using trusted publishing (no tokens needed)

To use this:

1. Create a new tag and release on GitHub
2. Publish the release
3. The workflow in `.github/workflows/publish.yml` will handle the rest

The automated publishing uses PyPI's trusted publishing feature, which is more secure than token-based authentication.

## Troubleshooting

If you encounter dependency resolution issues during build or installation, the package uses uv's `unsafe-best-match` index strategy (configured in pyproject.toml) to handle dependencies from multiple sources.
