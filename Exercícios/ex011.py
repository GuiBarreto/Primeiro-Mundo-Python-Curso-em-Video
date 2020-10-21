#CALCULO DE ÁREA QUADRADA PARA PINTAR PAREDE
a = float(input('Digite a altura da parede: '))
l = float(input('Digite a larguta da parede'))
m2 = a*l
t = (a*l)/2
print('a parede de {:.2f} X {:.2f} tem {:.2f} metros² serão necessários {:.3f} litros de tinta para pinta-lá! '
.format(a, l, m2, t))