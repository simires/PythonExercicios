v = float(input('Insira a sua velocidade em km/h: '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Você foi multado por ultrapassar o limite de 80 km/h! Pague R$ {multa:.2f}')

"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""