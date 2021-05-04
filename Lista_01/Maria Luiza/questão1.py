"""Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, em
seguida calcule e informe:
a. A média de altura do grupo;
b. A mulher mais alta e o homem mais baixo;
c. O número de homens com mais de 1,70 m de altura;
d. O homem mais pesado;
e. O percentual de homens e de mulheres."""

somaaltura = 0
mulheralta = 0
homembaixo = 0
homens170 = 0
homempesado = 0
homens = 0
mulheres = 0

for v in range(1, 4):
    print(''' ----- {}ª PESSOA ----- '''.format(v))
    sexo = str(input("Sexo[M/F]: ")).strip().upper()
    peso = int(input("Peso: "))
    altura = float(input("Altura: "))
    somaaltura += altura
    if sexo in 'M':
        homens += 1
    else:
        mulheres += 1

    if altura >= 1.70 and sexo in 'M':
        homens170 += 1
    if v == 1 and sexo in 'M':
        homembaixo = altura
        homempesado = peso
    if sexo in 'M' and altura < homembaixo:
        homembaixo = altura
    if sexo in 'M' and peso > homempesado:
        homempesado = peso


    if v == 1 and sexo in 'F':
        mulheralta = altura
    if sexo in 'F' and altura > mulheralta:
        mulheralta = altura

mediaaltura = somaaltura / 4
porcentagemhomem = homens*100/4
porcentagemmulher = mulheres*100/4

print('\033[1m'f"A média de altura foi de: {mediaaltura:.2f}")
print(f"A mulher mais alta tem {mulheralta} de altura.")
print(f"O homem mais baixo tem {homembaixo} de altura.")
print(f"Tem {homens170} homens com mais de 1,70 de altura.")
print(f"O homem mais pesado, pesa {homempesado}kg.")
print(f"A porcentagem de homens é de {porcentagemhomem:.2f}%")
print(f"A porcentagem de mulheres é de {porcentagemmulher:.2f}%"'\033[m')