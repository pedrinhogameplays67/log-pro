numeros = []
for i in range(0, 10):

    numero = int(input('Digite os números: '))
    numeros.append(numero)


for numero in numeros:
    if numero < 0:
        index = numeros.index(numero)
        numeros.remove(numero)
        numeros.insert(index, 0)
print(numeros)



# OUTRA FORMA DE FAZER
# ===========================================================

# numeros = []

# for i in range(0, 10):
#     numero = int(input('Digite um número: '))
#     numeros.append(numero)

# print(numeros)

# for i in range(0, len(numeros)):
#     if numeros[i] < 0:
#         numeros.remove(numeros[i])
#         numeros.insert(i, 0)

# print(numeros)

