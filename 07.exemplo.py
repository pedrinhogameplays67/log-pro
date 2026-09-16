from time import sleep

# pq o from time import? pq eu vou puxar da biblioteca time uma função (def)


while True:
# while serve pra usar como enquanto, enquanto nao estiver certa continue

    senha = int(input("Digite a senha correta: "))
    if senha == 67:
        print('\033[32mSenha correta\033[0m')
        break
# break para o programa caso esteja correto
    else:
        print('Senha incorreta')
        sleep (0.9)
        n = input('Deseja continuar? ')
        if n != 'sim':
            break
            
# sleep é usado pra dar um tempo a cada mensagem, ou seja, a cada senha incorreta, ele espera 0.9 seg e continua
# eu poderia usar o return, mas só é usado dentro de função (def)
            
# continue é usado pra continuar o programa caso esteja certo (senha incorreta) nesse caso
        