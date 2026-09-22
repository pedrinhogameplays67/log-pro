lista = []

carros = ['Ferrari F430 Spider', 'Monza Tubarão',
'Golf Sapão', 'Uno com Escada', 'Opala SS Beberrão',
'New civic', ]

# slice
dois_carros = carros[0:2]
print(dois_carros)

# adicionar na lista (no final da lista)
carros.append('Celta Preta')
print(carros)

print(30* '-')

# retira do fim da lista
# em python, aceita parametro (pode tirar de qualquer lugar)
carros.pop()
print(carros)

# New Civic
carros[5]

# Fim da lista - nesse '-1' mostra a ultima posição
carros[-1]

# penultima
carros[-2]

# verificar tipo
# print(type(carros))

# imprimir 1 elemento
# print(carros[4])




# 
# for carro in carros;
#   print('f{carro}')

# for i in range(len(carros)):
#     print(f'{i+1} - {carros[i]}')


# notas = [10, 5, 9.5, 7, 4.5, 1, 0]

# for nota in notas:
#     print(type(nota), nota)

# listas oidem ter qualquer coisa dentro delas
# sopa = [0, 1.2, 'a', 'E, aí?', True,
#         ['Mais uma lista']]
# for s in sopa:
#     print(type(s), s)

# lista pra cadastro
cadastro = ['Senai', 'eu@senai.br', '01/01/1900',
           'rua xavier, 417', '21 77777-7777']
print(carros[0])

