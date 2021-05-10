from produtos02 import  Produto


p1 = Produto()
p2 = Produto()
p3 = Produto()
p4 = Produto()
p5 = Produto()
      
print("----------Olá! Segue a lista de produtos:----------")
p1.adicionar('1234', "café","Santa Clara",'R$ 1,50')
p2.adicionar('0425', "leite","Itambé", 'R$ 2, 89')
p3.adicionar('1478', "manteiga","Delicata",'R$ 3,99')
p4.adicionar('6932', "Arroz", "Namorado",'R$ 4,00')
p5.adicionar('1264', "sabão","Ypê", 'R$ 5,10')

p1.listar()
p2.listar()
p3.listar()
p4.listar()
p5.listar()