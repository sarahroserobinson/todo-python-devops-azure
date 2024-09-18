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

@app.post("/")
def add_to_do():
    req = request.get_json()
    task = req.get('task')
    if task:
        new_task = To_Do(task=task, done=False)
        db.session.add(new_task)
        db.session.commit()
        return "To Do list updated"
    else:   
        return "Please provide task: None given", 400


if __name__ == "__main__":
    app.run(debug=True)