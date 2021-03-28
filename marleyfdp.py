class human():
    SER_HUMANO = True
    
    def __init__(self, cor_pele, peso, altura):
        self.cor_pele = cor_pele
        self.peso = peso
        self.altura = altura


    def get_cor_pele(self):
        print(self.cor_pele)
    
    def get_altura(self):
        print(self.altura)

    def get_peso(self):
        print(self.peso)
    
    def Cabelao(self, cabelo):
        if (cabelo == True):
            print("Tem cabelo")
        else:
            print("carecão kkkk")
    
    
    def Tatuagem(self, tattoo):
        if (tattoo == True):
            print("O cara tem skin")
        else:
            print("O mano não tem skin kkk")


human1 = human("Branco", 71.50, 1.82)
human1.get_cor_pele()
human1.get_altura()
human1.get_peso()
human1.Cabelao(cabelo = True)
human1.Tatuagem(tattoo = True)

print("")

human2 = human("Negro", 82.30, 1.91)
human2.get_cor_pele()
human2.get_altura()
human2.get_peso()
human2.Cabelao(cabelo = False)
human2.Tatuagem(tattoo = False)
