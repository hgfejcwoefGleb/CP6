N = int(input("Введите количество элементов массива: "))
D = [0]*N
from random import randint
for i in range(N): 
  D[i]  = randint(1, 100)
print("Заданный массив", D) 
print("Максимальное значаение = ", max(D))