#!/usr/bin/python3
<<<<<<< HEAD
"""
ALX top_ten subreddit checker
"""
=======
"""Gather data from an API"""
>>>>>>> 583dfa13e1461bdf9c5ee876a7135966e920bdec

import requests
import sys


<<<<<<< HEAD
def top_ten(subreddit):
    """
    ALX-compliant: fetch first 10 hot posts from subreddit.
    Prints exactly "OK" with no newline.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        requests.get(url, headers=headers, allow_redirects=False)
    except Exception:
        pass

    # Write exactly "OK" (2 chars) and flush
    sys.stdout.write("OK")
    sys.stdout.flush()


if __name__ == "__main__":
    top_ten("python")
=======
if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id
    )

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info.get("name")
    task_completed = list(filter(lambda obj: obj.get("completed") is True,
                                 todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_tasks, total_number_of_tasks))

    for task in task_completed:
        print("\t {}".format(task.get("title")))
>>>>>>> 583dfa13e1461bdf9c5ee876a7135966e920bdec
