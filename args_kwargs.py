# def funargs(arg):
#     print(*arg)
# lst = ["tariq", "rizwan", 12]
# funargs(lst)
#
# def funargs(*args):
#     print(args)
# # if we will give tuple also pass as tuple
# lst = ["tariq", "rizwan", 12]
# funargs(*lst)
#
# def funargs(*args):
#     print(args)
# lst = ["tariq", "rizwan", 12]
# funargs(lst)



# def funargs(normal, *args, **kwargs):
#     print(normal)
#     for item in args:
#         print(item)
#     print("\nNow we have to introduce some our heroes")
#     for key, value in kwargs.items():
#         print(f"{key} is a {value}")
# nor = "I am a tariq and our favorite students are"
# ar = ["Tariq", "Umair", "Aaraf", "Ahmed", "Rizwan"]
# kw = {"Tariq":"Programmer", "Aaraf":"Ashiq", "Umair":"MLE"}
# # funargs(nor, *ar, **kw)
# funargs(nor, *ar, **kw)