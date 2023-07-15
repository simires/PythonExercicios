km = float(input('Qual é a diatância da sua viagem em km? '))
if km > 200:
    p = km * 0.45
    print(f'O valor da sua passagem é R$ {km * 0.45:.2f}')
else:
    print(f'O valor da sua passagem é R$ {km * 0.50:.2f}')

"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas."""