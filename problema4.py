# Problema 4:
# Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
# pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
# materias.
# Puede usar el siguiente esquema a manera de ejemplo
# {
# Alumno: Juan,
# Notas: [10, 12, 15]
# }
# Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
# completo de los alumnos.
# Nota:
# El uso de listas con diccionarios le será de utilidad.

alumnos = []

print("Sistema de Registro de Alumnos")
print("------------------------------")

# solicita el numero de alumnos a registrar
cantidad = int(input("¿Cuántos alumnos quiere registrar? "))

# Registrar cada alumno
for i in range(cantidad):
    print(f"\nAlumno {i+1}:")
    nombre = input("Nombre del alumno: ")
    
    # Pedir las 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)
    
    # Guardar al alumno en la lista
    alumnos.append({
        "Alumno": nombre,
        "Notas": notas
    })

# Mostrar todos los alumnos registrados
print("\nLista completa de alumnos:")
print("-------------------------")
for alumno in alumnos:
    print(f"Nombre: {alumno['Alumno']} - Notas: {alumno['Notas']}")