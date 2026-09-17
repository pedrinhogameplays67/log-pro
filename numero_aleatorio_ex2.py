import random
from time import sleep



pontuacao = 0



for rodada in range(0, 3):
    print(f'Rodada {rodada + 1}')
    randmachine = random.randint(0, 51)
    numero_aleatorio = int(input('Adivinhe um número entre 0 e 50: '))
    for i in range (0, 4):
        if numero_aleatorio == randmachine:
            print('Você acertou o número')
            if i == 0:
                print('100 pontos na 1° tentativa!')
                pontuacao += 100
            elif i == 1:
                print('75 pontos na 2° tentativa!')
                pontuacao += 75
            elif i == 2:
                print('50 pontos na 3° tentativa!')
                pontuacao += 50
            elif i == 3:
                print('25 pontos na 4° tentativa')
                pontuacao += 25
            elif i == 4:
                print('10 pontos na 5° tentativa')
                pontuacao += 10

            else:
                print(f'Você não acertou, o número é {randmachine} ')
            break
        elif numero_aleatorio > randmachine:
            palpite_maior = print('Seu palpite foi maior que o número secreto. ')
            palpite_maior
        elif numero_aleatorio < randmachine:
            palpite_menor = print('Seu palpite foi menor que o número secreto. ')
            palpite_menor

        numero_aleatorio = int(input('Adivinhe um número entre 0 e 50: '))

print(f'Sua pontuação final é: {pontuacao}')