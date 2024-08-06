from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration key
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/projectno_3database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
   __tablename__ = "students"
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(200), nullable=False)
   email = db.Column(db.String(200), unique=True, nullable=False)
   password = db.Column(db.String(200), nullable=False)

# Define the Teacher model
class Teacher(db.Model):
   __tablename__ = "teachers"
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(200), nullable=False)
   email = db.Column(db.String(200), unique=True, nullable=False)
   password = db.Column(db.String(200), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()


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

@app.route("/studentsignup" , methods =["POST","GET"] )
def studentsignup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
        new_student = Student(name=name,email=email,password=password)
        db.session.add(new_student)
        db.session.commit()
        
        return "this is Student form submitted"
    
    return render_template("studentsign.html")

@app.route("/techer/dashboard")
def tecacher_dashboard():
    return render_template("tech_dashboard.html")

app.route("/student/dashboard")
def tecacher_dashboard():
    return render_template("student_dashboard.html")


#crestinf shw data route that show the data in student table



if __name__ == "__main__":
    app.run(debug=True,port=5052)