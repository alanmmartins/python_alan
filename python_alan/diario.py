def valorpagamento():
    diario = []
    
    while True:
        val = float (input('valor da prestação: '))
        atr = int (input('dias atrasados: '))
        multa = 0.03
        multa_dia = 0.001 * atr 
        total = int (val+(val+multa_dia)+(val*multa))
        print (f'o valor a aser pago e de r${total}.')
        diario.append(total)
        
        continuar = input('continuar? S/N:  ').lower()
        if continuar == 'N':
            break
    
    print (f'as prestações pagas de hoje foram {diario}')
    print ('Eccerrado')
        
valorpagamento  ()      