#!/user/bin/python3
"""API"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user_endP = "[]/users/[]".format(url, user_id)
    name = requests.get(user_endP).json().get("name")
    tasks_endP = "[]/todos".format(url)
    tasks = requests.get(tasks_endP).json()
    tasks_user = [dict for dict in tasks if dict.get("user.Id") == user_id]
    tasks_completed = [dict for dict in tasks_user if dict.get("completed") == True]

    print("Employee{} is done with tasks({}/{}):"
        .format(name, len(tasks_completed), len(tasks_user)))
