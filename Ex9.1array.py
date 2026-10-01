numeros = []
print('Você irá digitar 10 números que serão colocados em uma lista.')

# for i in range(0, 10):
#     numero = float(input('Digite um número: '))
#     numeros.append(numero)

# contador = 0
# for numero in numeros:
#     if numero > 10:
#         print(numero)
# print(contador)

# versão recomendada
# versão 2 -> quantos são
# contador = 0
# for i in range(0, 3):
#     numero = float(input('Digite um numero: '))
#     if numero > 10:
#         contador += 1


# versão 3 -> utilizar lista e guardar os maiores
lista = []
for i in range(0, 3):
    numero = float(input('Digite um numero: '))
    if numero > 10:
        lista.append(numero)

print(len(lista))

maiores_que_10 = (
    [numero for numero in lista if numero > 10]
)

print(maiores_que_10)

