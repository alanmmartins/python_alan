from abc import ABC, abstractclassmethod

class filmes(ABC):
    nome = None
    base = None
    
    @abstractclassmethod
    def r_diaria9(self):
        pass