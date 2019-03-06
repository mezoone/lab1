import random
n=int(input("\nВведите кол-во эл-ов списка "))
k=int(input("\nВведите диапазон эл-ов списка "))
mass=random.sample(range(k),n)
minim=k+1
for i in range(n):
    if mass[i]<minim:
        minim=mass[i]
print(mass)
print('Минимальное число массива',minim)
