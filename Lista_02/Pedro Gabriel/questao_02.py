"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Souza
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado:
Atleta: Rodrigo Souza
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""


n = str (input("Qual o nome do atleta: ")) #Nome.
s1 = float (input("Primeiro salto: ")) #Salto 1.
s2 = float (input("Segundo salto: ")) #Salto 2.
s3 = float (input("Terceiro salto: ")) #Salto 3.
s4 = float (input("Quarto salto: ")) #Salto 4.
s5 = float (input("Quinto salto: ")) #Salto 5.
total = (s1 + s2 + s3 + s4 + s5)
m = (total / 5)
print("Resultado: ")
print("Nome do atleta", n)
print("Saltos:", s1,'-', s2,'-', s3,'-', s4,'-', s5)
print("Media dos saltos", m)
