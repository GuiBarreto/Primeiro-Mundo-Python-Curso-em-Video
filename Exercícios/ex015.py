#PREÇO DO ALUGUEL
a = float(input('Quantos dias alugados? '))
km = float(input('quantos km rodados? '))
v = (a * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(v))
