
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "? ")
    notas.append(nota)
print("En", asignaturas, "has sacado", notas)
