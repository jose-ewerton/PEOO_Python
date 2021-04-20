#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
#do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
#programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
#depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
#não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Z= (input("Qual seu nome?"))

A= (float(input("Digite seu primeiro salto:")))
B= (float(input("Digite seu segundo salto:")))
C= (float(input("Digite seu terceiro salto:")))
D= (float(input("Digite seu quarto salto:")))
E= (float(input("Digite seu quinto salto:")))

Y= (A+B+C+D+E)/5

X=(Z,'Você realizou 5 saltos' ,A,B,C,D,E, 'eles tem a média de',Y,)
print(X)


