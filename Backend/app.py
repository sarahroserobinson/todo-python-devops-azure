from flask import Flask, request

app = Flask(__name__)

to_do_list = []

@app.get("/")
def get_list():
    return to_do_list

@app.post("/")
def add_to_do():
    return

if __name__ == "__main__":
    app.run(debug=True)