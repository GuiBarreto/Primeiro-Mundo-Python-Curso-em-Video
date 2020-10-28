#AUMENTO DO SALÁRIO
salario = float(input('Digite seu salário R$:'))
maior = salario * 0.10
menor = salario * 0.15
if salario > 1250:
    print('Seu aumento será de R${} virando R${} ' .format(maior, salario + maior))
else:
    print('Seu aumento será de R${} virando R${}' .format(menor, salario + menor))
    