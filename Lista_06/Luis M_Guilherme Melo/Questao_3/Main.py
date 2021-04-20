from Endereco import Pessoa, Endereco


gente = Pessoa(69420, "luis", 704)
gente2 = Pessoa(1113, "pinho", 190)
endereco1= Endereco(294, "cap jose", "cm", "RN", "Brazil")
endereco2= Endereco(294, "cap jose", "cm", "RN", "Brazil")
endereco3= Endereco(420, "cracolandia", "Sao Paulo", "SP", "Brazil")
gente.inserir_endereco(endereco1)
gente.inserir_endereco(endereco2)
gente2.inserir_endereco(endereco3)
gente.listar_enderecos()
gente2.listar_enderecos()
