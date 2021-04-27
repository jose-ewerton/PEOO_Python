import funções

print('teste pra função da soma')
a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
funções.soma_total(a, b)
print('='*40)

print('teste pra função do acréscimo')
a = int(input('Digite um valor:'))
funções.acrescenta50(a)
print('='*40)

print('teste pra função de concatenação')
print('Separe uma palavra em 3 sílabas')
p1 = str(input('1º sílaba:'))
p2 = str(input('2º sílaba:'))
p3 = str(input('3º sílaba:'))
print(funções.concatenar(p1, p2, p3))
print('='*40)

print('teste pra função de chave e valor')
print(funções.ultimo_valor_chave(chave01="Carro", chave02="Armário", chave03="Feijão"))
