# Construa um jogo de pedra, papel e tesoura.

jogador1 = input('Jogador 1 escolha sua mão: Pedra, Papel ou Tesoura: ')
jogador2 = input('Jogador 2 escolha sua mão: Pedra, Papel ou Tesoura: ')

# primeiro bloco -> jogado1 == pedra
if(jogador1 == 'Pedra'):
    if (jogador2 == 'Pedra'):
        print('Empate')
    if(jogador2 == 'Papel'):
        print('Jogador 2 Ganhou')
    if(jogador2 == 'Tesoura'):
        print('Jogador 1 Ganhou')

if(jogador1 == 'Papel'):
    if (jogador2 == 'Pedra'):
        print('Jogador 1 Ganhou')
    if(jogador2 == 'Papel'):
        print('Empate')
    if(jogador2 == 'Tesoura'):
        print('Jogador 2 Ganhou')

if(jogador1 == 'Tesoura'):
    if (jogador2 == 'Pedra'):
        print('Jogador 2 Ganhou')
    if(jogador2 == 'Papel'):
        print('Jogador 1 Ganhou')
    if(jogador2 == 'Tesoura'):
        print('Empate')


# OUTRA FORMA

jogador1 = input('Jogador 1 escolha sua mão: Pedra, Papel ou Tesoura: ')
jogador2 = input('Jogador 2 escolha sua mão: Pedra, Papel ou Tesoura: ')

if jogador1 == jogador2:
    print('Empate')
# quando o jogador1 ganha?
# (Papel, Pedra), (Pedra, Tesoura), (Tesoura, Papel)
if( (jogador1 == 'Papel' and jogador2 == 'Pedra')
   or (jogador1 == 'Pedra' and jogador2 == 'Tesoura')
   or (jogador1 == 'Tesoura' and jogador2 == 'Papel')
):
    print('O Jogador 1 Ganhou')
# else -> jogador 2 ganhou
else:
    print('O jogador 2 Ganhou')

