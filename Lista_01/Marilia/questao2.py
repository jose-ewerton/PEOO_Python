#valores
impares = list()
primos = list()
somaimpares = 0
somaprimos = 0


#código principal
for n in range(1, 11):
    a = int(input("Digite um número:"))
    if a % n == 0:
        somaprimos += a
        primos.append(a)
    elif a % n != 0:
        somaimpares += a
        impares.append(a)

#saída
print("Números primos: {}".format(primos))
print("Soma dos números primos: {}".format(somaprimos))
print("Números ímpares: {}".format(impares))
print("Soma dos números ímpares: {}".format(somaimpares))