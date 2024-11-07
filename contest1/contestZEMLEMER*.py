n,m=map(int,input().split())
a=[[0 for i in range (m)] for i in range(n)]
b=[[0 for i in range (m)] for i in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
b[n-1]=a[n-1]
for i in range (n):
    b[i][m-1]=a[i][m-1]
for i in range (n-2,-1,-1):
    for j in range (m-2,-1,-1):
        if a[i][j]!=0:
          b[i][j]=min(b[i+1][j], b[i][j+1], b[i+1][j+1])+1
l=0
for i in range(n):
    for j in range(m):
        if b[i][j]>=l:
            l=b[i][j]
print(l)
