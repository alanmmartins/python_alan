print('*****************menu****************')
print("")
print('prato____________________________preço')
print('codigo prato_____________________preço')
print('[1]______peixe ao molho_________R$100.00')
print('[2]______macarrao ao molho______R$500.00')
print('[3]______frango a parmegiana____R$655.00')
print('[4]______file mignon____________R$99.00')
print('[5]______churrasco______________R$879.00')
print("")
input ('informe o codigo do prato:  ')
menu = {
     'peixe ao molho':100.00,
     'macarrao ao molho':500.00,
     'frago':655.00,
     'file':99.00,
    'churrasco':879.00 ,       
 }
print("codigo do prato e :")
for prato, preço in menu.items():
    print(f"{prato}: R${preço}")
    
