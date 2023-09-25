# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n будет
# задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:


# a1 = 2
# d = 3
# n = 4
# На выходе:


# 2
# 5
# 8
# 11

a1 = int(input("Введите первое число : "))  # a
d = int(input("Введите разность: "))               # d
n = int(input("Введите количество элементов: "))             # n

for i in range(n):
  print(a1 + i * d)