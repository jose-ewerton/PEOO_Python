#valores
somaaltura = 0
mulheralta = 0
homem_mais_baixo = 0
homens_170 = 0
homem_mais_pesado = 0
total_homens = 0
total_mulheres = 0


#Código Principal
for c in range(1, 16):
    print('{}ª PESSOA'.format(c))
    sexo = str(input("Sexo(Masculino ou Feminino): ")).lower().strip()
    peso = int(input("Peso: "))
    altura = float(input("Altura: "))
    somaaltura += altura
    if sexo in 'm':
        total_homens += 1
    else:
        total_mulheres += 1

    if altura >= 1.70 and sexo in 'm':
        homens_170 += 1
    if c == 1 and sexo in 'm':
        homem_mais_baixo = altura
        homem_mais_pesado = peso
    if sexo in 'm' and altura < homem_mais_baixo:
        homem_mais_baixo = altura
    if sexo in 'm' and peso > homem_mais_pesado:
        homem_mais_pesado = peso
    if c == 1 and sexo in 'f':
        mulheralta = altura
    if sexo in 'f' and altura > mulheralta:
        mulheralta = altura

#valores finais
mediaaltura = somaaltura / 15
porcentagemhomem = total_homens*100/15
porcentagemmulher = total_mulheres*100/15


#saída
print("A média de altura foi de: {:.2f}".format(mediaaltura))
print("A mulher mais alta tem {} de altura.".format(mulheralta))
print("O homem mais baixo tem {} de altura.".format(homem_mais_baixo))
print("Tem {} homens com mais de 1,70 de altura.".format(homens_170))
print("O homem mais pesado, pesa {}kg.".format(homem_mais_pesado))
print("A porcentagem de homens é de {:.2f}%".format(porcentagemhomem))
print("A porcentagem de mulheres é de {:.2f}%".format(porcentagemmulher))