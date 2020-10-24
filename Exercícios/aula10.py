n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Dgite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 7:
    print('Parabéns!!!')
else:
    print('Estude mais!')  