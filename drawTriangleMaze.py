import turtle

turtle.setup(width = 500, height = 500)
t = turtle.Pen()
t.shape("turtle")
t.width(3)

color_change = 0
colors = [ "red", "blue", "green", "black"]


for i in range(0, 303, 8):
    t.forward(i)
    t.left(120)
    t.pencolor(colors[color_change])
    color_change = color_change + 1
    if color_change >= 4 :
        color_change = 0
    
    
    

