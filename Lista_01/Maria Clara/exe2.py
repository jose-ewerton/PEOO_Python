soma2 = 0
soma = 0
for c in range(1, 11):
    print('-=-=-=-=-=-=-=-=-=-=-=-= ')
    num = float(input('Digite um número: '))
    if num % 2 == 1:
        soma += num
    if num % num == 0:
        soma2 += num
print(f'A soma dos números ímpares foi: {soma} ')
print(f'A soma dos números primos foi: {soma2} ')
