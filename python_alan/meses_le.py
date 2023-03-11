opcao = int(input(f"""

        Escolha uma das opções 

        [1] Adicionar serviços 
        [2] Imprimir relatório
        [3] Sair
"""))

match opcao:
    case 1 :
        entrada = int(input('Quantas tarefas deseja adicionar?'))
        
        M= [0]* entrada
        V= [0]* entrada

        for x in range(len(M) and len(V)):
                M[x] = input(f'Digite o mês de seriço: \n')
                V[x] = int (input(f'Digite o valor do serviço\n'))
                
                    

        entrada2 = int(input(f"""
                               Escolha uma das opçõe a seguir:
                               
                            [2] Imprimir relatório
                            [3] Sair                       """))

        if (entrada2==2):
            print(f'Os meses de serviço foram:\n')
            for x in range(len(M)):
                print(M[x])
            
            for v in V:
                vf = v+v
            print(f'O valor total de serviços no ano foi: ' ,vf )
           

        elif(entrada2==3):
                quit()
        else: 
            print("Opção inválida")
    
    case 2:
        ee = int(input(f"""

                    Sem serviços adcionados até o momento , deseja adcionar algum?
        
                    [1] Adicionar serviços
                    [3] Sair
        
        """))

        if (ee==1):
            entrada = int(input('Quantas tarefas deseja adcionar?'))
            M= [0]* entrada 
            V= [0]* entrada          
            for x in range(len(M) and len(V)):
                M[x] = input(f'Digite o mês de seriço: \n')
                V[x] = int (input(f'Digite o valor do serviço'))
                

            entrada2 = int(input(f"""
                               Escolha uma das opçõe a seguir:
                               
                            [2] Imprimir relatório
                            [3] Sair                       """))

            if (entrada2==2):
                for x in range(len(M)):
                    print(M[x])
                    for v in V:
                        vf = v+v
                print(f'O valor total de serviços no ano foi: ' ,vf )
            
            
            elif(entrada2==3):
                     quit()
            else: 
                    print("Opção inválida")
        elif (ee==3):
            quit()
    
    case 3:
        quit()