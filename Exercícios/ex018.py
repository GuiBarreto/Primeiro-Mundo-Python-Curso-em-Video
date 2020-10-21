import math
ângulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem: \no seno de {:.2f} \no cosseno de {:.2f} \ne a tangente {:.2f}'
      .format(ângulo, seno, cosseno, tangente))
