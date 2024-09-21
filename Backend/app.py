from flask import Flask, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://username:password@azurehost:portnum/to_do_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class To_Do(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(100))
    done = db.Column(db.Boolean)


CORS(app)

@app.get("/")
def get_list():
    to_do_list =  To_Do.query.all()
    return render_template("index.html", completed_list=to_do_list)

@app.post("/toggle")
def toggle_completed():
    req = request.get_json()
    task_id = req.get('id')
    task_id_num = int(task_id)
    print(f"Received task ID: {task_id}") 
    task = To_Do.query.get(task_id_num)
    if task:
        task.done = not task.done
        db.session.commit()
        return "Task updated", 200
    else:
        return "That task isn't included in the list", 404

@app.post("/addtask")
def add_to_do():
    req = request.get_json()
    task = req.get('task')
    if task:
        new_task = To_Do(task=task, done=False)
        db.session.add(new_task)
        db.session.commit()
        return "To Do list updated", 201
    else:   
        return "Please provide task: None given", 400

@app.delete("/removetask")
def remove_task():
    req = request.get_json()
    task2 = req.get('task')
    to_do = To_Do()
    task_to_delete = db.session.query(to_do)
    db.session.delete(task_to_delete)
    db.session.commit()
    return "Task has been deleted", 200


if __name__ == "__main__":
    app.run(debug=True)