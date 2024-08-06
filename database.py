import sqlite3

con = sqlite3.connect("myuserdatabase")

print("open data base")

con.execute("CREAT TABLE IF NOT EXISTS student_reg ()")



print("database creat succesfully ")


con.close()