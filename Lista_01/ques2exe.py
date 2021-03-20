#PERGUNTA
num = []
for i in range(10):
    num.append(int(input("Digite um número: ")))

#NUMEROS IMPARES
impar = []
for b in num:
    if b % 2 != 0:
        impar.append(b)

#NUMEROS PRIMOS
primos = 0
g = 0
indi = 0
contador = 0

while g < 9:
    for d in range(1, num[indi]+1):
        if num[indi] % d == 0:
            contador += 1
    if contador == 2:
        primos += num[indi]
    g += 1
    indi += 1
    contador = 0
print(f"A soma dos números impares é", sum(impar))
print(f"A soma dos números primos é", primos)
