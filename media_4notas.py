nome = input ('digite seu nome: ')
nota1 = int(input ('digite a primeira nota : '))
nota2 = int(input ('digite a segunda nota : '))
nota3 = int(input ('digite a terceira nota : '))
nota4 = int(input ('digite a quarta nota : '))
m =(nota1, nota2, nota3, nota4)/4
if m>= 7:
    print(f'{nome}sua media e {m} voce foi aprovado')
elif m<5:
    print(f'{nome}sua media e {m} voce foi reprovado')
else :
    print(f'{nome}sua media e {m} voce esta de recuperação')       