angulo1 = float(input('Informe a medida angular: '))
angulo2 = float(input('Informe a medida angular: '))
angulo3 = float(input('Informe a medida angular: '))


# if angulo1 + angulo2 >= angulo3 or angulo1 + angulo3 >= angulo2 or angulo2 + angulo3 >= angulo1:
#      print('Este triangulo não possui forma geométrica')
#      exit()



if angulo1 + angulo2 < angulo3 or angulo2 + angulo3 < angulo1 or angulo1 + angulo3 < angulo2:
     print('Este triangulo não possui forma geométrica')
     exit()


if angulo1 == angulo2 == angulo3:
     print('Este triângulo é equilátero.')

elif angulo1 == angulo2 or angulo2 == angulo3 or angulo1 == angulo3:
     print('Este triângulo é isósceles. ')

elif angulo1 != angulo2 and angulo2 != angulo3 and angulo1 != angulo3:
     print('Este triângulo é escaleno')




# outra forma
lado_a = float(input('Informe a medida angular: '))
lado_b = float(input('Informe a medida angular: '))
lado_c = float(input('Informe a medida angular: '))

condicao = (
     (lado_a + lado_b > lado_c) and
     (lado_a + lado_c > lado_b) and
     (lado_b + lado_c > lado_a) 
)

if condicao:
     if lado_a == lado_b == lado_c:
          print('Equilatero.')

     elif lado_a != lado_b != lado_c:
          print('Escaleno.')

     elif (lado_a == lado_b or 
           lado_a == lado_c or 
           lado_b == lado_c):
          print('Isosceles')
else:
     print('Não é um triangulo.')