# Installation Guide

This guide walks through installing and running the Task MCP server locally.

## 1. Prerequisites

Make sure the following are installed:

- Python 3.9+
- MySQL Server
- Git

## 2. Clone the Repository

```bash
git clone https://github.com/Arunsp03/MYSQL-MCP-Server
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the Database

Create a `.env` file in the project root:

```env
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=tasks
DB_PORT=3306
```

Then create the tasks table if it does not exist:

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

## 5. Run the Server

```bash
python mcp_server.py
```

This starts the MCP server and exposes tools such as:

- `fetch_tasks`
- `add_new_task`
- `update_task_status`
- `delete_task`

## 6. Connect to Claude Desktop

Open the Claude Desktop config file and add:

```json
{
  "mcpServers": {
    "mysql-tasks-server": {
      "command": "C:/path/to/python.exe",
      "args": [
        "C:/path/to/your-project-folder/mcp_server.py"
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

Then restart Claude Desktop.

## Troubleshooting

- If the server fails to start, verify the Python path and dependencies.
- If the database fails to connect, confirm MySQL is running and credentials are correct.
- If Claude Desktop does not recognize the tool, validate the JSON config and restart the app.

## Next Steps

Once the server is connected, you can ask Claude Desktop to manage tasks directly through the MCP tools.
