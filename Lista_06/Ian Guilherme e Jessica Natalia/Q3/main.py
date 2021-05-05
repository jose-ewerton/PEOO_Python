from Pessoa import Endereco, Pessoa

p = Pessoa(1,"Rodrigo","123.456.789-00")

l1 = Endereco(467,"Alberto Maranhão","São Gonçalo do Amarante", "RN","Brasil")
l2 = Endereco(192,"Da Mangabeira", "Extremoz","RN","Brasil")

p.adicionar_endereco(l1)
p.adicionar_endereco(l2)

p.apresentar()

p.remover_local(467)

p.apresentar()