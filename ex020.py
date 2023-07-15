from random import shuffle
prim = input('Primeiro aluno: ')
sec = input('Segundo aluno: ')
terc = input('Terceiro aluno: ')
quar = input('Quarto aluno: ')
lista = [prim, sec, terc, quar]
shuffle(lista)
print('A ordem de apresentação será: \n{}'.format(lista))
