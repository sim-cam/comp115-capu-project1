import turtle

wn = turtle.Screen()
wn.bgcolor('black')
pip = turtle.Turtle()
pip.speed(0)
pip.pensize(8)

def draw_petal(radius, angle):
    pip.circle(radius, angle)
    pip.left(180 - angle)
    pip.circle(radius, angle)
    pip.left(180 - angle)

def draw_diamond(length):
    for i in range(2):
        pip.forward(length)
        pip.left(60)
        pip.forward(length)
        pip.left(120)

def draw_circle(circle, angle):
    pip.circle(circle)
    pip.left(angle)

def lil_circles(num_circ, circle, angle):
    for i in range(num_circ):
        pip.up()
        pip.forward(300)
        pip.down()
        pip.circle(circle)
        pip.up()
        pip.backward(300)
        pip.right(360 / angle)

for i in range(15):
    pip.color('DodgerBlue3')
    draw_circle(150, 60)

for i in range(24):
    pip.down()
    pip.color('LightBlue2')
    draw_diamond(150)
    pip.left(15)


for i in range(10):
    pip.color('LightYellow')
    draw_petal(200, 36)
    pip.left(36)

for i in range(1):
    pip.color('plum1')
    lil_circles(8, 5, 6)

for i in range(20):
    pip.down()
    pip.color('plum1')
    draw_petal(100, 18)
    pip.left(18)

wn.exitonclick()
    
