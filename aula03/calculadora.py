# calculadora tem que ter o metodo somar, dividir, multiplicar e subtrair
# 3 atributor valor 1, operação e valor 2 
# 1 metodo para realizar o calculo

class calculadora():

    def __init__(self, num1, operação, num2):
        self.num1 = num1
        self.num2 = num2
        self.operação = operação

    def Somar(self):
        cal = self.num1 + self.num2
        return cal

    def Subtrar(self):
        cal2 = self.num1 - self.num2
        return cal2
    
    def Multiplicar(self):
        cal3 = self.num1 * self.num2
        return cal3

    def Divisao(self):
        cal4 = self.num1 / self.num2
        return cal4
    
    def Calcular(self):
        # Preciso colocar algo pra fazer a ação
        if self.operação == "+":
            return self.Somar()
        elif self.operação == "-":
            return self.Subtrar()
        elif self.operação == "*":
            return self.Multiplicar()
        elif self.operação == "/":
            return self.Divisao()
#o usuario tem que digitar um numero, dai eu vou ter que dividir
#usando split e dps calcular
entrada = input("Digite os valores: ")
entrada_split = entrada.split(" ")
calcular = calculadora(int(entrada_split[0]), entrada_split[1], int(entrada_split[2]))
result = calcular.Calcular()
print(result)