
vetorh_homem = []
vetorh_mulher = []
vetorp_homem = []
vetorp_mulher = []
vetorhomens = []
vetormulheres = []
a = 0

while a < 15:
    print("-    -   -   -   -   -   -   -")
    sexo = str(input("Qual seu gênero? \nM - macho / F - fêmea --> "))
    if sexo == 'M':
        vetorhomens.append(sexo)
        h = float(input("Qual sua altura? "))
        vetorh_homem.append(h)
        p = float(input("Qual seu peso? "))
        vetorp_homem.append(p)

        homarrao = []
        for c in vetorh_homem:
            if c >= 1.70:
                homarrao.append(c)
        a += 1
    elif sexo == 'F':
        vetormulheres.append(sexo)
        h = float(input("Qual sua altura? "))
        vetorh_mulher.append(h)
        p = float(input("Qual seu peso? "))
        vetorp_mulher.append(p)

        a += 1
    else:
        print("Por favor, siga a regra!")
  

#MEDIA
somah = (sum(vetorh_mulher) + sum(vetorh_homem)) / (len(vetorhomens) + len(vetormulheres))
print(30*"-")
print("A média da altura do grupo é %.2f m" %somah)
#MULHER MAIS ALTA E HOMEM BAIXO
print("A mulher mais alta tem a altura de {}m e homem mais baixo tem a altura de {}m." .format(max(vetorh_mulher), min(vetorh_homem)))
#HOMENS 1.70
print("A quantidade de homens acima de 1.70 são: ", len(homarrao))
#HOMEM PESADO
print("O homem mais pesado tem {}kg" .format(max(vetorp_homem)))
#HOMENS E MULHERES
porh = vetorhomens % 15
porm = vetormulheres % 15
print("A porcentagem de mulheres são {} % e de homens {} % " .format(vetormulheres, vetorhomens))




