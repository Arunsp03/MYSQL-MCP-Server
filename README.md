# MSSQL MCP Server

This project exposes a lightweight Model Context Protocol (MCP) server for managing tasks in a MySQL database. It gives Claude Desktop and other MCP-compatible clients a clean way to list tasks, add new ones, update their status, and delete them.

> Note: the codebase is configured for MySQL using PyMySQL, even though the repository name references MSSQL. The connection settings are managed through environment variables in `dbConfig.py`.

## Features

- Fetch all tasks
- Add a new task
- Update task status
- Delete a task
- Uses environment variables for database configuration
- Works with Claude Desktop through MCP integration

## Project Structure

- `mcp_server.py` – MCP server definition and tool registration
- `dbTools.py` – database helper functions
- `dbConfig.py` – MySQL connection configuration
- `requirements.txt` – Python dependencies
- `.env` – local environment settings (not committed to Git)

## Prerequisites

Before running this project, make sure you have:

- Python 3.9+
- MySQL Server or MariaDB running locally or on a remote host
- A database named `tasks` (or update the value in `.env`)
- Access to the database with credentials that can create/read/update/delete rows

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```env
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=tasks
DB_PORT=3306
```

5. Make sure the database exists and contains a `tasks` table. Example schema:

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Running the Server

Start the MCP server:

```bash
python mcp_server.py
```

The server will expose tools such as:

- `fetch_tasks`
- `add_new_task`
- `update_task_status`
- `delete_task`

## Claude Desktop Setup

To connect this MCP server to Claude Desktop:

1. Open Claude Desktop.
2. Go to Settings > Developer > Edit Config.
3. Open the `claude_desktop_config.json` file.
4. Add the server configuration below:

```json
{
  "mcpServers": {
    "mysql-tasks-server": {
      "command": "C:/path/to/python.exe",
      "args": [
        "C:/path/to/MSSQL MCP Server/mcp_server.py"
      ],
      "env": {
        "DB_HOST": "127.0.0.1",
        "DB_USER": "root",
        "DB_PASSWORD": "your_password",
        "DB_NAME": "tasks",
        "DB_PORT": "3306"
      }
    }
  }
}
```

### Important notes

- Replace `C:/path/to/python.exe` with the actual Python executable from your virtual environment.
- Replace the project path with the real folder location where this repo is saved.
- If you run the server from a virtual environment, the Python path is usually something like:

```powershell
C:\Users\YOUR_NAME\Projects\MSSQL MCP Server\.venv\Scripts\python.exe
```

- If Claude Desktop does not detect the server, restart Claude Desktop after saving the config.

## Example Usage

Once connected in Claude Desktop, you can ask things like:

- “Show me all tasks.”
- “Add a task called ‘Prepare sprint demo’ due on 2026-09-01.”
- “Update task 3 to completed.”
- “Delete task 8.”

## Troubleshooting

### Server won't start

- Verify Python is installed and the virtual environment is activated.
- Check that dependencies are installed with `pip install -r requirements.txt`.
- Confirm the `.env` values are correct.

### Database connection fails

- Ensure MySQL is running.
- Check the DB host, username, password, port, and database name.
- Make sure the user has correct privileges.

### Claude Desktop cannot find the server

- Confirm the config file is valid JSON.
- Validate the Python executable and project path are correct.
- Restart Claude Desktop after editing the config.

## License

This project is provided as-is for educational and local development purposes.
