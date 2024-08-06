from flask import Flask, request, render_template

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