#Draw Redpea
#yeye1214


import turtle as t
from time import sleep


#t.hideturtle()
t.screensize(bg='#2D2D2D')
t.setup(width=1920/1.8, height=1080/1.8, startx=100, starty=100)


###define redpea
def draw_body(initx, inity):

    ###body
    t.pu()
    t.goto(initx, inity)
    t.pd()
    t.pensize(3)
    t.color('black', '#FF6464')
    t.begin_fill()
    t.seth(105)
    t.circle(80, 160)
    t.fd(50)
    t.right(10)
    t.circle(88, 150)
    t.circle(120, 20)
    t.left(20)
    t.fd(30)
    t.left(13)
    t.fd(40)
    t.left(1)
    t.fd(45) 
    t.end_fill()    

    ###Eyes1
    t.pu()
    t.goto(initx + -20, inity + -10)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.color('black','white')
    t.circle(22, 360)
    t.end_fill()
    ###White in eyes
    t.circle(22, 280)
    t.begin_fill()
    t.color('black','black')
    t.circle(22, 180)
    #t.seth(280)
    #t.fd(44)
    t.end_fill()
 
    ###Mouth
    t.pu()
    t.goto(initx-7, inity + -30)
    t.pd()
    t.seth(330)
    t.circle(10, 70)    
    
    ###Z1
    t.pu()
    t.goto(initx + -70, inity + -40)
    t.pd()
    t.pensize(5)
    t.pencolor('yellow')
    t.seth(-5)
    t.fd(25)
    t.right(160)
    t.fd(25)
    t.left(155)
    t.fd(25)
    t.pu()    


def draw_hands(initx, inity):
    t.pu()
    t.pencolor('black')
    t.pensize(3)
    t.goto(initx + -100, inity + -60)
    t.pd()
    t.seth(260)
    t.circle(200,15)
  

def draw_legs1(initx, inity):

    ###RL
    t.pu()
    t.goto(initx + -80, inity + -160)
    t.pd()
    t.seth(265)
    t.fd(30)
    t.pu()

    ###LL
    t.pu()
    t.goto(initx + -70, inity + -175)
    t.pd()
    t.seth(275)
    t.fd(15)
    t.pu()    


def draw_legs2(initx, inity):

    ###RL
    t.pu()
    t.goto(initx + -72, inity + -160)
    t.pd()
    t.seth(273)
    t.fd(30)
    t.pu()

    ###LL
    t.pu()
    t.goto(initx + -78, inity + -175)
    t.pd()
    t.seth(268)
    t.fd(15)
    t.pu()


def grass(initx, inity):
    t.pu()
    t.goto(initx, inity)
    t.seth(105)
    t.color('#50D264')
    t.begin_fill()
    t.pd()
    t.fd(50)
    t.right(160)
    t.fd(40)
    t.left(130)
    t.fd(35)
    t.right(145)
    t.fd(35)
    t.left(120)
    t.fd(40)
    t.right(150)
    t.fd(48)
    t.goto(initx, inity)
    t.pu()
    t.end_fill()

    
##################
#yeye1214#########
##################

    
class pea_first:
    def __init__(self, x, y):
        draw_body(x, y)
        draw_hands(x, y) 
        draw_legs1(x, y)


class pea_second:
    def __init__(self, x, y):
        draw_body(x, y)
        draw_hands(x, y) 
        draw_legs2(x, y)

    
##################
##################
##################


###Draw Redpea
#t.tracer(True)
t.speed(9)
pea_first(200, 0)
sleep(2)
t.clear()


##################
##################
##################


###Move
t.hideturtle()
for i in range(4000):
    t.tracer(False)
    #sleep(...)
    t.clear()
    grass(-50,-220)
    grass(280,180)
    grass(-350,50)
    if i % 32 < 16:
        pea_first(-700+i*4,50)
    else:
        pea_second(-700+i*4,50) 
    t.tracer(True)


