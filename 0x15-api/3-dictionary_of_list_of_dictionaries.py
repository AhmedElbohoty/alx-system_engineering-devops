#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests


if __name__ == '__main__':
    timeout = 5

    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    users_resp = requests.get(users_url, timeout=timeout)
    users = users_resp.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')

        todo_url = f'{base_url}/users/{user_id}/todos/'
        todo_resp = requests.get(todo_url, timeout=timeout)
        todos = todo_resp.json()

        dictionary[user_id] = []
        for todo in todos:
            user = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user_name
            }
            dictionary[user_id].append(user)

    with open('todo_all_employees.json', 'w', encoding="utf-8") as filename:
        json.dump(dictionary, filename)
