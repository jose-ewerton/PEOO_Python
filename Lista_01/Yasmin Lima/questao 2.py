impares = list()

primos = list()

somaimpares = 0

somaprimos = 0

 

for n in range(1, 11):

    a = int(input("Diga um número:"))

    if a % n == 0:

        somaprimos += a

        primos.append(a)

    elif a % n != 0:

        somaimpares += a

        impares.append(a)

 

print("Números primos: {}").format(primos)

print("a soma dos números primos: {}").format(somaprimos)

print("os números ímpares: {}").format(impares)

print("a soma dos números ímpares: {}").format(somaimpares)

 

ótimo = 0

regular = 0

bom = 0

médiaótimo = 0

 

for p in range(1, 16):

    idade = int(input("idade: "))

    op = int(input("digite um numero para classificar o filme o filme?"

              " 1=regular/2=bom/3=ótimo:"))

    if op == 3:

        médiaótimo += idade

        ótimo += 1

    elif op == 2:

        bom += 1

    elif op == 1:

        regular += 1

    else:

        print("esse numero nao vale")

        break

 

médiaótimo = médiaótimo/ótimo

porcentagem = bom*100/15

 

 

print("As pessoas que responderam 'ÓTIMO' tem em média {} de idade.".format(médiaótimo))

print("{} pessoas acharam o filme 'REGULAR'!".format(regular))

print("{:.2f}% de todas as pessoas responderam 'BOM'!".format(porcentagem))
