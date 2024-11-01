import numpy as np
n, m = (int(i) for i in input().split())
mat = np.zeros((n,m))
x,y = 0, 0
mat[0][0]=1
k,l= 0,1
end = 2
while end <= n*m:
    if 0<=x+k<=n-1 and 0<=y+l<=m-1 and mat[x+k][y+l] == 0:
        mat[x + k][y + l]=end
        end+=1
        x=x+k
        y=y+l
    elif l == 1:
         l=0
         k=1
    elif k == 1:
         k=0
         l=-1
    elif l == -1:
         l=0
         k=-1
    elif k==-1:
         k=0
         l=1
print(mat, end='\n''\n')

