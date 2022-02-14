a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
x = a
fa = x**2 + 3*x - 10
x = b
fb = x**2 + 3*x - 10
f = fa * fb
if f > 0:
    print("Given values don't have solution lies")
else:
    fc = 1
    k = 1
    while fc != 0:
        c = (a + b)/2
        x = c
        fc = x ** 2 + 3 * x - 10
        f = fa * fc
        print("a = {}     b = {}    c = {}      k = {}".format(a, b, c, k))
        k += 1
        if f < 0:
            b = c
        else:
            a = c
print("solution of given equation is {}".format(c))