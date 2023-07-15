casa = float(input('Qual é o valor total da casa a ser financiada? R$'))
sal = float(input('Qual é o salário do solicitante do financiamento? R$'))
ano = int(input('Em quantos anos pretende pagar o financiamento? '))
prestacao = casa / (ano * 12)
if prestacao > sal * 0.30:
    print('Seu financiamento foi NEGADO!')
else:
    print(f'Seu financiamento foi APROVADO!\nA prestação mensal será de R$ {prestacao:.2f}!')
