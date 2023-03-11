class pessoa:
    def __init__(self, nome, idade,cpf):
        self.nome = nome
        self._idade = idade
        self._cpf = cpf
        
ps = pessoa('alan','24','125.947.658.36')
print(ps.nome)
print(ps._idade) 
print(ps._cpf)

"""publico " " = cpf
    privado"_" = _cpf 
    protegido "__" = __cpf"""