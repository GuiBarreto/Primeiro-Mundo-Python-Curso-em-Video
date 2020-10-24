velocidade = float(input('Qual a velocidade em Km/H do seu carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado em R${:.2f} ligeirinho' .format(multa))
else:
    print('Que bom pois o limite é 80Km/H e você será multado se passar.')