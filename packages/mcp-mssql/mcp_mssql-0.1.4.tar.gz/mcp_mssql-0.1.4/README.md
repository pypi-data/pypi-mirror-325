# mcp-mssql

MSSQL server package for MCP (Message Communication Protocol)

## Installation

```bash
pip install mcp-mssql
```

## Usage

```python
from mssql.server import DBConfig

# Configure your database
db = DBConfig()
connection = db.get_connection()
```

## Environment Variables

Required environment variables:
- MSSQL_SERVER
- MSSQL_DATABASE
- MSSQL_USER
- MSSQL_PASSWORD
- MSSQL_DRIVER