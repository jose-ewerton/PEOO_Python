'''Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
a soma dos números primos.'''



n0 = []
nimp = []
ci = 1
for c in range(1, 11):
    n = int(input(f"Digite o {ci}º número: "))
    n0.append(n)
    if n %2 != 0:
        nimp.append(n)
    somaimp= sum(nimp)
    ci+= 1

np= 0
np2= 0
somaprimo= 0
for c2 in range (1, 11):
    for c3 in range(1, n0 [np]+1):
        if n0 [np] % c3 ==0:
            np2+=1

    if np2 == 2:
            somaprimo += n0[np]

    np += 1
    np2 = 0



print('')
print('================================================')
print('')

print("A soma dos números que são primos é de:",somaprimo)
print("A soma dos números que são ímpares é de:", somaimp)

print('')
print('================================================')
print('')
print('By: Vinicius Barbosa')