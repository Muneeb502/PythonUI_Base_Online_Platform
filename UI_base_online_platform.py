from flask import Flask, request, render_template
import sqlite3 as sql

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/teachersignup" , methods =["POST","GET"]) 
def teachersignup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        sub_id = request.form["sub_id"]
        password = request.form["password"]
        with sql.connect("mydata.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO teachers (name, email ,subject_id, password) VALUES ( ?, ?,?,?)", (name, email ,sub_id, password))
            con.commit()
        return render_template("teacherlogin.html")
    return render_template("teachersign.html")



@app.route("/teacherlogin" , methods =["POST","GET"])
def teacherlogin():
    if request.method == "POST":
        email = request.form["email"]
        sub_id = request.form["subject_id"]
        password = request.form["password"]
        
        # Connect to the database
        with sql.connect("mydata.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM teachers WHERE email = ? AND subject_id = ? AND password = ?", (email,sub_id, password))
            teacher = cur.fetchone()
        
        # Check if a matching student is found
        if teacher:
            # Redirect to a dashboard or home page after successful login
            return render_template("tech_dashboard.html")
        else:
            # Render the login page again with an error message
            error = "Invalid email or password. Please try again."
            return render_template("teacherlogin.html", error=error)
    
    return render_template("teacherlogin.html")
    
    
    
@app.route("/studentsignup"  , methods =["POST","GET"])
def studentsignup():    
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        with sql.connect("mydata.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name, email , password) VALUES ( ?, ?,?)", (name, email , password))
            con.commit()
        return render_template("studentlogin.html")
    return render_template("studentsign.html")

@app.route("/studentlogin" , methods =["POST","GET"])
def studentlogin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        # Connect to the database
        with sql.connect("mydata.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM students WHERE email = ?  AND password = ?", (email, password))
            student = cur.fetchone()
        
        # Check if a matching student is found
        if student:
            # Redirect to a dashboard or home page after successful login
            return render_template("student_dashboard.html")
        else:
            # Render the login page again with an error message
            error = "Invalid email or password. Please try again."
            return render_template("studentlogin.html", error=error)
    
    return render_template("studentlogin.html")





@app.route("/techer/dashboard")
def tecacher_dashboard():
    return render_template("tech_dashboard.html")

app.route("/student/dashboard")
def student_dashboard():
     
    return render_template("student_dashboard.html")


#crestinf shw data route that show the data in student table
# just temporay

@app.route("/showdata")
def show_data():
        con = sql.Connection("mydata.db")
        con.row_factory =sql.Row
        
        cur =con.cursor()
        
        cur.execute("select * from teachers ")
        
        rows = cur.fetchall()
        
        return render_template("show.html", rows=rows)









if __name__ == "__main__":
    app.run(debug=True,port=5052)