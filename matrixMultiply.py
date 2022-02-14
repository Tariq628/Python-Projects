def matrixinput(no_of_rows, no_of_columns, message):
    A = []
    for i in range(no_of_rows):
        R = []
        for j in range(no_of_columns):
            inp = int(input("Enter the number" + message))
            R.append(inp)
        A.append(R)
    return A
def matrixmultiply():
    C = []
    for i in range(2):
        D = []
        for j in range(2):
            sum = 0
            for k in range(3):
                multiply = A[i][k] * B[k][j]
                sum += multiply
            D.append(sum)
            print(sum, end="    ")
        C.append(D)
        print("\n")
    return C

matrixar, matrixac = int(input("Enter the number of rows A: ")), int(input("Enter the column of A: "))
matrixbr, matrixbc = int(input("Enter the number of rows B: ")), int(input("Enter the column of B: "))
if matrixar == matrixbc and matrixac == matrixbr:
    A = matrixinput(2, 3, " A: ")

    B = matrixinput(3, 2, " B: ")

    C = matrixmultiply()
    print(C)
else:
    print("Wrong Input---")