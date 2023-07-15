from random import choice
prim = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
terc = input('Terceiro aluno: ')
quar = input('Quarto aluno: ')
lista = [prim, seg, terc, quar]
print(f'O aluno escolhido foi: {choice(lista)}')
