# Problema 1:
# Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
# en el rango de 1500 y 2700 (ambos incluidos)

# Definimos el rango de números a analizar
inicio = 1500
fin = 2700

# Creamos una lista vacía para guardar los números que cumplen las condiciones
numeros_encontrados = []

# Recorremos todos los números en el rango especificado
for numero in range(inicio, fin + 1):
    # Verificamos si el número es divisible por 7 Y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_encontrados.append(numero)  # Añadimos el número a la lista

# Mostramos los resultados
print("Números entre 1500 y 2700 divisibles por 7 y múltiplos de 5:")
print(numeros_encontrados)