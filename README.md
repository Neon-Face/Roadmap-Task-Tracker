# CLI Task Tracker

## Project URL:
https://roadmap.sh/projects/task-tracker

## Introduction

A simple command-line interface (CLI) application for tracking and managing your tasks. This project helps you keep track of what you need to do, what you are currently working on, and what you have accomplished, all from your terminal.

## Features

*   **Add Tasks:** Easily add new tasks with a description.
*   **Update Tasks:** Modify the description of an existing task.
*   **Delete Tasks:** Remove tasks you no longer need.
*   **Mark Tasks:** Change the status of a task to 'todo', 'in-progress', or 'done'.
*   **List Tasks:** View all your tasks, or filter them by status (e.g., done, in-progress).
*   **Persistent Storage:** All tasks are saved automatically to a `tasks.json` file in the same directory, so your data is preserved between sessions.

## Requirements

*   Python 3.x (This project uses standard Python libraries only, no external installations are required.)

## How to Run

1.  **Save the script:** Save the provided Python code as `task_tracker.py` in a directory of your choice.
2.  **Open your terminal/command prompt:** Navigate to the directory where you saved `task_tracker.py`.

    ```bash
    cd /path/to/your/project
    ```

3.  **Execute commands:** Run the script using `python task_tracker.py` followed by the desired command and its arguments.

## Command-Line Usage

The basic syntax for running the application is:

```bash
python task_tracker.py <command> [arguments]