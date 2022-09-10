#!/usr/bin/python3
"""
Exports data in the JSON format
"""

import requests
import sys
import csv
import json

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")

    dict_json = {}
    list_tasks = []

    for task in todos.json():
        if task.get('userId') == int(userId):
            dict_task = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            list_tasks.append(dict_task)
    dict_json[userId] = list_tasks
    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(dict_json, f)
