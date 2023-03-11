valor =  float(input('digite o valor da mercadria' ) )
op = int(input('digite 1 para parcelar 2 pagamento a vista' ) )
match op:
    case 1:
        if valor>1000:
            parcelas = valor/5
            print(f'com esse valor voce pode parcelar em 5x de r$ {parcelas} ')
        else:
            parcelas = valor/3
            print(f'com esse valor voce pode parcelar e 3x de r$ {parcelas} ')
    case 2:
        avista = (valor*0.9)
        print (f'com esse valor e : {avista} ')
    case _:
        print ('opção invalida ')    