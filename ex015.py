dias = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos quilômetros o carro andou? '))
preco = 60 * dias + 0.15 * km
print('Considerando que paga-se R$60 por dia e R$0.15 por km rodado, ',end='')
print('o preço a se pagar é: R${:.2f}'.format(preco))
