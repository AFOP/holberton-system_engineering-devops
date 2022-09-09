#!/usr/bin/python3
"""
Write a Python script that,
using this REST API, for a given employee ID,
returns information about his/her TODOS list progress.
"""

import requests
import sys

if __name__ == "__main__":
    one_title = []
    titles = ""
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if (task.get('userId') == int(userId)) and task.get('completed'):
            completed += 1
            totalTasks += 1
            titles += "\n"
            titles += "\t"
            titles += task.get('title')
        elif (task.get('userId') == int(userId)):
            totalTasks += 1

    print(
        "Employee {} is done with tasks({}/{}):{}"
        .format(name, completed, totalTasks, titles))
