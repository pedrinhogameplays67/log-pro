nota1 = float(input('Digite a nota do primeiro bimestre: '))
recuperacao1 = float(input('Digite a nota da recuperação do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
recuperacao2 = float(input('Digite a nota da recuperação do segundo bimestre: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
recuperacao3 = float(input('Digite a nota da recuperação do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))
recuperacao4 = float(input('Digite a nota da recuperação do quarto bimestre: '))
recuperacao = print('Recuperação')
resultado_final = print(f'{nota1 + nota2 + nota3 + nota4}')
if 0 > nota1 < 6.9:
    print(f'{recuperacao}')
    if recuperacao:
        print(f'{recuperacao1}')
        if recuperacao1 + nota1 >= 7.0 < 10.0:
            print('Você passou de bimestre')
        elif 7.0 > nota1 < 10.0:
            print('Você passou de bimestre')


if 0 > nota2 < 6.9:
    print(f'{recuperacao}')
    if recuperacao:
        print(f'{recuperacao2}')
        if recuperacao2 + nota2 >= 7.0 < 10.0:
            print('Você passou de bimestre')
        elif 7.0 > nota2 < 10.0:
            print('Você passou de bimestre')

if 0 > nota3 < 6.9:
    print(f'{recuperacao}')
    if recuperacao:
        print(f'{recuperacao2}')
        if recuperacao3 + nota3 >= 7.0 < 10.0:
            print('Você passou de bimestre')
        elif 7.0 > nota3 < 10.0:
            print('Você passou de bimestre')

if nota1 + nota2 + nota3 / 3 >= 21:
    print('Você passou de ano!')
    

    if 0 > nota4 < 6.9:
        print(f'{recuperacao}')
        if recuperacao:
            print(f'{recuperacao1}')
            if recuperacao4 + nota4 >= 7.0 < 10.0:
                print('Você passou de bimestre')
            elif 7.0 > nota4 < 10.0:
                print('Você passou de bimestre')


