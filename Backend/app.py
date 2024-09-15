from flask import Flask

app = Flask(__name__)

@app.get("/")
def get_list():
    return 