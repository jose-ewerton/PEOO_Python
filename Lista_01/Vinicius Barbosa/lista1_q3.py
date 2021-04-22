'''Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
a um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
a. A média das idades das pessoas que responderam ótimo;
b. A quantidade de pessoas que responderam regular;
c. A porcentagem de pessoas que responderam bom entre todos os espectadores
analisados.'''



b = int(input('quantas pessoas irão avaliar o filme?'))
a = input('Qual o nome do filme que está sobre analise crítica?')

x = b + 1

print(f'Me informe a idade e a opinião dos {b} espectadores sobre o filmme "{a.upper()}" sendo ótimo = 3, bom = 2, regular = 1')

opn = []
idade = []
i = 1
while i < x:
  """
  forneca a opinião das pessoas como 1 = ruim, 2 = regular, 3 = bom
  """
  idade.append(int(input(f"qual a idade da {i}º pessoa?:")))
  opn.append(int(input("qual o nivel de opniao dele, sendo bom = 3, regular = 2, e ruim = 1?:")))
  i += 1

print('')
print('===============================================')
print('')


md = sum(idade) / len(idade)
print(f"a media da idade do grupo é de: {md} anos")
cont = opn.count(2) #contagem de opniões = regular
cont2 = opn.count(1) #contagem de opniões = ruim
cont3 = opn.count(3) #contagem de opniões = bom
print(f'{cont2} pessoas votaram "RUIM"')
print(f'{cont} pessoas votaram "REGULAR"')
print(f'{cont3} pessoas votaram "BOM"')

pbom = (opn.count(3) / len(opn)) * 100
pregular = (opn.count(2) / len(opn)) * 100
pruim = (opn.count(1) / len(opn)) * 100


print(f'{pbom}% das pessoas votaram em "BOM", {pregular} em "REGULAR", e {pruim} em "RUIM"')


print('')
print('===============================================')
print('')
print('By: Vinicius Barbosa')