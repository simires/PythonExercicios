n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menor = ''
maior = ''
if n1 < n2: # achando quem é o menor e o maior entre n1 e n2
    menor = n1
    maior = n2
if n2 < n1:
    menor = n2
    maior = n1

n3 = int(input('Digite o terceiro número: '))
if n3 < menor: # se n3 for menor que o menor anterior, ele é o menor
    menor = n3
else: # se não for o menor
    if n3 > maior: # se ele for maior que o maior anterior, ele é o maior
        maior = n3
print(f'Menor = {menor} \nMaior = {maior}')

"""Faça um programa que leia três números e mostre qual é o maior
e qual é o menor."""