#ANALISANDO NOME
nome = str(input('Digite seu Nome completo: ')).strip()
print('Analisando seu nome.....')
print('Seu nome em maiusculo fica {} '.format(nome.upper()))
print('Seu nome em minusculo fica {} '.format(nome.lower()))
print('Seu nome no total tem {} letras' .format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro é {} e ele tem {} letras' .format(separa[0], len(separa[0])))