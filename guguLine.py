for a in range(2,10) :
    print("# %2d단 #" % a, end=" ")
print()

for b in range(2,10) :
    for a in range(2,10) :
        print(" %2d x %2d = %2d" %(a,b, a*b), end=" ")
    print()
    