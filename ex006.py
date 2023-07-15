n = float(input('Digite um número: '))
dob = n * 2
tri = n * 3
raiz = n ** (1/2)
print(' O dobro desse número é {} \n O triplo é {} \n Sua raiz quadrada é {:.2f}' .format(dob, tri, raiz))
# se não colocamos f nas chaves depois do . e do número, ele não vai mostrar 2 casas depois da vírgula
