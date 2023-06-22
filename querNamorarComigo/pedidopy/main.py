import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image


root = tk.Tk()
root.title('VAI DAR NAMOROOOO?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 60 and abs(e.y - button_1.winfo_y()) < 60:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        'Tão facil aceitar né', 'Agora tu tem um namorado gatinha!!!!')


def denied():
    button_1.destroy()

# """ def adicionar_imagem():
#    # Carregar a imagem
#   image = Image.open("C:\Users\DELL\Desktop\querNamorarComigo\img")


#image = image.resize((300, 300), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(image)
# label.configure(image=photo)
#label.image = photo
#janela = tk.Tk()
#botao = tk.Button(janela, text="Adicionar imagem", command=adicionar_imagem)
# botao.pack()
#label = tk.Label(janela)
# label.pack()
# """
margin = Canvas(width=500,
                bg='#ffc8dd',
                height=300,  # altura
                bd=0, highlightthickness=0,
                relief='ridge')
margin.pack()
text_id = Label(bg='#ffc8dd',  # O background ou bg é um atributo do Tkinter
                text='Você Quer namorar comigo?',
                fg='#f50505',  # Fg – Cor do texto
                font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(text='Não',
                     bg='#bd5924',
                     command=denied,
                     relief='ridge',
                     bd=3,
                     font=('Montserrat', 14, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(text='Sim',
                     bg='#03fc0b',
                     relief='ridge',
                     bd=5,
                     command=accepted,
                     font=('Montserrat', 14, 'bold'))
button_2.pack()


root.mainloop()


# pip install pillow
