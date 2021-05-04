p = 0
i = 0
contador = 0
for c in range(1, 11):
  n = int(input('Digite um número: '))
  if n % 2 != 0:
    i += n
  for valor in range(2,n):
    if n % valor == 0:
      contador += 1
  if (contador == 0 and  n != 1):
    p +=n
  contador = 0

   

print("O somatório dos números primos é: ", p)
print("O somatório dos números ímpares é: ", i)


