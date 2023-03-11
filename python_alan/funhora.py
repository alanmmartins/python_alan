def hora(h,m):
    b =h /12
    if b <= 1:
        hh = str (h)
        print('sua hora: '+ hh +' : ', end='' )
    elif b > 1 and b < 2: 
        hhh = str (h - 12)
        print('sua hora: '+ hhh +' : ', end= '')
    else: 
        print(' formato de hora invalido')  
    if b <= 1 and m <= 60 :
        print(m , 'a.m')
    elif b > 1 and m <= 60:
        print (m, 'p.m')
    else: 
        print ('formato de minutos invalido') 

while True:
    print ('digite 500 para sair ')
    h = int(input('informe a hora: '))
    if h == 500:
        break
    m = int (input('informe os minutos : '))
    hora (h , m )           