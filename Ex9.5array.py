# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.

# lista = []
# for i in range(2):
#     nome = input('Digite o nome: ')
#     idade = int(input('Digite a idade: '))
#     lista.append([nome, idade])


# for i in range(0, len(lista)):

#     menor_idade = min(lista)

#     if menor_idade:
#         print(menor_idade)

# JEITO CERTO

lista = []
for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    lista.append ([nome, idade])


# Forma 1 -> Usar o indice (0 mais novo esta no inicio da lista)
mais_novo = 0 # indice
# [['eu', 50], ['tu', 70]]
#  o loop inicia do proximo elemento
for i in range (1, len(lista)):
    if lista [i][1] < lista[mais_novo][1]:
        mais_novo = i
        print(f'Era, então a posição do mais novo na lista é: {i}\n')


print (f'\n\n\nO usuário mais novo é: {lista[mais_novo][0]}')

# Forma 2 -> agora com função (min)
# [['Alfredo', 35], ['labubu', 5]]
mais_novo = min(lista, key=lambda pessoa: pessoa[1])
print(f'O usuário mais novo é: {mais_novo[0]}')

