print('*****************seviços****************')
print("")
print('_________________________________________')
print('[1]______informar novo serviço')
print('[2]______exibir relatorio')
print('[3]______sair')
print("_________________________________________")


x = int(input())
if (x >= 1) and (x <= 3):
     match x:

        case 1: #> > > > > > > > > > CASE 1 < < < < < < < < < <
            valor = 1
            print('Você escolheu a opção 1 -> informar serviço')
            print('')
            
            serviço = input ('valor do serviço serviço : ')
            
            print(f'valor doserviço e  {serviço} ')
              
        case 2: #> > > > > > > > > >case 2 < < < < < < < <     
            valor = 2
            print('Você escolheu a opção 2 -> exibir relatorio')
            print('')
            
            relatorio_ano = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,]
            #12 meses
            print('relarorio anual :') 
            print(sum(relatorio_ano))
                    
        case 3: #> > > > > > > case 3< < < < <  < < < <  
            valor = 3
            print('Você escolheu a opçao 3 -> sair ')
            print('sair') 
          
             