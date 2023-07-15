frase = str(input('Digite uma frase: ')).strip().lower()
qv = frase.count('a')
p1 = frase.find('a') + 1
p2 = frase.rfind('a') + 1
print(f'A letra "a" aparece {qv} vezes')
print(f'A letra "a" aparece pela primeira vez na posição {p1}')
print(f'A letra "a" aparece pela última vez na posição {p2}')
