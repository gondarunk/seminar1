a, b = (int(i) for i in input().split())
def nod(a,b):
    c=min(a,b)
    for i in range (c):
        if i!=0 and a%i==0 and b%i==0:
            h=i
    return h
d=nod(a,b)
a1=a//d
b1=b//d
y=0
if a!=b:
    while (((1 - b1 * y) % a1) != 0):
        y += 1

    x = (1 - b1 * y) // a1
    print(x, y, d)
else:
    print(0,1,a)

