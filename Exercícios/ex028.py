#JOGO DA ESCOLHA DE ZERO A 5
from random import choice
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
rival = (int(input('Escolha um número de 0 a 5 :')))
lista = [n0, n1, n2, n3, n4, n5]
escolhido = choice(lista)
if escolhido == rival:
    print('Parabéns você acertou!!!')
else:
    print('Errrrrooooouuuu o número certo é {}!!!!'.format(escolhido))
    