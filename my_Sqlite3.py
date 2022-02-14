# import sqlite3
# conn = sqlite3.connect("test.db")
# cur = conn.cursor()
# cur.execute("create table member (id int primary key, name varchar not null, price int default 0)")
# cur.execute("INSERT INTO member VALUES(?,?)", (1,"Tariq")) #wrong, Because we are saying that we want to insert all columns by not specifying the specific columns. so use right way like:
# cur.execute('insert into member (id, name) values(33, "Ahmed")')
# cur.execute("INSERT INTO member VALUES(?,?,?)", (3,"Tariq")) #Right
# cur.execute("INSERT INTO member (id,name) VALUES(1,'RAMAYANA')") #use it, if don't wanna pass default value
# cur.execute("alter table member add column cast varchar")
# cur.execute("alter table member cast add values('Kaleri')")
# cur.execute("SELECT * FROM member")
# for i in cur:
#     print(i)
# conn.commit()
# conn.close()



# import sqlite3
# conn = sqlite3.connect("test.db")
# cur = conn.cursor()
# cur.execute("create table member (id int primary key, name varchar not null, price int default 0)")
# cur.execute("alter table member add column cast varchar")
# cur.execute("ALTER TABLE member ADD constraint")
# cur.execute("SELECT * FROM member")
# for i in cur:
#     print(i)
# conn.commit()
# conn.close()



# import sqlite3
# conn = sqlite3.connect("test.db")
# cur = conn.cursor()
# cur.execute("drop table member")
# cur.execute("create table member (id int not null ,name varchar(100) not null, price int default 0)")
# cur.execute("insert into member('id', 'name', 'price') values(4, 'tariq', 100)")

# cur.execute("alter table member add column cast varchar(100)")
# cur.execute("")
# cur.execute("SELECT * FROM member")
# for i in cur:
#     print(i)
# conn.commit()
# conn.close()



# import sqlite3
# con = sqlite3.connect("test.db")
# cur = con.cursor()
# cur.execute("create table member (id int primary key, name varchar not null, price int default 0)")
# cur.execute("CREATE TABLE Students (Name text, RollNo real)")
# cur.execute("alter table Students add column cast varchar(100)")
# cur.execute("INSERT INTO Students VALUES(?,?, ?)", ("Tariq",1, "Kaleri"))
# cur.execute("alter table Students add column cast varchar(100)")
# cur.execute("INSERT INTO Students VALUES(?,?)", ("Tariq",1))
# cur.execute("SELECT * FROM Students")
# for i in cur:
#     print(i)
# cur.execute("create table new (id int primary key not null, name text not null,age int not null)")
# cur.execute("INSERT INTO new VALUES(?,?,?)", (14, 'tariq', 20))
# cur.execute("update new set name='amir' where id=13")
# cur.execute("select id,name from new where id=14")
# for i in cur:
#     print(i)
# con.commit()
# con.close()# con = connect("test.db")
# cur = con.cursor()
# cur.execute("create table member (id int primary key, name varchar not null, price int default 0)")
# cur.execute("CREATE TABLE Students (Name text, RollNo real)")
# cur.execute("alter table Students add column cast varchar(100)")
# cur.execute("INSERT INTO Students VALUES(?,?, ?)", ("Tariq",1, "Kaleri"))
# cur.execute("alter table Students add column cast varchar(100)")
# cur.execute("INSERT INTO Students VALUES(?,?)", ("Tariq",1))
# cur.execute("SELECT * FROM Students")
# for i in cur:
#     print(i)
# cur.execute("create table new (id int primary key not null, name text not null,age int not null)")
# cur.execute("INSERT INTO new VALUES(?,?,?)", (14, 'tariq', 20))
# cur.execute("update new set name='amir' where id=13")
# cur.execute("select id,name from new where id=14")
# for i in cur:
#     print(i)
# con.commit()
# con.close()




# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def grade_name(self):
#         return self.grade
# std1 = Student("Tariq", 12, 80)
# std2 = Student("Ertugrul", 12, 85)
# std3 = Student("Kurdugulu", 12, 86)
# print(std1.grade_name())
# add = 0
# class Courses:
#     def __init__(self, name, max_std):
#         self.name = name
#         self.max_std = max_std
#         self.students = []
#
#
#     def add_std(self, std_grade):
#         global add
#         if len(self.students) < self.max_std:
#             add += std_grade
#             self.students.append(std_grade)
#             print(f"{std_grade} is Added")
#         else:
#             avg = add/self.max_std
#             print(avg)
# course = Courses("OOP", 3)
# course.add_std(std1.grade)
# course.add_std(std2.grade)
# course.add_std(std3.grade)
# course.add_std(std2.grade)







# class Bank():
#     def __init__(self, bank_name, emp_name, pos_name):
#         self.bank_name = bank_name
#         self.emp_name = pos_name
#         self.pos_name = pos_name
#         self.amount = 0
#     def deposit_amount(self, dep_amount):
#         self.amount += dep_amount
#         return self.amount
#     def withdrawamount(self, w_d_a):
#         if w_d_a <= self.amount:
#             self.amount = self.amount - w_d_a
#             print(f"Take your Amount {w_d_a}--Now Your Total Balance is {self.amount}")
#         else:
#             print("You don't have sufficient balance")
#     def check_balance(self):
#        print(f"Your Total AMount is {self.amount}")
# Tariq = Bank("Sindh Bank", "Tariq", "Programmer")
# Tariq.deposit_amount(12000)
# Tariq.withdrawamount(3000)
# Tariq.check_balance()


