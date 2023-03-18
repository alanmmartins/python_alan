#importa modulos 
from tkinter import *
import random
import playsound


def escolha_dificuldade():
    Label(interface_dificuldade,text='escolha a sua dificuldade abaixo',font=('Arial',12),fg='black').pack()
    #
    Button(interface_dificuldade,text='facil-10 errros',font=('Arial',12),fg='black',          
           command=escolha_dificuldade_facil).pack()
    Button(interface_dificuldade,text='Meio-10 errros',font=('Arial',12),fg='black',
           command=escolha_dificuldade_medio).pack()
    Button(interface_dificuldade,text='Dificil-10 errros',font=('Arial',12),fg='black',
           command=escolha_dificuldade_dificil).pack()
    
    #
    def escolha_dificuldade_facil():
        dificuldade.append(10)
        interface_dificuldade.destroy()
        
    def escolha_dificuldade_medio():
        dificuldade.append(8)
        interface_dificuldade.destroy()    
        
    def escolha_dificuldade_dificil():
        dificuldade.append(6)
        interface_dificuldade.destroy()    
        
    def forca(event):    
        cabeca_olhos_nariz = interface_forca.create_oval #cria uma forma oval
        corpo = interface_forca.create_line #cra linha
        boca = interface_forca.create_arc #arco
        try:
            char =crate.get().upper()[0]
        except IndexError:
            pass
        else:
            try:
                int(char)#o q e letra
            except ValueError:
                if char not in letras_escolhidas:
                    letras_escolhidas.append(char)                    
                    for indice in range(len(letras)):
                        if char == letras [indice]:
                            lista_traco[indice] = letras[indice]
                            caractere_vazio['text'] = lista_traco
                            lista.conferencia.appnd(char)
                    if char not in letras:
                        lista.erro.append(char)
                        caracteres_anteriores['text'] = lista_erro
    entrada_dados.set('')
    if len(lista_conferencial) == len(letras):
        mensagem_final['text'] = 'jogo ganho parabens'
        mensagem_final['fg'] = 'green'
        caracter.destroy()
        button(interface,text='finalizar',font=('Arial',12),fg='red',command=quit).pack()
    if len(lista_conferencial) == len(letras):
        mensagem_final['text'] = 'erros maximos'
        mensagem_final['fg'] = 'red'
        caracter.destroy()
        button(interface,text='finalizar',font=('Arial',12),fg='red',command=quit).pack()
      
     #bonequinho
    if len(lista_erro) == 1: #cabeçç
        cabeca_olhos_nariz(165,95,215,140,fill='gray',outline='black')
    if len(lista_erro) == 2:#corpo
        corpo(190,140,190,235)
    if len (lista_erro) == 3:#braco
        corpo(190,140,130,190)
    if len (lista_erro) == 4:#braco2
        corpo(190,140,250,190) 
    if len (lista_erro) == 5:#perna
        corpo(190,235,125,300)       
    if len (lista_erro) == 6:#perna2
        corpo(190,140,250,190)  
    if len (lista_erro) == 7:#olho
        cabeca_olhos_nariz(175,105,185,115,fill='white',outline='black')
    if len (lista_erro) == 8:#olho2
        cabeca_olhos_nariz(195,105,205,115,fill='white',outline='black') 
    if len (lista_erro) == 9:#nariz
        cabeca_olhos_nariz(187.5,117.5,192.5,122.5,fill='white',outline='black')       
    if len (lista_erro) == 7:#olho
        bca(165,125,205,130,fill='white')
        
def quit(): #finaliza
    interface.destroy()    
    
    
playsound.playsound('musica_fundo.mp3',block = False) 

#leitura
with open('palavras.txt') as arq:
    leitura = arq.readlines()
    palavra = random.choice(leitura).split('\n')[0].upper()
    #dcdcdcddc
    #        
   #

                
#                               
letras = []
lista_traco= [] 
lista_erro = []
ltras_escolhidas =[]
lista_conferencial = []
dificuldade =[]

#armz dados na lstas
for indice in range(len(palavra)):
    letras.append(palavra[indice])
    lista_traco.append(' ___ ')
    
interface_dificuldade = Tk()
escolha_dificuldade()
interface_dificuldade.mainloop()

if len(dificuldade) == 1:
    interface = Tk
    #canvas
    interface_titulo=Canvas(interface) 
    interface_titulo.pack(side=TOP)
    interface_forca = Canvas(interface,width=400,height=400)
    interface_forca.pack(side=TOP)
    interface_texto = Canvas(interface,width=400,height=400)
    interface_forca.pack(side=TOP)
    
    #
    #
    
    interface_forca.create_rectangle(10,400,400,390,fill='yellow')
    #
    interface_forca.create_rectangle(10,400,20,30,fill='yellow')
    interface_forca.create_rectangle(10,400,400,40,fill='yellow')
    interface_forca.create_rectangle(180,40,200,50,fill='red')
    interface_forca.create_rectangle(187.5,50,192.5,90,fill='black')
    interface_forca.create_oval(160,90,220,145,fill='black')
    interface_forca.create_oval(165,95,215,140,fill='white')
    
    #
    Label(interface_titulo,text='bem vindo ao jogo da orca',font=('arial',12),fg='black').pack()
    Label(interface_titulo,text= 'digite a sua letra;\n',font=('arial',12),fg='black').pack()
    
    entrada_dados = StringVar()
    caracter = Entry(interface_texto,textvariable=entrada_dados)
    #
    #
    caracter.pack()
    caracter.bind('<return>',forca)
    
#
    caracter_vazio = Label(interface_texto,text=traco)
    caracter_vazio.pack()
    
    #
    Label(interface_texto,text='letras erradas:').pack()
    caracteres_anteriores = Label(interface_texto,text=lista_traco)
    caracteres_anteriores.pack()
    
    #
    mensagem_final = Label(interface_texto,text='')
    mensagem_final.pack()
    interface.mainloop()
    
    
    
    
    
    
    