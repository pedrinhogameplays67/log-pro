primeiro = 0
segundo = 1
proximo_numero = (primeiro + segundo)

for i in range(2000):
    print(proximo_numero)
    if proximo_numero > 987:
        break
    primeiro = segundo
    segundo = proximo_numero
    proximo_numero = primeiro + segundo
    continue


# OUTRA FORMA

# num1 = 0
# num2 = 1
# resultado = 0
# while num1 <= 2000:
#     resultado = num1 + num2
#     print(num1)
#     num1 = num2
#     num2 = resultado

