from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from sqlalchemy.sql import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://username:password@azurehost:portnum/to_do_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class To_Do(db.model):
    _tablename_ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(100))
    done = db.Column(db.boolean)


CORS(app)

@app.get("/")
def get_list():
    to_do_list =  To_Do.query.all()
    return render_template("index.html", todo_list=to_do_list)

@app.post("/")
def add_to_do():
    task = request.form.get('task')
    new_task = To_Do(task=task, complete=false)
    db.session.add(new_task)
    db.session.commit
    return To_Do


if __name__ == "__main__":
    app.run(debug=True)