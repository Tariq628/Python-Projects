dict1 = {"x":4, "y":2, "z":3}
dict2 = {"x":5, "y":7, "z":8, "a":10}
# print(dict2 | dict1) #same keys always overwite by 1st write variable in printstatement(here is dict2) keys
# print(dict1 | dict2) #same keys always overwite by 1st write variable in printstatement(here is dict1) keys
dict2 |= dict1 #alternate of dict1 | dict2
print(dict2)