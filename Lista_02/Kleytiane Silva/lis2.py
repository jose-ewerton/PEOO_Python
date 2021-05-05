print('Responda com sinceridade as perguntas a seguir, use 0 para não e 1 para sim.')
p1 = int(input('Telefonou para a vítima? '))
p2 = int(input('Esteve no local do crime? '))
p3 = int(input('Mora perto da vítima? '))
p4 = int(input('Devia para a vítima? '))
p5 = int(input('Já trabalhou com a vítima? '))
lista = []

if p1 == 1:
  lista += ['a']

if p2 == 1:
  lista += ['b']

if p3 == 1:
  lista += ['c']

if p4 == 1:
  lista += ['d']

if p5 == 1:
  lista += ['e']

pr = len(lista)
if pr < 2:
  print('Você é inocente :)')
elif pr == 2:
  print('Você é suspeito..')
elif pr == 3 or pr == 4:
  print('Você é cúmplice')
elif pr == 5:
  print('Você é culpado :O')