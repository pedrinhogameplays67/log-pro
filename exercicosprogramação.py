# três números e fale o maior

numero1 = int(input('Digite o primeiro numer: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    if numero1 > numero3:
        print(numero1)

if numero2 > numero3:
    if numero2 > numero1:
        print(numero2)

if numero3 > numero2:
    if numero3 > numero1:
        print(numero3)

