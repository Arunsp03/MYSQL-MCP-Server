import sys
from mcp.server.mcpserver import MCPServer
import dbTools 

mcp = MCPServer("mysql-tasks-server")
@mcp.tool()
def fetch_tasks(**kwargs) -> str:
    """Fetch all tasks from the MySQL database."""
    try:
        return dbTools.fetch_tasks()
       
        
    except Exception as e:
        print(f"[ERROR] Server error: {str(e)}", file=sys.stderr)
        return f"Database error: {str(e)}"

@mcp.tool()
def add_new_task(title: str, description: str, due_date: str) -> str:
    """Add a new task to the database. due_date must be in YYYY-MM-DD format."""
    print(f"[DEBUG] Adding task: {title}", file=sys.stderr)
    return dbTools.insert_task(title, description, due_date)

@mcp.tool()
def update_task_status(task_id: int, new_status: str) -> str:
    """Update the status of an existing task. Status should usually be 'pending' or 'completed'."""
    print(f"[DEBUG] Updating task {task_id} to {new_status}", file=sys.stderr)
    return dbTools.update_task_status(task_id, new_status)

@mcp.tool()
def delete_task(task_id: int) -> str:
    """Permanently delete a task from the database using its ID."""
    print(f"[DEBUG] Deleting task {task_id}", file=sys.stderr)
    return dbTools.delete_task(task_id)


if __name__ == "__main__":
    print("[DEBUG] Starting MySQL tasks MCP server...", file=sys.stderr)
    mcp.run()