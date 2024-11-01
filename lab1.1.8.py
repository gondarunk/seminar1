import matplotlib.pyplot as plt
import numpy as np
nl1=[0.4,0.8,1.2,1.6,2.0]
time1=[0.117,0.207,0.283,0.350,0.410]
nl1t=[]
y=[]
for i in range (len(nl1)):
    nl1t.append(nl1[i]/(time1[i]))
plt.xlabel('time, s')
plt.ylabel('nl/t')
a, b = np.polyfit(time1, nl1t, 1)
for i in range(len(time1)):
    y.append(a*time1[i]+b)
plt.plot(time1, y, '-')
plt.title('first line')
plt.plot(time1, nl1t, 'o')
print(a)
print(b)
plt.xlim(0, 0.5) # Ось X от 0 до 4
plt.ylim(0, 5) # Ось Y от 0 до 8

plt.grid()
plt.show()

