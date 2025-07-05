# Problema 5:
# Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
# Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
# Ejemplo:
# Número ingresado: 15789000 y Dígito: 0
# Cantidad de veces 0 en el número: 4
# Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
# count.

def contar_digito(numero, digito):
    # Convertimos ambos a string para poder usar el método count
    str_numero = str(numero)
    str_digito = str(digito)
    
    # Usamos el método count para contar las ocurrencias
    return str_numero.count(str_digito)

# Ejemplo de uso
numero = 15789000
digito = 0
resultado = contar_digito(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {resultado}")