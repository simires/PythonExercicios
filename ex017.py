from math import sqrt, hypot
c_o = float(input('Digite o cateto oposto: '))
c_a = float(input('Digite o cateto adjacente: '))
'''hip = sqrt(c_o ** 2 + c_a ** 2)
print(f'A hipotenusa de {c_o} e {c_a} é {hip:.2f}')'''

hip = hypot(c_o, c_a)
print(f'O valor da hipotenusa é {hip:.2f}')