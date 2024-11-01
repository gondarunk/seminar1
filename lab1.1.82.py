import matplotlib.pyplot as plt
import numpy as np
nl1=[0.4,0.8,1.2,1.6,2.0]
time1=[0.11746,0.20709,0.28347,0.35083,0.41096]
nl1t=[]
for i in range (len(nl1)):
    nl1t.append(nl1[i]/(time1[i]))
plt.xlabel('time, s')
plt.ylabel('nl/t')
a, b = np.polyfit(time1, nl1t, 1)
plt.plot(time1, nl1t, 'o')
y=[]
for i in range(len(time1)):
    y.append(a*time1[i]+b)
plt.plot(time1, y, '-')
plt.title('8 line')
print(a)
plt.xlim(0, 0.5) # Ось X от 0 до 0.5
plt.ylim(0, 5) # Ось Y от 0 до 5
plt.grid()
plt.show()
