print ('nome do time de futebol')
time = input()
match  time:
    case 'flamengo' | 'fluminense '| 'vasco'| 'botafogo':
        print('carioca')
    case 'sao paulo'| 'santos'| 'palmeiras'| 'corinthians':
        print ('e um time paulista')
    case _:
        print ('outro estado')
                