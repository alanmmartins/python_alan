print('******************************************************')
print('**************CRIANÇA ESPERANÇA***********************')
print('******************************************************')
print('+++++++++++++++++obrigado---++++++++++++++++++++++++++')
print('******************************************************')
print('[1]para doar 10 reais')
print('[2]para doar20 reais')
print('[3]para doar30 reais')
print('[4]para doar outros valores')
print('[5]para cancelar')
d = int(input())
match d:
    case 1:
        valor = 10
    case 2:
        valor = 20
    case 3:
        valor = 30
    case 4:
        valor = int(input('qual e o valor da doação R$: '))
    case 5:
        print('você nao vai ajudar crianças hoje') 
print('******************************************************')
print(f'sua doação foi de {valor} reais')
print('*****************************************************')
print('**********************obrigado***********************')                       