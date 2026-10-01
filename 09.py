
par = 0
impar = 0

for i in range(0, 7):
    
    numero = int(input('Digite um número: '))
    
    
    if  numero % 2 == 0:
            par += 1
    else: impar += 1

print(f'Par = {par}')
print(f'Impar = {impar}')

