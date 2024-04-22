#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    timeout = 5

    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee_resp = requests.get(employee_url, timeout=timeout)
    employee_name = employee_resp.json().get('username')

    todo_resp = requests.get(todo_url, timeout=timeout)
    todos = todo_resp.json()

    with open(f'{employee_id}.csv', 'w', encoding="utf-8") as file:
        for task in todos:
            title = task.get('title')
            comp = task.get('completed')
            row = f'"{employee_id}","{employee_name}","{comp}","{title}"\n'
            file.write(row)
