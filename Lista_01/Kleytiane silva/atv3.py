votos = [input("Digite sua idade e opiniao sobre o filme (ótimo 3 ,bom 2 ,regular 1): ").split() for c in range(15)]
print()

list1 = [int(c[0]) for c in votos if c[1] == '3']
print("Média de idade das pessoas que responderam ótimo", sum(list1)/len(list1))

list2 = [1 for c in votos if c[1] == '1']
print("Quantidade de pessoas que responderam regular", len(list2))

list3 = [1 for c in votos if c[1] == '2']
print("Porcentagem das pessoas que responderam bom", len(list3)/len(votos)*100)