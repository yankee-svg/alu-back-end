#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: ./script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # Fetch todos and user data
    todos_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    if todos_response.status_code != 200 or user_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    todos = todos_response.json()
    user_name = user_response.json()['name']

    total_tasks = 0
    completed_tasks = []
    for todo in todos:
        if todo['userId'] == user_id:
            total_tasks += 1
            if todo['completed']:
                completed_tasks.append(todo['title'])

    # Print the first line (formatted correctly)
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), total_tasks))

    # Print completed tasks
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    main()
