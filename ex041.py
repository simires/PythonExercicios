from datetime import date
anonasceu = int(input('A Confederação Nacional de Natação precisa classificá-lo. Qual o seu ano de nascimento?  '))
anoatual = date.today().year
idade = anoatual - anonasceu
if idade <= 9:
    print('Sua categoria de natação é MIRIM')
elif 9 < idade <= 14:
    print('Sua categoria de natação é INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria de natação é JUNIOR')
elif 19 < idade <= 20:
    print('Sua categoria de natação é SÊNIOR')
else:
    print('Sua categoria de natação é MASTER')
