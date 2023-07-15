mony = float(input('Digite quantos reais tem na carteira: \nR$'))
# 1 dólar == 4.88 reais
dolar = mony/4.88
# 1 iene == 0.038 real
iene = mony/0.038
# 1 euro == 5.16 reais
euro = mony/5.16
print('Você pode comprar :\nU${:.2f} \nY${:.2f}\nE${:.2f}'.format(dolar, iene, euro))
