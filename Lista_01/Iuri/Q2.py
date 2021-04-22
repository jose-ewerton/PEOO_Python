soma1 = 0
soma2 = 0
for c in range (1, 11):
  n = int(input("Digite o {}° número: ".format(c)))
  if n % 3 == 1:
    soma1 += n
  if n % n == 0:
    soma2 += n
    

print("Essa é soma dos ímpares {} e essa é a soma dos primos {}.".format(soma1, soma2))
