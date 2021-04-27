import Funções

print('teste pra função da soma')
a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
Funções.soma_total(a, b)
print('='*40)

print('teste pra função do acréscimo')
a = int(input('Digite um valor:'))
Funções.acrescenta50(a)
print('='*40)

print('teste pra função de concatenação')
print('Separe uma palavra em 3 sílabas')
p1 = str(input('1º sílaba:'))
p2 = str(input('2º sílaba:'))
p3 = str(input('3º sílaba:'))
print(Funções.concatenar(p1, p2, p3))
print('='*40)

print('teste pra função de chave e valor')
print(Funções.ultimo_valor_chave(chave01="Carro", chave02="Armário", chave03="Feijão"))