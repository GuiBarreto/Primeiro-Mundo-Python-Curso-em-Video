print('-=-' * 20)
print('Analisador de triângulo')
print('-=-' * 20)
r1 = float(input('Informe o primeiro segmento de reta: '))
r2 = float(input('Informe o segundo segmento de reta: '))
r3 = float(input('Informe o terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO!!!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!!!')
    