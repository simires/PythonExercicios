#calcular sen cos e tg de um ângulo
from math import radians, sin, cos, tan
ang = radians(float(input('Digite o ângulo: ')))
print(f'seno = {sin(ang):.2f} \ncosseno = {cos(ang):.2f} \ntangente = {tan(ang):.2f}')
#as funções sin, cos e tan trabalham com radianos, então temos que converter o valor do ângulo p/ radianos
