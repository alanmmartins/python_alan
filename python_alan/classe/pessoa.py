class pessoa :
    def __init__(self,nome ,sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo
        
    def desativar (self):
        self.ativo = False
        print ('A pessoa foi desativada com sucesso')
        
if __name__ == '__main__':
    pessoa1 = pessoa('alan', 'M', '470.010.278-04', True) 
    pessoa2 = pessoa('alana', 'f', '570.010.278-04', False) 
    pessoa1.desativar()      
