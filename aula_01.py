class cachorro():
    ANIMAL = True

    def __init__(self, cor_pelo, cicatriz, tamanho):
        self.cor_pelo = cor_pelo
        self.cicatriz = cicatriz
        self.tamanho = tamanho
    
    def Latir(self, barulho):
        latir = "Latir {}".format(barulho)
        print(latir)
    def Andar(self, anda):
        if(anda == True):
            print("Andando")
        else:
            print("Parado")
    def Comer(self, come):     
        if(come == True):
            print("Comendo")
        else:
            print("Não comendo")
    def get_tamanho(self):
        print(self.tamanho)
    def get_cor_pelo(self):
        print(self.cor_pelo) 
    def get_cicatriz(self):
        print(self.cicatriz)       


    
cachorro1 = cachorro("Branco", False, 16.50)
cachorro2 = cachorro("Preto", True, 17)        

cachorro1.Latir(barulho="Au Au")
cachorro1.Andar(anda= False)
cachorro1.Comer(come= False)
cachorro1.get_tamanho()
cachorro1.get_cor_pelo()
cachorro1.get_cicatriz()

print("")

cachorro2.Latir(barulho="Ruf Ruf")
cachorro2.Andar(anda= True)
cachorro2.Comer(come= True)
cachorro2.get_tamanho()
cachorro2.get_cor_pelo()
cachorro2.get_cicatriz()
            