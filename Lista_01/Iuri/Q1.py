z = 0 
x = 0 
v = 0 
b = 0 
n = 0 
m = 0 
k = 9999 
l = 0 

for c in range(0, 15):
  p = float(input("Digite seu peso: "))
  a = float(input("Digite sua altura: "))
  c = srt(input("Qual o seu sexo? (F/M)"))

  z += a
  if a > m and c.upper() == "F":
    m = a

  if a < 75.6:
    k and c.upper() == "M":
      k += a

  if a > 1.70 and c.upper() == "M":
    n += 1

  if p > l and c.upper() == "M":
    l = p

  if c.upper() == "M":
    b += 1

  if c.upper() == "F":
    v += 1

q = sa / 15 
w = (100 * nm) / 15 
e = (100 * nh) / 15 

print ("A média de todas as alturas são: {}.".format(q))
print ("A mulher mais alta mede: {}.".format(m))
print ("O homem mais baixo mede: {}.".format(k))
print ("Número de homens medindo mais de 1,70 {}.".format(v))
print ("O homem mais pesado: {}".format(l))
print ("O percentual das mulheres: {}%".format(w))
print ("O percentual de homens: {}%",format(e))
