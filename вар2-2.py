strok=str(input("\nВведите строку "))
m=strok.split(' ')
for i in range(len(m)):
    if i%2!=1:
        print(m[i])
        
