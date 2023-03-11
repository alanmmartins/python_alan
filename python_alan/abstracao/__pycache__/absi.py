from abs import *
class infantil(filmes):
   
    def __init__(self, nome, base):
         filmes.nome = nome
         filmes.base = base
    
    def r_diaria(self):
        return self.base * 1.1
    