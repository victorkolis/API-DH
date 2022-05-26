from flask import Flask


app = Flask(__name__)


@app.get("/home")
def home():
    return "<h1>Olá</h1>"


@app.get("/victor")
def get_users():
    return {"nome": "Victor", "idade": 28}


@app.get("/states")
def get_states():
    with open("db.json", "r") as file:
        return file.read()
