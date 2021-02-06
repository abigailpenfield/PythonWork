import turtle

colors = ['cornflowerblue', 'lightpink', 'mediumspringgreen', \
          'mediumslateblue', 'lightcoral']
pen = turtle.Pen()
pen.speed(0)
turtle.bgcolor('black')
for x in range(250):
    pen.pencolor(colors[x%5])
    pen.width(x/100+1)
    pen.forward(x)
    pen.right(50)
    pen.backward(x+5)
    pen.left(25)
    
##turtle.reset()







