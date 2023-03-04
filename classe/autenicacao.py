class pessoa :
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
class pessoaauteticavel(pessoa):   
    def __init__(self, nome, sobrenome, idade, usuario, senha): 
        pessoa.__init__(self, nome, sobrenome, idade)
        self.usuario = usuario
        self.senha = senha
        
    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha
    
p = pessoaauteticavel('alan', 'martins', 24, 'jade','secreta')
p2 = pessoaauteticavel('alana', 'martins', 24, 'jade','secreta')

print(pessoa.nome_completo(p))
print(pessoaauteticavel.autenticar(p, 'jade', 'secreta'))     #jade e a senha entao e true
print('--------------------------------')
print(pessoa.nome_completo(p2))
print(pessoaauteticavel.autenticar(p2, 'jde', 'secreta'))