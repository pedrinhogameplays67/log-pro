# Construa um programa onde o usuário digitará
# dez números. O programa deverá calcular quantos 
# deles são maiores que dez.

numeros = []

for i in range(0, 3):
    numero = float(input('Digite  um número: '))
    numeros.append(numero)
contador = 0
for numero in numeros:
    if numero > 10:
        contador += 1
print(contador)

