from produto import Produto

p = Produto()
print(p)

p.adicionar("001", "feijão", "Curimataú", "R$ 6,00") #aqui se passa parametro
'''
p.adicionar(cod, nome, marca, preco)
p.adicionar(cod, nome, marca, preco)
p.adicionar(cod, nome, marca, preco)
'''
p.listar() # aqui se espera um print ou return

cod = int(input("Digite o código do produto que deseja deletar: "))
p.deletar(cod) # para deletar usem o id do produto

p.listar() # aqui se espera um print ou return

cod = int(input("Digite o código do produto que deseja atualizar: "))
p.atualizar(cod) #para atualizar usem o id do produto

p.listar() # aqui se espera um print ou return