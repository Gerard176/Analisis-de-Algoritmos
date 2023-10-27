
a = 2600
print(a)
if a%4 == 0 and  a%100 != 0:
    print("es bisisesto")
elif a%100 == 0 and  a%400 != 0:
    print("no es bisisesto")
elif a%100 == 0 and a%400 == 0:
    print("es bisiesto")
else:
    print("no es bisisesto")    

array = []

for i in range(0,11):
    array.append(i)

print("pares")
for i in array:
    if i%2 == 0:
        print(array[i])
print("impares")    
for i in array:
    if i%2 != 0:
        print(array[i])
c = 1
sum = 0 
for i in array:
    
    if c == 5:
        sum += array[i]
    c+=1 