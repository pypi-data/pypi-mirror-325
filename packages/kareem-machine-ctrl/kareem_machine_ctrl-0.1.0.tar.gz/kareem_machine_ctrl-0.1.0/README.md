# kareem-machine-ctrl

This is a sample project demonstrating an MCP integration using FastMCP.

## Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -e .
```

## Run

You can run the MCP server with uv (make sure uv is installed):

```bash
uv run server.py
```

This will start the MCP server, ready to accept protocol commands.
