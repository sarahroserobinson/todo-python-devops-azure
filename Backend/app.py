from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

to_do_list = []
CORS(app)

@app.get("/")
def get_list():
    return jsonify(to_do_list)

@app.post("/")
def add_to_do():
    task = request.json.get('task')
    to_do_list.append({'to_do': task})
    return jsonify({'message': 'to do list updated'}), 201

if __name__ == "__main__":
    app.run(debug=True)