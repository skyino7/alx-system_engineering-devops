#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys


def main():
    """Retrieve and display employee TODO list progress."""
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    employee_url = f'{url}users?id={employee_id}'
    todos = f'{url}todos?userId={employee_id}'
    done = f'{url}todos?userId={employee_id}&completed=true'

    user_data = requests.get(f'{url}{employee_url}').json()
    employee_name = user_data[0].get("name")

    todos_data = requests.get(f'{url}{todos}').json()
    todos_done = requests.get(f'{url}{done}').json()

    done_tasks = len(todos_done)
    total_tasks = len(todos_data)

    print(f'Employee {employee_name} is done with tasks '
          f'({done_tasks} / {total_tasks}): ')
    for task in todos_done:
        print(f'\t {task.get("title")}')


if __name__ == "__main__":
    main()
