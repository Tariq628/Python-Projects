f = open(r"file.txt", "r")
a = f.read()
print(a)
dict = {}
for i in a:
    if i in dict:
        dict[i] += 1
    if i not in dict and i != " ":
        dict[i] = 1
print(dict)
f.close()



# Other method
str1 = "GeeksForGeeks"
dict = {}
for i in str1:
    # print(i)
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)