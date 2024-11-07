a = int(input())
b=[]
t = 0
while a != 1:

    if (a % 2 == 0 or a % 3 == 0):
        if (((a - 1) % 9 == 0) and a % 16 != 0):
            a = (a - 1)//9
            b.append(a)
            t += 3
        else:
            if ((a - 1) % 32 == 0):
                a = (a - 1)//32
                b.append(a)
                t += 6
            if (a % 16 == 0):
                a = a//16
                b.append(a)
                t += 4
            if (a % 16 != 0 and a % 2 == 0):
                a = a//2
                b.append(a)
                t += 1
            if (a % 9 == 0 or a % 3 == 0):
                a = a//3
                b.append(a)
                t += 1
    else:
        if a != 1:
            a = a - 1
            b.append(a)
            t+= 1
        if a == 1:
            break
print(t)
c=b[::-1]
print(*c)