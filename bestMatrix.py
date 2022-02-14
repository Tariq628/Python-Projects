print("We take 3 by 3 matrices only")
check = int(input("Press 1 for check Square 2 for Equal 3 for Null 4 for unit 5 for"
                  "Symmetric 6 for scalar 7 for Diagonal 8 for Identity 9 for Inverse 10 for dimension of \n multiplication  matrix 11 for dimension of sum matrix"
                  " : "))
if check != 10 and check != 11:
    no_of_rows = int(input("Enter the no.of rows: "))
    no_of_columns = int(input("Enter the no.of columns: "))
if check != 1 and check != 10 and check != 11:
    A = []
    for i in range(no_of_rows):
        R = []
        for j in range(no_of_columns):
            inp = int(input("Enter the number A: "))
            R.append(inp)
        print()
        A.append(R)
    print(A)
#
#
if check == 1:
    if no_of_rows == no_of_columns:
        print("Yes-- It's an Square Matrix")
    else:
        print("Not a Square")


elif check == 2:
    B = []
    for i in range(no_of_rows):
        S = []
        for j in range(no_of_columns):
            inp = int(input("Enter the number B: "))
            S.append(inp)
        B.append(S)
    if A[0] == B[0] and A[1] == B[1] and A[2] == B[2]:
        print("Yes-- A and B are equal matrices")
    else:
        print("Not A equal")
#
#
if check == 3:
    for i in range(3):
        sum = 0
        for j in range(3):
            inp = A[i][j]
            sum += inp
    if sum == 0:
        print("Yes it's null")
    else:
        print("Not a null")



if check == 4:
    if A[0][1] == 0 and A[0][2] == 0 and A[1][0] == 0 and A[1][2] == 0 and A[2][0] == 0 and A[2][1] == 0 and A[0][0] == 1 and A[1][1] == 1 and A[2][2] == 1:
        print("Yes-- it's unit matrix")
    else:
        print("Not a Unit")





if check == 5:
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    S = []
    for i in range(3):
        T = []
        for j in range(3):
            inp = B[i][j] = A[j][i]
            T.append(inp)
        S.append(T)
    print(S)
    print()

    for i in range(3):
        for j in range(3):
            print(S[i][j], end="    ")
        print("\n")


if check == 6:
    if A[0][1] == 0 and A[0][2] == 0 and A[1][0] == 0 and A[1][2] == 0 and A[2][0] == 0 and A[2][1] == 0 and A[0][0] == A[1][1] == A[2][2]:
        print("Yes-- It's Scalar Matrix")
    else:
        print("Not a Scalar matrix")


if check == 7:
    if A[0][1] == 0 and A[0][2] == 0 and A[1][0] == 0 and A[1][2] == 0 and A[2][0] == 0 and A[2][1] == 0:
        print("Yes-- It's Diagonal Matrix")
    else:
        print("Not a Diagonal matrix")


if check == 8:
    if A[0][1] == 0 and A[0][2] == 0 and A[1][0] == 0 and A[1][2] == 0 and A[2][0] == 0 and A[2][1] == 0 and A[0][0] == 1 and A[1][1] == 1 and A[2][2] == 1:
        print("Yes-- it's Identity matrix")
    else:
        print("Not an Identity")


if check == 10:
    no_of_rows_A = int(input("Enter the no.of rows A : "))
    no_of_columns_A = int(input("Enter the no.of columns A : "))
    no_of_rows_B = int(input("Enter the no.of rows B : "))
    no_of_columns_B = int(input("Enter the no.of columns B : "))
    if no_of_rows_A == no_of_columns_B and no_of_columns_A == no_of_rows_B:
        print("Yes Dimension Of Multiplication is Right")
    else:
        print("No Dimension Of Multiplication is Wrong")




if check == 11:
    no_of_rows_A = int(input("Enter the no.of rows A : "))
    no_of_columns_A = int(input("Enter the no.of columns A : "))
    no_of_rows_B = int(input("Enter the no.of rows B : "))
    no_of_columns_B = int(input("Enter the no.of columns B : "))
    if no_of_rows_A == no_of_rows_B and no_of_columns_A == no_of_columns_B:
        print("Yes Dimension Of Sum of Matrix is Right")
    else:
        print("No Dimension Of Sum of Matrix is Wrong")