#ANALISANDO UM NÚMERO
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} '.format(num))
print('Possui {} unidades'.format(u))
print('Possui {} dezenas'.format(d))
print('Possui {} centenas'.format(c))
print('Possui {} milhares'.format(m))