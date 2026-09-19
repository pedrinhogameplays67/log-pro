
# se a cidade for RJ,
#   print "Seja bem-vindo a cidade Maravilhosa, nome"
# se não for RJ, exiba o nome da pessoa e da cidade

def verificar_local(nome, cidade):
    if cidade == 'Rio de Janeiro' or cidade == 'RJ':
        print(f'Seja bem-vindo à Cidade Maravilhosa, {nome}')
    else:
        print(f'Seja Bem-vindo à {cidade}, {nome}')

nome = input('Digite seu nome: ')
cidade = input('Digite a cidade ')
    
verificar_local(nome, cidade)
