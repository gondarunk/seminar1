import numpy as np
import matplotlib.pyplot as plt

# Данные для аппроксимации
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 6])

# Вычисление коэффициентов прямой по МНК
a, b = np.polyfit(x, y, 1)

# Построение графика
plt.plot(x, y, 'o', label='Данные')
plt.plot(x, a * x + b, '-', label='Аппроксимированная прямая')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Аппроксимация прямой методом наименьших квадратов')
plt.legend()
print(a)
print(b)
plt.show()