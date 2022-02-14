def matrixinput(no_of_rows, no_of_columns, message):
    A = []
    for i in range(no_of_rows):
        R = []
        for j in range(no_of_columns):
            inp = int(input("Enter the number" + message))
            R.append(inp)
        A.append(R)
    return A
def matrixadd():
    add = []
    for i in range(2):
        R = []
        for j in range(3):
            inp = A[i][j] + B[i][j]
            R.append(inp)
            print(inp, end="    ")
        add.append(R)
        print("\n")
    return add
matrixar, matrixac = int(input("Enter the number of rows A: ")), int(input("Enter the column of A: "))
matrixbr, matrixbc = int(input("Enter the number of rows B: ")), int(input("Enter the column of B: "))
if matrixar == matrixbr and matrixac == matrixbc:
    A = matrixinput(2, 3, " A: ")
    B = matrixinput(2, 3, " B: ")
    C = matrixadd()
    print(C)
else:
    print("Wrong input: ")