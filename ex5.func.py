# Crie uma função que coloque qualquer 
# padrão e o retorne:
#  Tudo em minúscula.
#   Sem espaços na frente ou atrás
#       (começando e finalizando o texto).

def limpar_texto(texto):
    texto = texto.strip().lower()
    if ['0', '1', '2'] in texto:
        return texto, True


l = [0, 1]
l.is_digit()
texto, tem_numero = limpar_texto('vamos2 ver ')
print(texto)
print(tem_numero)