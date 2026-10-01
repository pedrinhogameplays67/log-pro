numero = []

for i in range(0, 10):
    numeros = int(input('Digite os números: '))
    numero.append(numeros)

print(f'O maior número é {max(numero)} e o menor \
número é {min(numero)}')

print(f'A posição do maior número é: {numero.index(min(numero))} \
e do menor número é: {(numero.index(max(numero)))}')

