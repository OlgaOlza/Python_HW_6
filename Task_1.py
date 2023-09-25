# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

# Пример

# На входе:


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# # import random
# # number = int(input('Введите длину массива: '))
# # # min_number = int(input('Введите минимальное число: '))
# # # max_number = int(input('Введите максимальное число: '))
# # list1 = []
# for i in range(number+1):
#     i = random.randint(1,10)
#     list1.append(i)
# print(list1)
# for i in range(len(list1)):
#     if min_number <= list1[i] <= max_number:
#         print(f'Число которое входят в диапозон равно {list1[i]}. Индекс числа равен {i}')2
        
# # list_1 = [1, 3, 7, 10, 5, 8]
# list_2 = []
# # max_number = 8
# # min_number = 4
# for i in range(len(list_1)):
#     if list_1[i] >= min_number and list_1[i] <= max_number:
#         list_2.append(i)
# print(*list_2)

for i in range(len(list_1)):
  if min_number <= list_1[i] <= max_number:
    print(i)



