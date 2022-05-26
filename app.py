from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.htm")


@app.get("/user/victor")
def get_users():
    return {"nome": "Victor", "idade": 28}


@app.get("/states")
def get_states():
    with open("db.json", "r") as file:
        return file.read()


app.run(debug=True, port=33507)
