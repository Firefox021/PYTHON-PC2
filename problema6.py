# Problema 6:
# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
# Nota: La secuencia de Fibonacci es la serie de números:
# 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
# Cada número siguiente se obtiene sumando los dos números anteriore

def fibonacci_max(limite):
    # Inicializar los primeros dos números de la serie
    a, b = 0, 1
    serie = []
    
    while a <= limite:
        serie.append(a)
        # se calcula el siguiente número de la serie
        a, b = b, a + b
    
    return serie

# Llamamos a la función colocano el numero 50 como numer max quesolicitan
resultado = fibonacci_max(50)

print("Serie de Fibonacci entre 0 y 50:")
print(resultado)