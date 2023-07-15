"""Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint # módulo pra randomizar os números
from time import sleep # módulo pra fazer o computador 'esperar' antes de dar a resposta
num = randint(0, 5) # Faz o computador 'pensar'
print('\033[1;34m=-=\033[m'*20)
print('Pensei em um número entre 0 e 5... qual você acha que é?')
print('\033[1;34m=-=\033[m'*20)
numu = int(input()) # É a resposta do usuário
print('\033[1;34m-=-'*20)
print('\033[36mPROCESSANDO...\033[m')
sleep(2) # vai fazer ele esperar 2 segundos
if num == numu: # Se os números forem iguais, acertou
    print('\033[33mVocê acertou!\033[m')
else: # Se os números não forem iguais, errou
    print(f'\033[35mVocê errou!\033[m Era \033[32m{num}\033[m')
