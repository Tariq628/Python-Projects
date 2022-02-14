# class Employee():
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     @classmethod
#     def change_leaves(cls, newLeaves):
#         cls.no_of_leaves = newLeaves
# tariq = Employee("Tariq", 3000000, "Programmer")
# harry = Employee("Harry", 123, "Developer")
# Employee.change_leaves(123)
# print(tariq.no_of_leaves)



# def dec1(func1):
#     def nowexec():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexec
# @dec1
# def who_is_harry():
#     print("harry is a good boy")
# # after running nowexec will come in who_is_harry then we call
# # who_is_harry it's mean we call nowexec
#
# # who_is_harry = dec1(who_is_harry)
# who_is_harry()



# class Employee():
#     no_of_leaves = 8
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     @classmethod
#     def change_leaves(cls, newLeaves):
#         cls.no_of_leaves = newLeaves
#     @classmethod
#     def from_dash(cls, string):
#         print(string.split("-"))
#         print(*string.split("-"))
#         return cls(*string.split("-"))
# tariq = Employee("Tariq", 3000000, "Programmer")
# harry = Employee("Harry", 123, "Developer")
# umair = Employee.from_dash("Umair-20-A")
# print(umair.salary)
# umair.change_leaves(123)