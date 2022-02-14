def matrixinput(no_of_rows, no_of_columns, display = "A: "):
    A = []
    for i in range(no_of_rows):
        R = []
        for i in range(no_of_columns):
            inpA = int(input("Enter the number " + display))
            R.append(inpA)
        A.append(R)
    return A
# def multiply(nra, nrb):
#     C = []
#     for i in range(nra):
#         R = []
#         for j in range(nra):
#             s = 0
#             for k in range(nrb):
#                 inp3 = A[i][k] * B[k][j]
#                 s += inp3
#             R.append(s)
#         C.append(R)
#     return C
def multiply(nra, nrb):
    main_matrix = []
    for i in range(nra):
        R = []
        for j in range(nra):
            s = 0
            for k in range(nrb):
                inp = A[i][k] * B[k][j]
                s = s + inp
            R.append(s)
        main_matrix.append(R)
    return main_matrix

# if nca != nrb or nra != ncb:
#     print("Wrong Input: ")
#
# else:
A = matrixinput(2, 3, "A: ")

B = matrixinput(3, 2, "B: ")

C = multiply(2, 3)

print(C)