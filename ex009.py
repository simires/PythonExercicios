nm = int(input('Digite um número inteiro: '))
#print(' {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {}' .format(nm, nm*1, nm, nm*2, nm, nm*3, nm, nm*4, nm, nm*5))
#print(' {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}'.format(nm, nm*6, nm, nm*7, nm, nm*8, nm, nm*9 , nm, nm*10))
print('-' * 20)
for i in range(1,11):
    print('{} x {:2} = {}'.format(nm, i, nm*i))
print('-' * 20)
