import os
import json
import sys
from datetime import datetime

TASK_FILE = "tasks.json"

def _load_tasks():
    if not os.path.exists(TASK_FILE):
        print("No Tasks File Detected.")
        print("Creating Empty Tasks File...")
        _save_tasks([])
        return []
    
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                print("Tasks File Should Be A List, Initializing An Empty Tasks File...")
                _save_tasks([])
                return []
            return tasks
    except json.JSONDecodeError:
        print("Tasks File Is Corrupted, Initializing An Empty Tasks File...")
        _save_tasks([])
        return []
    except Exception as e:
        print(f"Error Loading Tasks File: {e}")
        return []

def _save_tasks(tasks: list):
    try:
        with open(TASK_FILE,"w",encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving tasks to '{TASK_FILE}': {e}", file = sys.stderr)

def print_help():
    print("Usage: python task_tracker.py <command> [arguments]")
    print("\nCommands:")
    print("  help                                - Show this help message.")
    print("  add <description>                   - Add a new task.")
    print("  list [status_filter]                - List all tasks. Optional filters: 'todo', 'in-progress', 'done', 'not-done'.")
    print("  update <id> <new_description>       - Update an existing task's description by ID.")
    print("  mark <id> <status>                  - Mark a task with status: 'todo', 'in-progress', 'done'.") # Updated help
    print("  delete <id>                         - Delete a task by ID.") # New help
    print("\nExamples:")
    print("  python task_tracker.py add \"Buy groceries\"")
    print("  python task_tracker.py list in-progress")
    print("  python task_tracker.py mark 5 done")
    print("  python task_tracker.py update 3 \"Review project proposal\"")
    print("  python task_tracker.py delete 1")

def _generate_new_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def _find_task(tasks, id):
    for i, task in enumerate(tasks):
        if task['id'] == int(id):
            return i
    return None

def add_task(tasks, description):
    task = {
        "id" : _generate_new_id(tasks),
        "description": description,
        "status": 'todo',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    tasks.append(task)
    _save_tasks(tasks)
    print(f"Added Task: ID {task['id']} - {task['description']}")

def list_tasks(tasks, status = None):
    
    filtered_tasks = []
    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
    else:
        filtered_tasks = tasks
    
    if not filtered_tasks:
        if status:
            print(f"No tasks found with status: {status}")
            print("Supported status: 'todo', 'in-progress', 'done'")
        else:
            print("No tasks at the moment.")
        return

    for task in filtered_tasks:
        print(f"{task['status']} - {task['description']} - Updated at: {task['updated_at']}")
    
def update_task(tasks, id, description):
    if not tasks:
        print("No Tasks To Be Updated")
        return
    task_index = _find_task(tasks, id)
    if task_index is not None:
        tasks[task_index]['description'] = description
        tasks[task_index]['updated_at'] = datetime.now().isoformat()
        _save_tasks(tasks)
        print(f"Task {id} is updated.")
        return
    else:
        print(f"No task found for id: {id}")
        return

def mark_task(tasks, id, mark):
    if not tasks:
        print("No Tasks To Be Updated")
        return
    task_index = _find_task(tasks, id)
    if task_index is not None:
        if mark == "mark-in-progress":
            tasks[task_index]['status'] = "in-progress"
            tasks[task_index]['updated_at'] = datetime.now().isoformat()
        elif mark == "mark-done":
            tasks[task_index]['status'] = "done"
            tasks[task_index]['updated_at'] = datetime.now().isoformat()
        _save_tasks(tasks)
        return
    else:
        print("No task found.")
        return

def delete_task(tasks, id):
    if not tasks:
        print(f"No task found for id: {id}")
        return
    task_index = _find_task(tasks, id)
    if task_index is not None:
        tasks.pop(task_index)
        _save_tasks(tasks)
        return

def main():
    args = sys.argv[1:]
    
    if not args or args[0] == "help":
        print_help()
        return
    
    tasks = _load_tasks()

    command = args[0]
 
    if command == "add":
        if len(args) < 2:
            print("Add function requires 'description'")
            print_help()
            sys.exit(1)
        description = " ".join(args[1:])
        add_task(tasks, description)
    elif command == "list":
        if len(args) > 1:
            status = args[1].lower()
        else:
            status = None
        list_tasks(tasks, status)
    elif command == "update":
        if len(args) < 3:
            print("Update function requires 'id' and 'description'")
            print_help()
            sys.exit(1)
        id = args[1]
        description = " ".join(args[2:])
        update_task(tasks, id, description)
    elif command == "mark-in-progress" or command == "mark-done":
        if len(args) < 2:
            print("Mark function requires 'id'")
            print_help()
            sys.exit(1)
        id = args[1]
        mark_task(tasks, id, command)
    elif command == "delete":
        if len(args) < 2:
            print("Delete function requires 'id'")
            print_help()
            sys.exit(1)
        id = args[1]
        delete_task(tasks, id)
    else:
        print("Unknown Command.")
        print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()

