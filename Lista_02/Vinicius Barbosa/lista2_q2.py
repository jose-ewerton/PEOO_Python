'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta.'''



n = str(input("Qual o nome do atleta? "))
salto1 = float (input("Distância do primeiro salto em metros? "))
salto2 = float (input("Distância do segundo salto em metros? "))
salto3 = float (input("Distância do terceiro salto em metros? "))
salto4 = float (input("Distância do quarto salto em metros? "))
salto5 = float (input("Distância do quinto salto em metros? "))
total = (salto1 + salto2 + salto3 + salto4 + salto5)
m = (total / 5)
print("Resultado:")
print("Atleta:", n)
print("Saltos:", salto1, "-", salto2, "-", salto3, "-", salto4 , "-", salto5)
print("Media dos saltos", m)

print('')
print('====================================================')
print('')

print('By: Vinicius Barbosa, info2v')