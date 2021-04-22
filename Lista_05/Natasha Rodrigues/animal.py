print('Classe:')
print('Animal')
print('-'*12)       
class Animal:
    def __init__(self, especie, cor, porte):
        self.especie = especie
        self.cor = cor
        self.porte = porte
        print('Atributos:')
        print(self.especie)
        print(self.cor)
        print(self.porte)
        print('-'*12)
        print('Métodos:')

    def correr(self):
        print(f'O {self.especie} esta correndo.')

    def lamber(self):
        print(f'O {self.especie} esta se lambendo.')

if __name__=="__main__":
        especie = input("Informe a especie do animal: ")
        cor = input("Informe a cor do {}: ".format(especie))
        porte = input("Informe o porte do {} (pequeno, medio, ou grande): ".format(especie))
        a1 = Animal(especie, cor, porte)
        corre = input("O {} esta correndo, sim ou não? ".format(especie)).upper()
        if corre == "SIM":
            a1.correr()
        elif corre == "NÃO":
            lambe = input("O {} esta se lambendo, sim ou não? ".format(especie)).upper()
            if lambe == "SIM":
                a1.lamber()