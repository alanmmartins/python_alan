import turtle
def desenhaBarra(t, altura):
    t.begin_fill()
    t.left(90)
    t.forward(altura)
    t.write('' + str(altura))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()
xs = [5,10,20,25,30,260,220] 
alturamax = max (xs) 
numbarras = len (xs)
moldura = 10
tess = turtle.Turtle()
tess.color('blue')
tess.fillcolor('black')
tess.pensize(3)
wn = turtle.Screen() 
wn.bgcolor ('lightgreen')
wn.setworldcoordinates(0-moldura,0-moldura,40*numbarras+moldura,alturamax+moldura)
for a in xs:
    desenhaBarra(tess, a)
wn.exitonclick()        