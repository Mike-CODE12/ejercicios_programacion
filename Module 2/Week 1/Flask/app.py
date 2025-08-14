import json
from flask import Flask, request, jsonify
import os


app = Flask(__name__)

TASKS_FILE = 'tasks.json'

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

def read_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            content = file.read()
            if not content:
                return []
            return json.loads(content)
    except IOError as e:
        if "No such file" in str(e):
            return jsonify({"error": "Tasks file not found"}), 404
        elif "Permission denied" in str(e):
            return jsonify({"error": "Permission denied while reading tasks"}), 503
        else:
            return jsonify({"error": "Error accessing the tasks file"}), 503
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in the tasks file"}), 422

def write_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError as ex:
        if "No space" in str(ex):
            return jsonify({"error": "Insufficient storage space to save tasks"}), 507
        elif "Permission denied" in str(ex):
            return jsonify({"error": "Permission denied while writing tasks"}), 503
        else:
            return jsonify({"error": "Error saving tasks to the file"}), 503


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    if isinstance(tasks, tuple):  
        return tasks  
    status = request.args.get('status')
    if status:
        filtered_tasks = [task for task in tasks if task.get('status') == status]
        return jsonify(filtered_tasks)
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    
    task_id = new_task.get('id')
    if not isinstance(task_id, int):
        return jsonify({"error": "ID is required and must be an integer"}), 400

    if not new_task.get('title'):
        return jsonify({"error": "Title is required"}), 400
    if not new_task.get('description'):
        return jsonify({"error": "Description is required"}), 400
    if not new_task.get('status'):
        return jsonify({"error": "Status is required"}), 400
    if new_task['status'] not in ['To Do', 'In Progress', 'Completed']:
        return jsonify({"error": "Invalid status. Must be one of: To Do, In Progress, Completed"}), 400

    tasks = read_tasks()
    if isinstance(tasks, tuple):
        return tasks
    if any(t['id'] == task_id for t in tasks):
        return jsonify({"error": "Task with this ID already exists"}), 400

    tasks.append(new_task)
    write_result = write_tasks(tasks)  
    if isinstance(write_result, tuple):  
        return write_result
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    update_data = request.get_json()

    if 'id' in update_data:
        return jsonify({"error": "Task ID cannot be changed"}), 400

    if 'title' in update_data and not update_data['title']:
        return jsonify({"error": "Title cannot be empty"}), 400
    if 'description' in update_data and not update_data['description']:
        return jsonify({"error": "Description cannot be empty"}), 400
    if 'status' in update_data and update_data['status'] not in ['To Do', 'In Progress', 'Completed']:
        return jsonify({"error": "Invalid status. Must be one of: To Do, In Progress, Completed"}), 400

    tasks = read_tasks()
    if isinstance(tasks, tuple):  
        return tasks 
    task_to_update = None
    for task in tasks:
        if task['id'] == task_id:
            task_to_update = task
            break

    if not task_to_update:
        return jsonify({"error": "Task not found"}), 404

    task_to_update.update(update_data)
    write_result = write_tasks(tasks)  
    if isinstance(write_result, tuple): 
        return write_result 
    return jsonify(task_to_update)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = read_tasks()
    if isinstance(tasks, tuple):  
        return tasks 
    task_index = None
    for index, task in enumerate(tasks):
        if task['id'] == task_id:
            task_index = index
            break

    if task_index is None:
        return jsonify({"error": "Task not found"}), 404

    deleted_task = tasks.pop(task_index)
    write_result = write_tasks(tasks)  
    if isinstance(write_result, tuple):  
        return write_result 
    return jsonify(deleted_task)

if __name__ == '__main__':
    app.run(debug=True)