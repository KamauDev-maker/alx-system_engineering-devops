#!/usr/bin/python3
"""
A script to export data in the CSV format..
"""
if __name__ == '__main__':
    import requests
    import sys
    import csv

    base_url = "https://jsonplaceholder.typicode.com"

    employee_id = int(sys.argv[1])

    user_info_url = "{}/users/{}".format(base_url, employee_id)
    user_info_response = requests.get(user_info_url)
    user_info = user_info_response.json()
    employee_name = user_info["name"]

    todo_list_url = "{}/todos?userId={}".format(base_url, employee_id)
    todo_list_response = requests.get(todo_list_url)
    todo_list = todo_list_response.json()

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
                ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_list:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": "COMPLETE" if task["completed"]
                else "INCOMPLETE",
                "TASK_TITLE": task["title"]
                })

    completed_tasks = 0
    total_tasks = len(todo_list)
    completed_task_titles = []
    for task in todo_list:
        if task["completed"]:
            completed_tasks += 1
            completed_task_titles.append(task["title"])

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            completed_tasks,
            total_tasks
            )
        )
    for title in completed_task_titles:
        print("\t {}".format(title))
