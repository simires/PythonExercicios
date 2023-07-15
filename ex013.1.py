preco = float(input('Digite o preço do produto: R$'))
#preço à vista tem 10% de desconto
print('Fazendo pagamento à vista, o preço fica: R${}'.format(preco*0.9))
#parcelado tem 8% de aumento
print('Com parcelamento fica R${}'.format(preco*1.08))
