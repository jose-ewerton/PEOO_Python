from Revista import Edicao, Revista

r = Revista(1, "Abramus", "Música e Arte")

r.adicionar_edicao(1,"25 de setembro de 2019", 24)
r.adicionar_edicao(2,"28 de dezembro de 2019", 13)
r.adicionar_edicao(3,"1 de janeiro de 2020", 33)

r.apresentar()