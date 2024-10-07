# create
# request (frontend) - GET, POST, PUT, PATCH, DELETE, json
# response (backend) - status code, json

from flask import request, jsonify
from config import app, db
from models import Tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Tasks.query.all() # retrieve all tasks from the database
    tasks_json = [task.to_json() for task in tasks]
    return jsonify({"tasks": tasks_json})

@app.route("/create_task", methods=["POST"])
def create_contact():
    email = request.json.get("email")
    to_do = request.json.get("toDo")
    in_progress = request.json.get("inProgress")
    done = request.json.get("done")
    pending = request.json.get("pending")
    
    if not email or not to_do or not in_progress or not done or not pending:
        return (jsonify({"error": "Missing data"}), 400,)
    
    new_task = Tasks(email=email, to_do=to_do, in_progress=in_progress, done=done, pending=pending)
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({"message": "Task created"})

@app.route("/update_task/<int:user_id>", methods=["PATCH"])
def update_task(user_id):
    task = Tasks.query.get(user_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.json
    task.to_do = data.get("toDo", task.to_do)
    task.in_progress = data.get("inProgress", task.in_progress)
    task.done = data.get("done", task.done)
    task.pending = data.get("pending", task.pending)
    
    db.session.commit()
    
    return jsonify({"message": "Task updated"}), 200

@app.route("/delete_task/<int:user_id>", methods=["DELETE"])
def delete_task(user_id):
    task = Tasks.query.get(user_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)