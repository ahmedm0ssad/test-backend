from flask import Flask, jsonify, request
import tasks  # Import functions from tasks.py

app = Flask(__name__)

# 1. Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks.get_all_tasks()})

# 2. Get a single task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get_task_by_id(task_id)
    if task:
        return jsonify({"task": task})
    else:
        return jsonify({"error": "Task not found"}), 404

# 3. Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.json.get('title')
    if new_task:
        return jsonify({"task": tasks.create_task(new_task)}), 201
    else:
        return jsonify({"error": "Invalid input"}), 400

# 4. Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    title = request.json.get('title')
    completed = request.json.get('completed')
    updated_task = tasks.update_task(task_id, title, completed)
    if updated_task:
        return jsonify({"task": updated_task})
    else:
        return jsonify({"error": "Task not found"}), 404

# 5. Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if tasks.delete_task(task_id):
        return jsonify({"message": "Task deleted successfully"})
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
