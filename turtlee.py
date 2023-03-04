import turtle
def desenhaQuadrado(t, tam):
    for i in range (4):
        t.forward (tam)
        t.left(45 )
dq = turtle.Screen ()
dq.bgcolor('lightblue')
jan = turtle.Turtle ()

desenhaQuadrado (jan, 5)
desenhaQuadrado (jan, 10)
desenhaQuadrado (jan, 20)
desenhaQuadrado (jan, 30)
desenhaQuadrado (jan, 40)
desenhaQuadrado (jan, 50)
desenhaQuadrado (jan, 60)
desenhaQuadrado (jan, 70)
desenhaQuadrado (jan, 80)



jan.penup()
jan.goto(1 ,10)
jan.pendown ()


dq.exittonclick()      
   
    
    