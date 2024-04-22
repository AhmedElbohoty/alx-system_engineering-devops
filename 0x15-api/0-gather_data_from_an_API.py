#!/usr/bin/python3
'''
For a given employee ID, returns information about his TODO list progress.
'''
import requests
import sys


def get_employee_todo(employee_id):
    '''
    For a given employee ID, returns information about his TODO list progress.

    Args:
        employee_id (str): the employee id.
    '''
    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    timeout = 5

    try:
        # Get Employee info
        employee_resp = requests.get(employee_url, timeout=timeout)
        employee_name = employee_resp.json()['name']

        # Get fetch todo list
        todo_resp = requests.get(todo_url, timeout=timeout)
        todos = todo_resp.json()

        total_tasks = len(todos)
        done_tasks = sum(1 for task in todos if task['completed'])

        print(f"Employee {employee_name} is done with tasks({
              done_tasks}/{total_tasks}):")

        for task in todos:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    get_employee_todo(sys.argv[1])
