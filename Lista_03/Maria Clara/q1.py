print(f'-=-=-=-=-=- PARA INTERRONPER DIGITE ZERO  -=-=-=-=-=-= ')
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
    x = int(input('Numero: '))
    if x == 0:
        break
    l.append(x)
    quantidade = len(l)


l = soma(l)
print(f"A soma dos {quantidade} números é: {l}")