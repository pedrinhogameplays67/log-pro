# três números e fale o maior
# int/float funcionaria de qualquer maneira

# numero1 = int(input('Digite o primeiro numero: '))
# numero2 = int(input('Digite o segundo numero: '))
# numero3 = int(input('Digite o segundo numero: '))

# if numero1 > numero2:
#     if numero1 > numero3:
#         print('O primeiro numero é o maior')

# if numero2 > numero3:
#     if numero2 > numero1:
#         print('O segundo numero é o maior')

# if numero3 > numero2:
#     if numero3 > numero1:
#         print('O terceiro numero é o maior')

# OUTRA FORMA

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))

if numero1 > numero2 and numero3 < numero1:
    print(numero1,('é o maior'))

elif numero2 > numero3:
    print(numero2,('é o maior'))

else:
    print(numero3,('é o maior'))




# OUTRA FORMA


# def calcular_maior():
#     conta = []
#     i = int(input("Digite quantidade de vezes que você: "))

#     for x in range(i):
#         n1 = int(input(f"Digite número{x+1}: "))
#         conta.append(n1)


#     print(f"Esse número e o maior {max(conta)}!")


# calcular_maior()
