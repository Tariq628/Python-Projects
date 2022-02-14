# no_rows = int(input("How many rows you want: "))
# r = 0
# while r < no_rows:
#     r += 1
#     c = 0
#     no_col = r
#     while c < no_col:
#         print("*", end=" ")
#         c += 1
#     print()






# maxlines = 5
# l = 0
# while l < maxlines:
#     l += 1
#     r = 0
#     while r < maxlines - l:
#         print(" ", end="")
#         r += 1
#     s = 0
#     # maxstars = l
#     while s < l:
#         print("*", end="")
#         s += 1
#     print()





#                          """Pyramid"""

# num = int(input("Enter: "))
# for i in range(0, num):
#     for j in range(0, num - 1 - i):
#         print(" ", end="")
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print()



# num = int(input("Enter: "))
# for i in range(0, num):
#     for j in range(num, i, -1):
#         print("*", end="")
#     print()
#     for j in range(0, i + 1):
#         print(" ", end="")




# n = int(input("Enter the rows: "))
# i = 0
# while i < n:
#     j = n
#     while j > i:
#         print("*", end=" ")
#         j -= 1
#     print()
#     i += 1



# for i in range(4):
#     for j in range(4 , i, -1):
#         print("*", end=" ")
#     print()
#     for j in range(i + 1):
#         print(" ", end=" ")