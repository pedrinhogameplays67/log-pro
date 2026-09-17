from time import sleep

print('Olá aluno desgraçado, sua média até o 3° bimestre' \
' precisa ser maior ou igual a 8, caso contrario você terá que fazer o 4° bimestre.' \
' Caso você for fazer o 4° bimestre sua média total precisa ser 6.')

sleep (4.0)

nota1 = float(input('Digite a nota do primeiro bimestre: '))
if nota1 >= 8.0:
    print('Você passou de bimestre')
else:
    print('KKKKKKKKKKKK animal')
    sleep (0.8)
    recuperacao1 = float(input('Digite a nota da recuperação do primeiro bimestre: '))

    if (recuperacao1 + nota1) / 2 >= 8.0:
        print('Você passou de bimestre')
sleep (1.0)

nota2 = float(input('Digite a nota do segundo bimestre: '))
if nota2 >= 8:
    print('Você passou de bimestre')
else:
    print('KKKKKKKKKKKKK vc é mt burro')
    sleep (0.8)    
    recuperacao2 = float(input('Digite a nota da recuperação do segundo bimestre: '))

    if (recuperacao2 + nota2) /2 >= 8.0:
            print('Você passou de bimestre')
sleep (1.0)

nota3 = float(input('Digite a nota do terceiro bimestre: '))
if nota3 >= 8:
    print('Você passou de bimestre')
else:
    print('KKKKKKKKKKKKK decepção da familia')
    sleep (0.8)    
    recuperacao3 = float(input('Digite a nota da recuperação do terceiro bimestre: '))

    if (recuperacao3 + nota3) /2 >= 8.0:
            print('Você passou de bimestre')
sleep (1.0)

resultado_final = nota1 + nota2 + nota3
if resultado_final >= 21:
    print('Você passou de ano!')
sleep (1.0)

resultado_final = nota1 + nota2 + nota3
if nota1 + nota2 + nota3 / 3 < 21:
    print('Você precisa fazer o 4° bimestre. sua nota é ' f'{resultado_final}')
    nota4 = float(input('Digite a nota do quarto bimestre: '))
    if (nota4 + nota1 + nota2 + nota3) / 4 < 24:
        print('isso nao é possivel KKKKKKKKKKKKKK')
        recuperacao4 = float(input('Digite a nota da recuperação do quarto bimestre: '))
        print(recuperacao4)
        resultado_final = nota1 + nota2 + nota3 / 3
        resultado_final_4 = nota4 + recuperacao4 / 2
        resultado_final_total_c_4 = resultado_final_4 + resultado_final / 2
        if resultado_final_total_c_4 >= 24:
            print('Você passou de ano! Sua nota é ' f'{resultado_final_total_c_4}')
        else:
            print('Um jegue consegue ser mais inteligente que vc, você reprovou de ano KKKKKKKKKKKKK')


# if 0 > nota1 < 6.9:
#     print(f'{recuperacao}')
#     if recuperacao:
#         print(f'{recuperacao1}')
#         if recuperacao1 + nota1 >= 8.0 < 10.0:
#             print('Você passou de bimestre')
#         elif 8.0 > nota1 < 10.0:
#             print('Você passou de bimestre')


# if 0 > nota2 < 6.9:
#     print(f'{recuperacao}')
#     if recuperacao:
#         print(f'{recuperacao2}')
#         if recuperacao2 + nota2 >= 8.0 < 10.0:
#             print('Você passou de bimestre')
#         elif 8.0 > nota2 < 10.0:
#             print('Você passou de bimestre')

# if 0 > nota3 < 6.9:
#     print(f'{recuperacao}')
#     if recuperacao:
#         print(f'{recuperacao2}')
#         if recuperacao3 + nota3 >= 8.0 < 10.0:
#             print('Você passou de bimestre')
#         elif 8.0 > nota3 < 10.0:
#             print('Você passou de bimestre')

# if resultado_final >= 21:
#     print('Você passou de ano!')

# # 4° bimestre caso precise de nota

# if nota1 + nota2 + nota3 / 3 < 21:
#     print(nota4)
#     if nota4 + nota1 + nota2 + nota3 / 4 < 21:
#         print(recuperacao4)
#         if resultado_final_total_c_4 <= 21:
#             print('Você passou de ano! ')
#         else:
#             print('Você reprovou de ano KKKKKKK')