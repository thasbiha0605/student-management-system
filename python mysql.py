from random import choice
from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="RihanDawood@0410",database="pythonsql_db")



def insert(name,department,city):
    se=con.cursor()
    sql="insert into students (name,department,city) values (%s,%s,%s)"
    student =(name,department,city)
    se.execute(sql,student)
    con.commit()
    print("data insert success")


def update(name,department,city,id):
    se = con.cursor()
    sql = "update students set name=%s,department=%s,city=%s where id=%s"
    student = (name, department, city,id)
    se.execute(sql, student)
    con.commit()
    print("data update success")

def select():
    se=con.cursor()
    sql="select id,name,department,city from students"
    se.execute(sql)
    #result=se.fetchone()
    result=se.fetchall()
    print(tabulate(result,headers=["id","name","age","city"]))

def delete(id):
    se = con.cursor()
    sql = "delete from students where id=%s"
    student = (id,)
    se.execute(sql, student)
    con.commit()
    print("data delete success")

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
       name = input("Enter name :")
       department = input("Enter department :")
       city = input("Enter city :")
       insert(name, department, city)
    elif choice == 2:
        id = input("Enter the id: ")
        name = input("Enter name :")
        department = input("Enter department :")
        city = input("Enter city :")
        update(name, department, city, id)
    elif choice == 3:
        select()
    elif choice== 4:
        id=input("Enter the id to delete :")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid selection.please try again ")

