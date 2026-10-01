nota = []

for i in range (0, 6):
    numeros = float(input('Digite as notas: '))
    nota.append(numeros)

resultado = sum(nota) / len(nota)
print(f'Sua média é {resultado:.2f}.')
contador = 0


for i in range (0, len(nota)):
# nota[i] é pra saber quais indices são menos que o resultado
    if nota[i] > resultado:
        print(nota[i])
# o contador serve pra somar cada nota que estiver acima da media, somando cada nota, se tiver duas, soma uma depois a outra.
        contador+=1
print(f'Você tem {contador} notas acima da média. ')




#  V1 -> jeito python 

# acima_media = [nota for nota in numeros if nota > resultado]

# print(f'Qtd notas acima da media: {len(acima_media)}')


# V2 -> 'normal'

# acima_media = []
# for nota in numeros:
#     if nota > resultado:
#         acima_media.append(nota)


