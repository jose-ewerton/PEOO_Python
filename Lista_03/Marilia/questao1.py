'''
#valores
n = []
s = []


#função
def somaequantidade(a):
    quantidade = len(n)
    soma = sum(s)
    print("Quantidade de números: {}".format(quantidade))
    print("Soma dos números: {}".format(soma))


#código principal
while True:
    a = int(input("informe um Número:"))
    print("digite '777' pra parar")
    n.append(a)
    s.append(a)

    if a == 777:
        n.pop()
        s.pop()
        print(somaequantidade(a))
        break
'''
def soma(*args):
    return sum(args)

print(soma(10,1,1))


