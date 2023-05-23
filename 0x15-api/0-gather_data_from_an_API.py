#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user_id = sys.argv[1]
    user_endPoint = "{}/users/{}".format(url,user_id)
    name = requesta.get(user_endPoint).json().get("name")
    task_endPoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endPoint).json()
    user_tasks = [task for task in tasks if task.get("userId") == user_id]
    completed_tasks = [task for task in user_tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):"
            .format(name, len(completed_tasks), len(user_tasks)))
