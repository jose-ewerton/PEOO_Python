print('Para parar a soma digite 0:')
def soma(lista):
    l = lista
    cont = 0
    soma = 0
    for i in range(len(l)):
        soma += l[i]
        cont += 1
    return soma

l = []
while True:
    n = int(input('Numero: '))
    if n == 0:
        break
    l.append(n)
    quant = len(l)

l = soma(l)
print(f"A soma dos {quant} números é: {l}")

