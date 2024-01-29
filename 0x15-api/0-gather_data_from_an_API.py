#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import sys
import requests


def main():
    """Retrieve and display employee TODO list progress."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    response = requests.get(url)
    json_obj = response.json()
    EMPLOYEE_NAME = json_obj.get("name")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    response = requests.get(url)
    json_obj = response.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for task in json_obj:
        if task.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task.get("title"))
        TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
