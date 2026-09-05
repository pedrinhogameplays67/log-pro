# programa de 3 números e dirá o maior

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

print((nota1 + nota2) / 2)

if ((nota1 + nota2) / 2) >= 6:
    print('Aprovado')
else:
    print('Reprovado')