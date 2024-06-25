from flask import Flask ,request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#  configuration key
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/projectno3_database"

db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
   __tablename__ = "STUDENTS"
   id = db.Column(db.Integer,primary_key = True,autoincremant=True)
   name = db.Column(db.String(200),nullable= False)
   email = db.Column(db.String(200), unique = True,nullable= False)
   password = db.Column(db.String(200), nullable= False)

# Define the Teacher model
class Teacher(db.Model):
   __tablename__ = "TEACHERS"
   id = db.Column(db.Integer,primary_key = True,autoincremant=True)
   name = db.Column(db.String(200),nullable= False)
   email = db.Column(db.String(200), unique = True,nullable= False)
   password = db.Column(db.String(200), nullable= False)

# Create the database tables
with app.app_context():
    db.create_all()

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

@app.route("/techer/dashboard")
def tecacher_dashboard():
    return render_template()


if __name__ == "__main__":
    app.run(debug=True,port=5001)