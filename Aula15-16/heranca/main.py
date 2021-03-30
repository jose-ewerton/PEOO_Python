from classes import Mamifero,Gato, Cachorro

m = Mamifero("Porco",60)
print(m.nome,m.peso)
m.alimentacao_filhote()
#m.alimentacao_adulta() ERRADO !!!!!!!!!!!!!

g = Gato()
g.nome = "Gato"
g.peso = 6
print(g.nome,g.peso)
g.alimentacao_filhote()
g.alimentacao_adulta()  #visivel ou só existe na classe filha (Gato)


c = Cachorro("Cachorro",20)
print(c.nome,c.peso,c.som)
c.alimentacao_filhote()
c.alimentacao_adulta()

'''
#herança múltipla e polimorfismo
Lista 1,2,3,4,5,6
50% da nota

Mini-projeto individual
50%
'''