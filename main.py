import requests
import sqlite3                                      #IT ALLOWS PYTHON TO COMMUNICATE WITH SQLITE DATABASES
from pydantic import BaseModel
from fastapi import FastAPI
conn=sqlite3.connect("students.db",check_same_thread=False)                 #CREATING A DATABASE CONNECTION
cursor=conn.cursor()                                #CREATING A DATABASE CURSOR
cursor.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,age INTGER,
course TEXT)""")
app=FastAPI()
class student(BaseModel):
    name:str
    age:int
    course:str
students=[]
@app.get("/")
def home():
    return{"message":"student management api"}

@app.post("/students")
def add_student(student :student):
    cursor.execute("INSERT INTO students(name,age,course) VALUES (?,?,?)",(student.name,student.age,student.course))  #EXCUTE SQL COMMAND IN DATABASE ,insert into MEANS ADD NEW RECORD,students DATABASE TABLE,name,age,course ARE COLUMNS, ? REPRESENTS A VALUE THAT WILL SUPPLY SEPARATELY
    conn.commit()
    return{"msg":"student added sucusfully"}

@app.get("/students")
def student_details():
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    return[
        {"id":row[0],
        "name":row[1],
        "age":row[2],
        "course":row[3]
        }
        for row in rows
    ]

@app.get("/students/{id}")
def student_by_id(id:int):
    for student in students:
        if student["id"]==id:
            return student
    return {"message ":"student not found"}

@app.put("/students/{id}")
def update_stu(id:int,updated_stu:student):
    for student in students:
        if student["id"]==id:
            student.update(updated_stu.model_dump())
            return student
    return {"msg":"not found"}

@app.delete("/students/{id}")
def delete_stu(id:int):
    for student in students:
        if student["id"]==id:
            students.remove(student)
            return {"msg":"deleted sucusfully"}
    return {"msg":"not found"}

