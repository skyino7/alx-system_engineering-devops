#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys


def main():
    """Script to export data in the CSV format"""

    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    employee_url = f'{url}users?id={employee_id}'
    todos = f'{url}todos?userId={employee_id}'
    done = f'{url}todos?userId={employee_id}&completed=true'
    not_done = f'{url}todos?userId={employee_id}&completed=false'

    user_data = requests.get(f'{url}{employee_url}').json()
    empN = user_data[0].get("username")

    todos_data = requests.get(f'{url}{todos}').json()
    todos_done = requests.get(f'{url}{done}').json()

    doneTask = len(todos_done)
    totalTask = len(todos_data)

    with open(f'{employee_id}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, empN,
                            task.get("completed"), task.get("title")])


if __name__ == "__main__":
    main()
