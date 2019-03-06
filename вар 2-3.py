import random
n=int(input("\nВведите кол-во эл-ов списка "))
k=int(input("\nВведите диапазон эл-ов списка "))
summ=0
m=random.sample(range(k),n)
for i in range(n):
    if m[i]<=10 and m[i]>=1:
        summ+=m[i]
print(m)
print('\nСумма чисел от 1 до 10 =',summ)
