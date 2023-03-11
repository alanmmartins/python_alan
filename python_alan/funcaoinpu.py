def imprimiLinha(numero):
    for n in range (1, numero + 1):
        print((' {} ').format(n), end='')
    print()

def imprimeSequencia(numero):
    for numero in range (numero + 1):
        imprimiLinha(numero)
       
numero = input('digite um numero ai :  ') 
imprimeSequencia(int(numero))                 