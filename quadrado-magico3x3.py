#  Construa um jogo Quadrado Mágico 3X3, no qual o usuário preencherá o
# vetor com números de um a nove (sem repetir números) 
# e a soma de todas as linhas, colunas e
#  diagonais será igual a quinze.

# iniciar a matrzi com o que o usuario digitar (matriz 3x3)
matriz = []
for i in range(3):# 3 linhas
    linha = [] # inicia a linha vazia
    for j in range(3): # 3 colunas
        numero = int(input('Digite um número entre 1 e 9: '))
        # garantir que não tenha numeros fora do intervalo 1~9
        while numero < 1 or numero > 9:
            numero = int(input('Digite um número entre 1 e 9: ')) 

        linha.append(numero) # guarda o numero na linha

    matriz.append(linha) # adiciona a linha completa a matriz

# Forma 1 = lógica
soma = 0 # soma cada possibilidade 
somas = [] # guarda todas as somas em posições diferentes 

# Verificação das linhas
for linha in matriz: # para cada linha na matriz
    for numero in linha: # e para cada número dentro da linha
        soma += numero # soma
    somas.append(soma)

    # Verificar colunas
for j in range(3): # trava as colunas para 'andar' nas linhas 
    soma = 0 # cria uma variavel para somar os numeros das colunas
    for i in range(3): # isso é para andar nas linhas
        soma += matriz[i][j]
    somas.append(soma)

# verificar diagonais
diagonal_principal = 0 # da esquerda para direita
for i in range(3):
    diagonal_principal += matriz[i][i]

somas.append(diagonal_principal)

diagonal_secundaria = 0
for i in range(3): # da direita para esquerda
    diagonal_secundaria += matriz[i][2-i]

somas.appen(diagonal_secundaria)

if all(somas == 15 for soma in somas):
    print('Vitória')
else:
    print('Derrota')

# contador_de_sucesso = 0
lista_sucesso = []
for soma in somas: # verificar cada restrição
    if soma == 15:
        # contador_de_sucesso += 1
        lista_sucesso.append(True)
    else:
        lista_sucesso.append(False)

# if False in lista_sucesso:
#   print('Perdeu')












# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# n = numero de elementos
# linha e coluna

# for 3x3 -> O(n²)
# linha
# for 3x1 -> O(n)

# k = numeros de for (um embaixo do outro)
# 2 for 3x3 -> O(k * n²)

# 3 for 3x3 -> O(k * n²) = 3 * 3 * 3 = n3