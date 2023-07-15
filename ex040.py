n1 = float(input('Qual foi a primeira nota do aluno? '))
n2 = float(input('Qual foi a segunda nota do aluno? '))
media = (n1 + n2) / 2
print(f'O valor da média é {media}')
if media < 5:
    print('Aluno reprovado!')
elif 5 <= media < 7:
    print('Aluno em recuperação!')
else:
    print('Aluno APROVADO!')
