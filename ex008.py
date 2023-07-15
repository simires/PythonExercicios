me = float(input('Digite o valor em metros: '))
# 1 metro == 10 dm
dm = me * 10
# 1 metro == 100 cm
cm = me * 100
# 1 metro == 1000 mm
mm = me * 1000
# 1 me == 0.1 dam
dam = me * 0.1
# 1 me == 0.01 hm
hm = me * 0.01
# 1 me == 0.001 km
km = me * 0.001
print('{} metros correspondem a:\n{} decímetros \n{} centímetros \n{} milímetros' .format(me, dm, cm, mm))
print('{} decâmetros \n{} hectômetros \n{} quilômetros'.format(dam, hm, km))
