si = 0
sp = 0

for c in range (1, 11,):
    n = int(input('Digite um número:'))
    if n % n == 0:
        sp = sp + n
    if n % 2 == 1:
        si = si + n

print('O somatório dos números primos é {}'.format(sp))
print('O somatório dos números ímpares é {}'.format(si))


