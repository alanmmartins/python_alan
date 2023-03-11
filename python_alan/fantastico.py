import turtle 
def desenharQuadradoMulticolorido(t, tam):
    for i in ['blue','purple', 'green', 'black']:
        t.color (i)
        t.forward(tam)
        t.left(90)
dq = turtle.Screen()
dq.bgcolor('lightblue')
tess = turtle.Turtle()
tess.pensize(3)
tamanho = 50
for i in range(20):
    desenharQuadradoMulticolorido (tess, tamanho)
    tamanho = tamanho 
    tess.forward(10)
    tess.right(18)
    
    tess.forward(-10)
    tess.right(18)
    
dq.exitonclick ()           
        