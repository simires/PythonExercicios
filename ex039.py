from datetime import date
anonasc = int(input('Qual o ano que você nasceu? '))
anoatual = date.today().year
dif = anoatual - anonasc
if dif < 18:
    print(f'Você tem {anoatual - anonasc} anos, portanto faltam {18 - dif} anos para se alistar para o serviço militar.')
elif dif == 18:
    print(f'Você tem {anoatual - anonasc} anos. É hora de se alistar para o serviço militar!')
else:
    print(f'Você tem {anoatual - anonasc} anos, então passaram {dif - 18} anos do período do alistamento militar para você.')
