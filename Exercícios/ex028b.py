from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar....')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('PARABÉNS!!! você me venceu!!!!')
else:
    print('GANHEI!!! Eu pensei {} e não no {}' .format(computador, jogador))
    