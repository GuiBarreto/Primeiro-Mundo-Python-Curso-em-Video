#AULA SOBRE IMPORTAR UMA FUNÇAO DA BIBLIOTECA
from math import sqrt
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hipo = ((cato ** 2) + (cata ** 2)) 
print('a hipotenusa do triângulo retângulo é {:.2f}'.format(sqrt(hipo)))
