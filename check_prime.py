check = 9
for i in range(1,check+1, 2):
    if i > 1:
        bolean = True
        for j in range(2, i):
            if i % j == 0:
                bolean = False
                break
        if bolean:
            print(i, "is Prime")