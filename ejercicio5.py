'''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numeros[-i],end="")'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
for numero in numeros:
    print(numero, end=" ")
