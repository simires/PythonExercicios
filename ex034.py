sal = float(input('Qual é o seu salário? R$ '))
if sal > 1250:
    print(f'Seu novo salário será de de R$ {(sal * 0.1) + sal:.2f}')
else:
    print(f'Seu novo salário será de R$ {(sal * 0.15) + sal:.2f}')

"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule
um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""