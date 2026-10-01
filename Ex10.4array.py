numero = []

for i in range(0, 5):
    vetor = int(input('Digite os números: '))
    numero.append(vetor)

segundo_vetor = numero.copy()

segundo_vetor.reverse()
print(segundo_vetor)
