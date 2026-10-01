numero = []


for i in range(0, 8):
    oito_n = int(input('Digite os números: '))
    numero.append(oito_n)

num_add = int(input('Adicione mais um número: '))

for i in range (0, len(numero)):
    if num_add == numero[i]:
        print(f'O número {num_add} já está na lista na posição {i + 1}')
