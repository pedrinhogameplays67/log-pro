
numeros = []
contadorPar = 0
contadorImpar = 0

for i in range(0, 7):
    numero = float(input('Digite um número: '))
    numeros.append
    if numero % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1

print(f'{contadorPar} números são pares')
print(f'{contadorImpar} números são ímpares')