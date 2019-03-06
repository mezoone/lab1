a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
k=int(input('k='))
if a*b==0:
    x='нет решения'
else:
    x=abs((((a**2)-(b**3)-(c**3)*(a**2))*(b-c+c*(k-(d/b**3)))-((k/b-k/a)*c)**2)-20000)
print('x = ',x)
