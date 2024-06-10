numeros = []
for i in range(8):
    numero = int(input("Introduce de uno en uno el numero ganador: "))
    numeros.append(numero)
numeros.sort()
print("Números ganadores ordenados de menor a mayor:", numeros)