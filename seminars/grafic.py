import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = [0,1,2,3,4]
y = [0,2,4,6,8]
#нарисуем график первой функции -- 2x
plt.figure(figsize=(8,5), dpi=100)
plt.plot(x,y, 'b^--', label='2x')
# figsize -- пропорции "поля" рисунка
#plt.figure(figsize=(8,5), dpi=100)
# С помощью numpy мы можем создавать массив из чисел с определенным интервалом функцией arange. np.linspace(..) делает то же самое, но с целыми числами
x2 = np.arange(0,4.5,0.05)
# Поскольку x2 -- массив numpy, мы можем это сделать просто "возведя в квадрат" массив
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')
# Подпишем оси
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Зададим какие-нибудь корявые "штрихи"/ticks на осях. в эти фунции можно передать любой список
plt.xticks([0,1.12,2.66,3,3.5])
plt.yticks([0,2,4,6,8,10])
plt.savefig('mygraph.png', dpi=300)
plt.show()

