arr = [170, 45, 755, 700, 802, 2433, 2, 66]
max_length = len(str(max(arr)))
print(max_length)


for i in range(len(arr)):
    arr[i] = str(arr[i]).zfill(max_length)


print(arr)
for digit_position in range(max_length):

    count = [0] * 10  
    output = [0] * len(arr)
    print(digit_position)


    for num in arr:
        digit = int(num[digit_position])
        # print(digit)
        count[digit] += 1
    print("bien")
    print(count)


    for i in range(1, 10):
        count[i] += count[i - 1]
    

    for i in range(len(arr) - 1, -1, -1):
        digit = int(arr[i][digit_position])
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    print(count)
    arr = output[:]

# Convierte los números ordenados de nuevo a enteros
arr = [int(num) for num in arr]



# Ejemplo de uso

print("Arreglo ordenado:")
print(arr)
