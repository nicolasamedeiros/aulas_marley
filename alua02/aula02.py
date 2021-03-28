from googletrans import Translator as Tr 

class Frase():
    MEU_TRADUTOR = Tr()

    def __init__(self, texto):
        self.texto = texto

#metodo detection pra ver se é um str

    def Detectar_txt(self):
        #se tipo for uma string ele vai mostar que é um texto se não é outra coisa
        if (type(self.texto) == str):
            return True
        else:
            return False
    
    def Detectar_idioma(self):
        #vai conferir se é um str para não dar erro
        if (self.Detectar_txt() == True):
            return self.MEU_TRADUTOR.detect(self.texto).lang
        else:
            pass

    def Traduzir(self):
        #Vai pegar a string e vai traduzir
        if (self.Detectar_txt() == True):
            return self.MEU_TRADUTOR.translate(self.texto,src=self.Detectar_idioma(), dest="pt").text
        else:
            pass
            


frase1 = Frase("This is a test")
frase1.Detectar_txt()
print(frase1.Detectar_txt())
print(frase1.Detectar_idioma())
print(frase1.Traduzir())
