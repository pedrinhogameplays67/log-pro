def impar(numero):
    if not numero % 2 == 0:
        return True

    return False



def impar2(numero):
    return not numero % 2 == 0


print(impar2(3))
# verificar se na senha tem 8 caracteres[
def verificar_senha(senha):
    # len() -> tamanho
    return len(senha) >= 8

verificar_senha('fjyv543x')
    