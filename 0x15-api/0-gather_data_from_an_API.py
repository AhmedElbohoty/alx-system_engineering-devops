#!/usr/bin/python3
"""For employee ID, returns information about his todo list progress"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    timeout = 5

    # Get Employee info
    employee_resp = requests.get(employee_url, timeout=timeout)
    employee_name = employee_resp.json().get("name")

    # Get fetch todo list
    todo_resp = requests.get(todo_url, timeout=timeout)
    todos = todo_resp.json()

    total_tasks = len(todos)
    done_todos = sum(1 for task in todos if task.get("completed"))

    print(f"Employee {employee_name} is done with tasks({\
          done_todos}/{total_tasks}):")

    for task in todos:
        if task.get("completed"):
            print(f"\t{task.get('title')}")
