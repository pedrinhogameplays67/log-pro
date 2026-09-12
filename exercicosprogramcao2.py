# média de 2 números
# float pq pode ter vírgula
# int seria se apenas tivesse numero inteiro

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print((nota1 + nota2) / 2)

if ((nota1 + nota2) / 2) >= 6:
    print('Aprovado')
else:
    print('Reprovado')

# outra forma de fazer

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))

# media = (nota1 + nota2) /2


# if media < 6:
#     print("Aluno Reprovado")
# else:
#     print('Aluno Aprovado')