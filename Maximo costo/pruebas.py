def factorial(n):
    print(factorial(n))
    return 1 if n == 0 else factorial(n-1)*n
    

resultado = factorial(5)

print(resultado)