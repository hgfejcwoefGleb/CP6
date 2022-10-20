N = int(input("Введите количество элементов массива: "))
D = [0]*N
from random import randint
for i in range(N): 
  D[i]  = randint(1, 100)
print(D) 
def maximus(D):
  a = D[0]
  for i in range(N):
    if a < D[i]:
      a = D[i]
  else: a=a
  return a
print("Максимальное значаение = ", maximus(D))