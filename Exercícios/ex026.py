frase = str(input('Digite uma frase: ')).upper().strip()
print('Tem {} letras A na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}' .format(frase.find('A') + 1))
print('A última letra A aparece na pocição {}' .format(frase.rfind('A') + 1))
