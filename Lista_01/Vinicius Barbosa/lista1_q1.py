'''
Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, em
seguida calcule e informe:
a. A média de altura do grupo;
b. A mulher mais alta e o homem mais baixo;
c. O número de homens com mais de 1,70 m de altura;
d. O homem mais pesado;
e. O percentual de homens e de mulheres'''

Masculino = []  #Homens
F = []  #Mulheres
alm = []  #Altura dos homens
alf = []  #Altura das mulheres
pesom = []  #Peso dos homens
pesof = []  #Peso das mulheres


print("Me infome dados de 15 pessoas para que eu possa calcular\na média da altura do grupo, a mulher mais alta\no homem mais baixo, o nº de homens com mais de 1,7 de altura\no homem mais pesado, e o percentual de homens e mulheres")

print(' ')
print('=========================================================')
print(' ')

i = 1

while i < 3:
    '''
    fiz com apenas 2 para que na hora de tastar não demore muito'''

    print(f"{i} individuo; use M/m para masculino e F/f para feminino")
    gen = input(f'Qual gênero do {i}º individuo:')

    if ((gen == "M") or (gen == "m")):

        Masculino.append(gen)
        for item in Masculino:
            print(f'Individuo {i} é ',gen)

        alm.append(float(input(f"Informe a altura do {i}º individuo em metros ex => 1.70: ")))
        pesom.append(float(input(f"Informe o peso do {i}º individuo em Kg ex => 80: ")))
        print('')

        m = []
        for cnt in alm:
            if cnt >= 1.70:
                m.append(cnt)

        i += 1

    elif ((gen == "F") or (gen == "f")):
        F.append(gen)
        for item in F:
            print(i,'º individuo ',item)

        alf.append(float(input(f"Informe a altura do {i}º individuo em metros ex => 1.70: ")))
        pesof.append(float(input(f"Informe o peso do {i} individuo em Kg ex => 80: ")))
        print('')
        i += 1

S = (sum(alm) + sum(alf)) / (len(Masculino) + len(F))

z = i - 1

pm = round((len(Masculino) / z ) * 100)
pf = round((len(F) / z ) * 100)

print(f'O grupo é formado por {z} pessoas')
print("A média da altura do grupo foi", S, "metros")
print("A mulher do grupo mais alta tem a altura de", max(alf), "metros e o homem mais baixo do grupo tem", min(alm), "metros")
print("O número de homens que tem altura acima de 1,70 são de ", len(m))
print("O homem mais pesado do grupo tem", max(pesom), "kg")
print("O percentual de homens no grupo é de", pm, "% e de mulheres é de", pf, "%")
print('')
print('By: Vinicius Barbosa')