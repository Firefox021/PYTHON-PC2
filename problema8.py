# Problema 8:
# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
# función acepta el número como argumento.

def factorial(n):
    if n < 0:
        return "El factorial debe ser mayor a cero."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)