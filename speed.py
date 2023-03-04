import shutil
import os

origem = 'C:/Users/Aluno/python_alan/origem'
destino = 'C:/Users/Aluno/python_alan/destino'
#extensao = 'jpg'
for nomearquivo in os.listdir(origem):
    #if nomearquivo.endwith(extensao):
    #origem = os.path.join(origem,nomearquivo)    
    #destino = os.path.join(destino,nomearquivo)
    shutil.copy(os.path.join(origem,nomearquivo),(os.path.join(destino,nomearquivo)))