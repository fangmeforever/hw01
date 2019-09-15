i = 0
x=' '
for i in range(1, 10):
    print(x*10*(i-1),end="")
    for j in range(1, 10):
        if j >= i:
            print("%s×%s = %2s" % (i,j ,i*j ),end="  ")
    i += 1
    print ("\n")