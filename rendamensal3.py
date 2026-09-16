# renda_mensal = float(input('Digite sua renda mensal: '))
# score  = 0.0
# possui_restricao = False


# if   renda_mensal >= 4000.00: 
#     0 < score < 1000
#     print('Aprovado')
# else:
#     possui_restricao
#     print ('Reprovado')

# if renda_mensal >= 2500.00 or renda_mensal >= 6000.00:
#     score >= 500
#     possui_restricao

#     print('Recusado')



# OUTRA FORMA/FORMA CORRETA

renda_mensal = 5000.0
score = 800
possui_restricao = False


if (not possui_restricao and score >= 700
    and renda_mensal >= 4000):
    print("Empréstimo Aprovado.")


elif (not possui_restricao and renda_mensal >= 2500
      and (score >= 500 or renda_mensal > 6000)):
    print('Analise Manual.')

else: 
    print('Empréstimo Negado.')

