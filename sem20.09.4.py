import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([2,3,4,5,6,7])
a=(np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
b = np.mean(y) - np.mean(x) * a
print(a)
print(b)
