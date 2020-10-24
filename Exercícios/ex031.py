distancia = float(input('Qual a distância em Km da sua viagem?'))
perto = distancia * 0.5
longe = distancia * 0.45
if distancia <= 200:
    print('Sua viagem custará R${:.2f}'.format(perto))
else:
    print('Sua viagem custará R${:.2f}'.format(longe))
