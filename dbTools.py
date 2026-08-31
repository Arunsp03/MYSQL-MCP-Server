from dbConfig import db_config 
import pymysql.cursors
import json

def get_connection():
    """Helper function to create a new database connection."""
    return pymysql.connect(**db_config)

def fetch_tasks():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from tasks;")                
            result = cursor.fetchall()
            return json.dumps(result, indent=2, default=str)
    except Exception as e:
        return f"Database fetch error: {str(e)}"
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

def insert_task(title: str, description: str, due_date: str) -> str:
    try:
        connection = get_connection()
        with connection.cursor() as cursor:            
            sql = "INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)"
            cursor.execute(sql, (title, description, due_date))        
        connection.commit()
        return f"Successfully added task: '{title}'"
    except Exception as e:
        return f"Database insert error: {str(e)}"
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

def update_task_status(task_id: int, new_status: str) -> str:
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "UPDATE tasks SET status = %s WHERE id = %s"
            cursor.execute(sql, (new_status, task_id))
            
            if cursor.rowcount == 0:
                return f"No task found with ID {task_id}."
                
        connection.commit()
        return f"Successfully updated task #{task_id} to '{new_status}'."
    except Exception as e:
        return f"Database update error: {str(e)}"
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

def delete_task(task_id: int) -> str:
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "DELETE FROM tasks WHERE id = %s"
            cursor.execute(sql, (task_id,))
            
            if cursor.rowcount == 0:
                return f"No task found with ID {task_id}."
                
        connection.commit()
        return f"Successfully deleted task #{task_id}."
    except Exception as e:
        return f"Database delete error: {str(e)}"
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()