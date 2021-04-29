from produto import Produto
from item_pedido import ItemPedido
from pedido import Pedido

p1 = Produto("00001", "Maça", 5.00)
p2 = Produto("00002", "batata", 7.00)
p3 = Produto("00003", "Prestigio",5.40)

condicao = True

pedido = Pedido()

while condicao == True:
    print("Bom dia usuário, segue lista de produtos")
    print("Produto 01: ",p1.codigo,p1.descricao,p1.valor)
    print("Produto 02: ",p2.codigo,p2.descricao,p2.valor)
    print("Produto 03: ",p3.codigo,p3.descricao,p3.valor)
    escolha = input("Escolha 1 para adicionar e 2 para remover da lista: ")
    if (escolha == '1'):
        codigo = input("Digite o código do produto que deseja: ")
        quant = int(input("Digite a quantidade desse produto: "))
        if (codigo == p1.codigo):
            pedido.adicionar_item(p1,quant)
        elif (codigo == p2.codigo):
            pedido.adicionar_item(p2,quant)
        elif (codigo == p3.codigo):
            pedido.adicionar_item(p3,quant)
        else:
            print("Insira um código válido!")
    elif (escolha == '2'):
        if (len(pedido.lista_pedidos) == 0):
            print("Lista de pedidos vazia!")
        else:
            print("Entra na função")
            pedido.remover_item()       
    condicao = True

'''
p1.detalha_produto()
p2.detalha_produto()
p3.detalha_produto()
'''


