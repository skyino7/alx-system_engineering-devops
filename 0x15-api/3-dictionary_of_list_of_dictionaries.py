#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests
import sys


def main():
    """Python script to export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/"
    users = f'{url}users'
    todos = f'{url}todos'

    user_data = requests.get(f'{url}{users}').json()
    todos_data = requests.get(f'{url}{todos}').json()

    data = {}
    for user in user_data:
        user_id = user.get("id")
        data[user_id] = [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in todos_data if task.get("userId") == user_id]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
