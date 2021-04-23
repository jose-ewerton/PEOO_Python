c_impar = 0
s_impar = 0

for c in range(1, 11):
    n = int(input('Digite um numero:'))
    if n % n == 0:
        s_impar = s_impar + n
    if n % 2 == 1:
        c_impar = c_impar + n

print('A soma dos numeros primos é {}'.format(s_impar))
print('A soma dos numeros impares é {}'.format(c_impar))


