p = []
i = []
for c in range(1, 5):
 n = int(input('Digite um número: '))
 if n % 2 == 0:
   p.append(n)
 else:
   i.append(n)

print("O somatório dos números primos é: ", sum(p))
print("O somatório dos números ímpares é: ", sum(i))


