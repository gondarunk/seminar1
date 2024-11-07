class Vector():
  def __init__(self, x,y,z):
      assert isinstance(x, float) and isinstance(y,float) and isinstance(z, float), "Координаты вектора должны быть числами"

      self.x=x
      self.y = y
      self.z = z
  def __add__(self, other):
      if isinstance(other, Vector):
          return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
      else:
          raise TypeError("Неверный тип данных")

  def __sub__(self,other):
      if isinstance(other, Vector):
          return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
      else:
          raise TypeError("Неверный тип данных")

  def abs(self):
      return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

  def __mul__(self, other):
      if isinstance(other, Vector):
          return self.x * other.x + self.y * other.y + self.z * other.z
      elif isinstance(other, (int, float)):
          return Vector(f"({self.x * other}, {self.y * other}, {self.z * other})")

      else:
          raise TypeError("Неверный тип данных")


v1=Vector(1.0,1.0,1.0)
v2=Vector(2.0,2.0,2.0)
v3=v1+v2
v4=v1-v2
print(f"v1 + v2: ({v3.x}, {v3.y}, {v3.z})")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: ({v4.x}, {v4.y}, {v4.z})")
print(f"Модуль {v1.abs()}")
print(f"Скалярное умножение v1*v2: {v1*v2} ")
print(f"v1*5.0: {v1*5} ")