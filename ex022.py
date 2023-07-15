nome = str(input('Digite seu nome completo:\n'))
print('Seu nome em maiúsculas é:', nome.upper())
print('Seu nome em minúsculas é:', nome.lower())
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
nome = nome.split()
l = ''
for i in nome:
    l = l + i
print(f'Seu nome completo tem {len(l)} letras')

