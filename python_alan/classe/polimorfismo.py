class pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self._cpf = cpf
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def id(self):
        return self._cpf

class cliente (pessoa):
    def __init__(self, nome, sobrenome, cpf, codigo): 
        super().__init__(nome, sobrenome, cpf,)
        self._codigo = codigo
        
    def id(self):
        return self._codigo           
    
class funcionario (pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula): 
        super().__init__(nome, sobrenome, cpf)
        self._matricula = matricula
        
    def id(self):
        return self._matricula
    
cliente1 = cliente('ze','pequeno','123.456.789-99','xxx-01')
funcionario1 = funcionario('alan','martins','470.010.278-04','000-01')  
funcionario2 = funcionario('jo','linha','201.656.569-33','000-02')         

print (cliente1.nome_completo())
print (cliente1.id())
print("----------------------------")
print(funcionario1.nome_completo())
print(funcionario1.id())
print("----------------------------")
print(funcionario2.nome_completo())
print(funcionario2.id())
