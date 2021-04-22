print('='*50)
print("                 LIST_1_QUEST_1 ")
print('='*50)
print('\n')
#definir um conjunto de dados
#nesse conjunto deve conter a altura peso e o gênero(M ou F) de 15 pessoas
#calcular e informar a média de altura do grupo
#mostrar a mulher mais alta e o homem mais baixo
#mostrar o número de homens com mais de 1,70 m de altura
#mostrar o homem mais pesado
#calcular o percentual de homens e de mulheres


peso_homem = []
peso_mulher = []
altura_homem = []
altura_mulher = []
genero_homem = []
genero_mulher = []
a = 0

while a < 15:
    genero = str(input("Qual é o seu gênero?\nDigite 'f' para feminino, 'm' ou para masculino: "))
    if genero == 'm':
        genero_homem.append(genero)
        altura_h = float(input('Qual é a sua altura? '))
        altura_homem.append(altura_h)
        peso_h = float(input('qual é o seu peso? '))
        peso_homem.append(peso_h)

        homem_alto = []
        homem_baixo = []
        for c in altura_homem:
            if c >= 1.70:
                homem_alto.append(c)
            else:
              homem_baixo.append(c)

        a += 1
    elif genero == 'f':
        genero_mulher.append(genero)
        altura_m = float(input("qual é a sua altura? "))
        altura_mulher.append(altura_m)
        peso_m = float(input("Qual é o seu peso?  "))
        peso_mulher.append(peso_m)
        print('_' * 50)
        mulher_alta = []
        mulher_baixa = []
        for c in altura_mulher:
            if c >= 1.70:
                mulher_alta.append(c)
            else:
              mulher_baixa.append(c)


        a += 1
media = (sum(altura_mulher)+ sum(altura_homem)/ (len(genero_homem)+len(genero_mulher)))
print('='*50)
print("A média da altura do grupo: {}".format(media))
print("A mulher mais alta tem a altura de {}m\nO homem mais baixo tem a altura de: {}m." .format(max(altura_mulher), min(altura_homem)))
print("O homem mais pesado tem {}kg" .format(max(peso_mulher)))
print("Quantidades de homens a cima de 1.70: {} ".format(len(homem_alto)))

porcentegem_homens = len(genero_homem)* 100/15
porcentagem_mulher = len(genero_mulher)* 100/15
print("porcentagem de mulheres: {} %\nporcentagem de homens: {} %".format(porcentagem_mulher, porcentegem_homens))