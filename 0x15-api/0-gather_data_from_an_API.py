#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    user_Id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    finished = [t.get('title') for t in todos if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(todos)))
    [print("\t {}".format(c)) for c in finished]
