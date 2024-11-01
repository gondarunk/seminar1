n, m = map(int, input().split())
a=[[0 for i in range(m)] for i in range (n)]
a[0][0]=1
for i in range (1,n):
    for j in range(1,m):
        if i-2>=0 and j-2>=0:
          a[i][j]=a[i-2][j-1]+a[i-1][j-2]
        elif i-2<0 and j-2>=0:
         a[i][j]=a[i-1][j-2]
        elif j - 2 < 0 and i - 2 >= 0:
            a[i][j] = a[i - 2][j - 1]
print(a[-1][-1])