nom = (input('Qual é o nome do atleta? '))
while nom > '':
  s1 = float(input('Qual é a distância do 1° salto? '))
  s2 = float(input('Qual é a distância do 2° salto? '))
  s3 = float(input('Qual é a distância do 3° salto? '))
  s4 = float(input('Qual é a distância do 4° salto? '))
  s5 = float(input('Qual é a distância do 5° salto? '))
  break

print('Nome do atleta:', nom)
r = [s1, s2, s3, s4, s5]
print('Saltos', r)
m = (s1+s2+s3+s4+s5)/5
print('Média dos saltos', m)
