# SISTEMA DE CONTROLE DE MAQUINÁRIO

# variavel hora da forma certa/otimizada
hora = 10
hora >= 8 and hora <= 17



cargo = input('Digite o cargo (Supervisor ou Operador): ')
hora = int(input('Digite o horario atual (em horas): '))
chave_emergência = True
# chave de emergencia é booleano, true ou false

if (chave_emergência or cargo == 'Supervisor' or
    (cargo == "Operador" and 8<=hora<=17)):
    print('Acesso Aprovado')
else:
    print('Acesso Recusado')