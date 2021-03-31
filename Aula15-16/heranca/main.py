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
c.comportamento()
c.metodo_classe()
c.metodo_estatico()

'''

Lista 1,2,3,4,5,6
50% da nota

Mini-projeto individual
50%
































Aquecimento - Defina uma classe ObjetoGrafico com atributos cor_de_preenchimento, preenchida, cor de contorno

3 classe Retangulo, Circulo e Triangulo
Todas devem ser subclasses de ObjetoGrafico e possuir os métodos área e perímetro


Metodos abstrato - criar uma classe e manda a tarefa para outra classe definir (Subclasses)


Metodos estáticos - não tem o self e só pode ser chamado pela classe

Conta.imprimir()
Nos metodos de classe também não são acessiveis, apenas com 
class Conta:
    num = 1000

    def teste(self):
        return Conta.num


Atributos da Classe - 

class Cachorro:
    nome = 'Rex'
    cor = 'marrom'
dog = Cachorro()
dog.nome
dog.cor

Cachorro.nome
Cachorro.cor


'''
















