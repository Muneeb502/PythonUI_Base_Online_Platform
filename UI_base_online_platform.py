from flask import Flask ,request, render_template
import sqlite3 as sql


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/teacherlogin")
def teacherlogin():
    return render_template("teacherlogin.html")

@app.route("/studentlogin")
def studentlogin():
    return render_template("studentlogin.html")

@app.route("/teachersignup")
def teachersignup():
    return render_template("teachersign.html")

@app.route("/studentsignup")
def studentsignup():
    return render_template("studentsign.html")


if __name__ == "__main__":
    app.run(debug=True,port=5001)