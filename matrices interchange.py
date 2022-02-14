# All matrices interchange handler

# A = []
# B = []
# nc = 3
# nr = 3
# r = 0
# while r < nr:
#     R = []
#     c = 0
#     while c < nc:
#         inp = int(input("Enter the number: "))
#         R.append(inp)
#         c += 1
#     r += 1
#     # B.append(R)
#     A.append(R)
#     B.append(R)
# # B = A.copy()
# #  it works successfully
# A[0] = B[1]
# A[1] = B[0]
# print(A)




# #it doesn't work right way
# i = 0
# j = 0
# k = 1
# while i < nr:
#     A[j][i] = B[k][i]
#     i += 1
# i = 0
# j = 0
# k = 1
# while i < nr:
#     A[k][i] = B[j][i]
#     i += 1
# print(A)




# #it also works successfully
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# i = 0
# j = 0
# k = 1
# while i < 3:
#     A[j][i] = B[k][i]
#     i += 1
# i = 0
# j = 0
# k = 1
# while i < 3:
#     A[k][i] = B[j][i]
#     i += 1
# print(A)



# # substract constant number from R1
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# const = 1
# i = 1
# for j in range(3):
#     A[i][j] = A[i][j] - const
# print(A)

# def const_minus(nra, nca):
#     main_matrix = []
#     main_matrix1 = []
#     for rows in range(nra):
#         R = []
#         for j in range(nca):
#             inp = int(input("Enter: "))
#             R.append(inp)
#         main_matrix.append(R)
#         main_matrix1.append(R)
#     main_matrix[0] = main_matrix1[1]
#     main_matrix[1] = main_matrix1[0]
#     const = 2
#     j = 0
#     k = 1
#     for i in range(nra):
#         main_matrix[k][i] = main_matrix[k][i] - main_matrix[j][i]*3
#     return main_matrix
# C = const_minus(3,3)
# print(C)






