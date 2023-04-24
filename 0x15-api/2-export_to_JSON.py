#!/usr/bin/python3
"""
A script to export data in the CSV format..
"""
if __name__ == '__main__':
    import requests
    import sys
    import json

    base_url = "https://jsonplaceholder.typicode.com"

    employee_id = int(sys.argv[1])

    user_info_url = "{}/users/{}".format(base_url, employee_id)
    todo_list_url = user_info_url + "/todos"
    user_info_response = requests.get(user_info_url).json()
    todo_list_response = requests.get(todo_list_url).json()
    username = user_info_response.get("username")
    total_task = todo_list_response
    completed_task_titles = []
    for task in total_task:
        id_completed = {}
        id_completed["task"] = str(task.get("title"))
        id_completed["completed"] = str(task.get("completed"))
        id_completed["username"] = str(username)
        completed_task_titles.append(id_completed)
    completed = {}
    completed[employee_id] = completed_task_titles
    with open("{}.json".format(employee_id), "w") as filejson:
        filejson.write(json.dumps(completed))
