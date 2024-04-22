#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
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

    dictionary = {employee_id: []}
    for task in todos:
        dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })
    with open(f'{employee_id}.json', 'w', encoding="utf-8") as filename:
        json.dump(dictionary, filename)
