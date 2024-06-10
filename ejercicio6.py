asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

suspendidas = []

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    if nota < 5:
        suspendidas.append(asignatura)

if suspendidas:
    print("Debes repetir las siguientes asignaturas:")
    for asignatura in suspendidas:
        print(asignatura)
else:
    print("No has suspendido ninguna, no tienes que recuperar.")