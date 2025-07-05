# Problema 2:
# Escriba un programa en Python para construir el siguiente patrón.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(n):
    print('* ' * (i+1))
for i in range(n,0,-1):
    print('* ' * i)