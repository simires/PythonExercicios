"""Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo."""
a = float(input('Qual o comprimento da primeira reta em \033[4mcm\033[m? '))
b = float(input('Qual o comprimento da segunda reta em \033[4mcm\033[m? '))
c = float(input('Qual o comprimento da terceira reta em \033[4mcm\033[m? '))
if a + b > c and a + c > b and b + c > a:
    print('Essas retas \033[32mPODEM\033[m formar um triângulo.')
else:
    print('Essas retas \033[31mNÃO PODEM\033[m formar um triângulo.')
