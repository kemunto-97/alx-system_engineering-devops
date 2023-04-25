#!/usr/bin/python3

import csv
import requests
import sys


def to_csv():
    try:
        user_id = int(sys.argv[1])
    except IndexError:
        print("Please provide a user ID as an argument.")
        return

    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    user = next((u for u in users if u.get('id') == user_id), None)
    if user is None:
        print("User not found.")
        return
    username = user.get('username')

    todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    task_status_title = [(t.get('completed'), t.get('title')) for t in todos if t.get('userId') == user_id]

    filename = f"{user_id}.csv"
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for task in task_status_title:
            writer.writerow({"USER_ID": user_id, "USERNAME": username,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
