print('======================================================')
print('Escola o código referente ao prato de sua preferência:')
print('======================================================')
print('')

print('[1] - Peixe ao Molho --- R$115,00')
print('[2] - Macarrão com Almôndegas --- R$33,00')
print('[3] - Frango a Parmegiana --- R$65,00')
print('[4] - Filé Mignon --- R$78,00')
print('[5] - Churrasco no Prato --- R$70,00')
print('')

x = int(input())
taxa = 0.5

if (x >= 1) and (x <= 5):
    match x:

        case 1: #> > > > > > > > > > CASE 1 < < < < < < < < < <
            valor = 115
            print('Você escolheu a opção 1 -> Peixe com Molho')
            print('')
            gorjeta = input('Deseja dar uma gorjeta ao Garçom? s = sim ou n = não: ')
            if gorjeta == 's':
                gorjeta = float(input('Qual o valor da sua gorjeta? '))
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                print('')
                if servico == 's':
                    conta = (taxa * valor + valor) + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    conta = valor + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')  
                    print('')
                else:
                    print('VALOR INVALIDO!')

            elif gorjeta == 'n':
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                if servico == 's':
                    conta = taxa * valor + valor
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    print(f'Sua conta deu um total de R${valor},00')
                    print('Obrigado pela preferência')
                    print('')
                else:
                    print('VALOR INVALIDO!')
            else:
                print('OPÇÃO INVÁLIDA!')

        case 2: #> > > > > > > > > > CASE 2 < < < < < < < < < <
            valor = 33
            print('Você escolheu a opção 2 -> Macarrão com Almôndegas')
            print('')
            gorjeta = input('Deseja dar uma gorjeta ao Garçom? s = sim ou n = não: ')
            if gorjeta == 's':
                gorjeta = float(input('Qual o valor da sua gorjeta? '))
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                print('')
                if servico == 's':
                    conta = (taxa * valor + valor) + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    conta = valor + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')  
                    print('')
                else:
                    print('VALOR INVALIDO!')

            elif gorjeta == 'n':
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                if servico == 's':
                    conta = taxa * valor + valor
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    print(f'Sua conta deu um total de R${valor},00')
                    print('Obrigado pela preferência')
                    print('')
                else:
                    print('VALOR INVALIDO!')
            else:
                print('OPÇÃO INVÁLIDA!')  

        case 3: #> > > > > > > > > > CASE 3 < < < < < < < < < <
            valor = 65
            print('Você escolheu a opção 3 -> Frango a Parmegiana')
            print('')
            gorjeta = input('Deseja dar uma gorjeta ao Garçom? s = sim ou n = não: ')
            if gorjeta == 's':
                gorjeta = float(input('Qual o valor da sua gorjeta? '))
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                print('')
                if servico == 's':
                    conta = (taxa * valor + valor) + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    conta = valor + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')  
                    print('')
                else:
                    print('VALOR INVALIDO!')

            elif gorjeta == 'n':
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                if servico == 's':
                    conta = taxa * valor + valor
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    print(f'Sua conta deu um total de R${valor},00')
                    print('Obrigado pela preferência')
                    print('')
                else:
                    print('VALOR INVALIDO!')
            else:
                print('OPÇÃO INVÁLIDA!')   

        case 4: #> > > > > > > > > > CASE 4 < < < < < < < < < <
            valor = 78
            print('Você escolheu a opção 4 -> Filé Mignon')
            print('')
            gorjeta = input('Deseja dar uma gorjeta ao Garçom? s = sim ou n = não: ')
            if gorjeta == 's':
                gorjeta = float(input('Qual o valor da sua gorjeta? '))
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                print('')
                if servico == 's':
                    conta = (taxa * valor + valor) + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    conta = valor + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')  
                    print('')
                else:
                    print('VALOR INVALIDO!')

            elif gorjeta == 'n':
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                if servico == 's':
                    conta = taxa * valor + valor
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    print(f'Sua conta deu um total de R${valor},00')
                    print('Obrigado pela preferência')
                    print('')
                else:
                    print('VALOR INVALIDO!')
            else:
                print('OPÇÃO INVÁLIDA!')   

        case 5: #> > > > > > > > > > CASE 5 < < < < < < < < < <
            valor = 70
            print('Você escolheu a opção 5 -> Churrasco no Prato')
            print('')
            gorjeta = input('Deseja dar uma gorjeta ao Garçom? s = sim ou n = não: ')
            if gorjeta == 's':
                gorjeta = float(input('Qual o valor da sua gorjeta? '))
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                print('')
                if servico == 's':
                    conta = (taxa * valor + valor) + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    conta = valor + gorjeta
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')  
                    print('')
                else:
                    print('VALOR INVALIDO!')

            elif gorjeta == 'n':
                servico = input('Deseja pagar a taxa de serviço? s = sim ou n = não: ')
                if servico == 's':
                    conta = taxa * valor + valor
                    print(f'Sua conta deu um total de R${conta},00')
                    print('Obrigado pela preferência')
                    print('')
                elif servico == 'n':
                    print(f'Sua conta deu um total de R${valor},00')
                    print('Obrigado pela preferência')
                    print('')
                else:
                    print('VALOR INVALIDO!')
            else:
                print('OPÇÃO INVÁLIDA!')                        

else:
    print('Código do prato inválido')