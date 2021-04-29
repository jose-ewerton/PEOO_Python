import função

#teste pra função da soma
a = int(input("Digite um número:"))
b = int(input("Digite um número:"))
c = int(input("Digite um número:"))
função.soma_total(a, b, c)
print('='*40)

#teste pra função do acréscimo
a = int(input('Digite um valor:'))
função.acrescenta50(a)
print('='*40)

#teste pra função de concatenação
print('Divida uma palavra em duas sílabas')
a = str(input("Digite uma sílaba:"))
b = str(input("Digite uma sílaba:"))
print(função.concatenar(a, b))