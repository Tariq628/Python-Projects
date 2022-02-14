inp = int(input("Enter the number 1: "))
inp1 = int(input("Enter the number 2: "))
x = inp
fa = x**2 + 3*x - 10
print(fa)
x = inp1
fb = x**2 + 3*x - 10
print(fb)
f = fa * fb
if f > 0:
    print("Given Range Does not contain solution")
else:
    fc = 1
    while fc != 0:
        c = (inp + inp1)/2
        x = c
        fc = x**2 + 3*x - 10
        f = fa * fc
        if f < 0:
            inp1 = c
        else:
            inp = c
    print(c)



# Trapeoid method

# n = int(input('Enter no of trapeozoid: '))
# x0 = eval(input('Enter value of Xo: '))
# xn = eval(input(f'Enter value of X{n}: '))
# single_piece_of_x = (xn- x0) / n
# xi = x0
# f = 0
# for i in range(n):
#     if i == 0:
#         x = x0
#         fx0 = (x**3) / 3 + (3 * x ** 2) / 2  - 10 * x
#         f += fx0
#     elif i == (n-1):
#         x = xn
#         fxn = (x**3) / 3 + (3 * x ** 2) / 2  - 10 * x
#         f += fxn
#     else:
#         x = xi
#         fxi = (x**3) / 3 + (3 * x ** 2) / 2  - 10 * x
#         f += (fxi * 2)
#     xi += single_piece_of_x


# trapeozoid = ((xn - x0) / 2) * f

# print(trapeozoid)