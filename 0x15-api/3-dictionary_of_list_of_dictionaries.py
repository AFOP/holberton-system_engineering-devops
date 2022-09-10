#!/usr/bin/python3
"""Exports data todo all employees in the JSON format"""

if __name__ == "__main__":

    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users")

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if (task.get('id')):
            taskDict = {"username": task.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
            taskList.append(taskDict)
            todoUser[task.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoUser, f)
