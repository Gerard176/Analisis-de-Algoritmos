def radix_sort_msd(arr):
    # Encuentra el número máximo para determinar el número de dígitos
    max_num = max(arr)
    exp = 1

    def counting_sort_msd(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    while max_num // exp > 0:
        counting_sort_msd(arr, exp)
        exp *= 10

# Ejemplo de uso:
arr = [170, 45, 75, 90, 802, 24, 2, 66, 12, 100]
radix_sort_msd(arr)
print("Array ordenado:", arr)