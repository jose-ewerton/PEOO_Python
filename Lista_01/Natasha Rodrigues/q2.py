'''
Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
a soma dos números primos.
'''
som = 0
somp = 0 
for n in range(1, 11):
    num = int(input('Digite um número:'))
    if num % 2 != 0:
        som += num
    if num % num == 0:
        somp += num
    
print('A soma dos numeros ímpares é {}'.format(som))
print('A soma dos numeros primos é {}'.format(somp))
