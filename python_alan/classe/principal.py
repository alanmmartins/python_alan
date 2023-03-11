class teste: #classe principal
    def __init__(self, valor): #metodo condrutor da calsse
        self.x = valor#referencia para  o objeto
        self.y = valor
    def soma (self):
        #total = self.x * self.y * self.x 
        total = self.x * self.y
        return 'soma realizada: ' +str(total)
calc = teste (3)#inserindo um objeto
c = calc.soma()
print(c)    