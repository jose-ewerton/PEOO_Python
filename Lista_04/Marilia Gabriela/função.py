def soma_total(*num):
    soma = sum(num)
    print("A soma dos valores digitados é: {}".format(soma))


def acrescenta50(a):
    porc = a * 50 / 100
    total = a + porc
    print("{} + 50% do seu valor é {}".format(a, total))


def concatenar(*silabas):
    v = ""
    for c in silabas:
        v += c
    return v