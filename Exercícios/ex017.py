import math
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa será {:.2f}'.format(hi))
