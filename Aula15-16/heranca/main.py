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


c = Cachorro()
print(c.nome,c.peso,c.som)
c.alimentacao_filhote()
c.alimentacao_adulta()
c.comportamento() #verificar se esse metodo existe na classe, senão ele vai olhar na classe pai

'''
c.metodo_classe()
c.metodo_estatico()



Lista 1,2,3,4,5,6
50% da nota

Mini-projeto individual
50%


Abstração, Encapsulamento, Herança e Polimorfismo (4 pilares da POO)

Abstração -- Do mundo real para a programação
    Objeto Pessoa - abstrai-se na programação aquilo que não é relevante ao projeto ou código
    Ex.: Para fazer um cadastro (Nome, e-mail, senha) -- isso é relevante no meu cadastro
    A cor dos olhos, cabelo, gosto musical

Encapsulamento -- Proteger atributos e métodos de acesso indevido
    -- Modificadores de acesso - public, protected e private
    Um bom encapsulamento é aquele que tem seus atributos privados, sendo acessado apenas pelos métodos acessores (Setter e Getter) e métodos devem ser públicos;


Herança -- Superclasses (Pai ou mãe) e subclasses (Filhas)
    Ex.: Formulário de cadastro básico (nome, e-mail, senha), para criar um novo formulário de cadastro eu irei extender ou herdar do meu antigo e acrescentar novas funcionalidades. 

Polimorfismos -- É a capacidade de sobrepor ou sobreescrever os métodos de uma classe, seja a própria ou herdada;

    Sobreposição -- a palavra significa a grosso modo por acima.   
    Sobreescrição -- é no sentido de ter uma classe com mesmo nome mais que recebe diferentes atributos;


Fora dos 4 pilares mais que é importante!

É o relacionamento entre os objetos -- é a simulação na programação do mundo real, mostrando como objetos se comunicam, acontece então a troca de informações.   
Assossiação --  a nível de atributos -- não existem uma dependencia para funcionalidade de ambos os objetos

Agregação -- a nível de atributos também  -- existe uma dependencia para o bom funionamento do objeto todo com relação a sua parte (se um objeto é chamado de todo quer dizer que ele quem agrega o outro que é denominado de parte)

Composição -- a nivel de instancia da classe parte -- a classe todo contem a classe parte, sendo assim a classe parte só deverá existir enquanto existir a classe todo;


































































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
















