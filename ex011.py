l = float(input('Largura da parede: \n'))
h = float(input('Altura da parede: \n'))
area = l * h
# 1 litro de tinta pinta 2 m²
tinta = area/2
print('A dimensão da parede é {} m x {} m, logo a área é {}\nVisto que 1 L de tinta pinta 2m²'.format(l, h, area))
print('A quantidade de tinta necessária é: {:.2f} litros'.format(tinta))
