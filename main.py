import json
import os
from datetime import datetime

def add_task(args):
    if not args:
        print("No arguments provided")
        return
    with open("task_data.json", "r") as json_file:
        task_data = json.load(json_file)
    new_task = {
        "id": len(task_data) + 1,
        'description': args,
        "status": "to-do"
    }
    task_data.append(new_task)
    with open("task_data.json", "w") as json_file:
        json.dump(task_data, json_file, indent=4)

def handle_user_input(user_input):
    split_user_input = user_input.split()
    if not split_user_input:
        return
    command = split_user_input[0]
    args = split_user_input[1:]
    if command == "add":
        add_task(" ".join(args))


def read_user_input():
    user_input = input("task-cli ")
    handle_user_input(user_input)

def check_json_exists():
    json_path = "task_data.json"
    if not os.path.exists(json_path):
        with open(json_path, "w") as json_file:
            json.dump([], json_file)

def task_cli():
    check_json_exists()
    read_user_input()


if __name__ == '__main__':
    task_cli()