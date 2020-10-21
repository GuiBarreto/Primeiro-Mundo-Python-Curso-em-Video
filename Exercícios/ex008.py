#CONVERSOR DE MEDIDAS
n = float(input('digite um valor em metros: '))
km = n/1000
hm = n/100
dam = n/10
cm = n*100
mm = n*1000
print('{} metros é o mesmo que {} Km, {} hm, {} dam, {} centimetros e {} milimetros!'
      .format(n, km, hm, dam, cm, mm))
