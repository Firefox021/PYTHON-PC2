# Problema 7:
# Escriba una función de Python que tome un número como parámetro y verifique que el número sea
# primo o no.

def es_primo(numero):
    # Si el número es menor o igual a 1, no es primo
    if numero <= 1:
        return False
    # Si el número es 2, es primo (el único par primo)
    elif numero == 2:
        return True
    # Si el número es par y mayor que 2, no es primo
    elif numero % 2 == 0:
        return False
    else:
        # Verificar divisores impares desde 3 hasta la mitad del número
        for divisor in range(3, (numero // 2) + 1, 2):
            if numero % divisor == 0:
                return False
        # Si no se encontraron divisores, es primo
        return True
num = int(input("Ingrese un número: "))

if es_primo(num):
    print(f"El número {num} **es primo**.")
else:
    print(f"El número {num} **no es primo**.")