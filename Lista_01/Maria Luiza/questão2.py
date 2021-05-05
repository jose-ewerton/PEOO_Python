"""Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
a soma dos números primos."""

impares = list()
primos = list()
somaimpares = 0
somaprimos = 0
for n in range(1, 11):
    a = int(input("Digite um número:"))
    #for só pra essa condição
    if a % 1 == 0 and a % a == 0:
        somaprimos += a
        primos.append(a)
    if a % 2 != 0:
        somaimpares += a
        impares.append(a)

print('\033[1m'f"Números primos: {primos}")
print(f"Soma dos números primos: {somaprimos}")
print(f"Números ímpares: {impares}")
print(f"Soma dos números ímpares: {somaimpares}"'\033[m')