c=[]
def prime (d):
    r=0
    for i in range (d):
        if i!=0 and i!=1 and i!=d and d%i==0:
           r+=1
    if r>0:
        return 1
    else:
        return 0
def simp (a):
    for i in range (a):
     if  i!=0 and i!=1 and prime(i)==0 and a%i==0:
        c.append(i)
    return c
    
s=int(input())
l=simp(s)
print (l)


