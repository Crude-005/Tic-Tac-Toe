import turtle

elements = ['x', 'o']
joy = False
t = turtle.Turtle()
d_b= {'ne': '', 'nc': '', 'nw': '', 'ce': '', 'cc': '', 'cw': '', 'se': '', 'sc': '', 'se': ''}

joy2 = False


class drawings():
    def tictac_screen(fr):
        fr.clear()
        fr.shape("circle")
        fr.color("black")
        fr.width(3)
        fr.pu()
        fr.goto(-180,-60)
        fr.pd()
        fr.fd(360)
        fr.up()
        fr.goto(-180,60)
        fr.pd()
        fr.fd(360)
        fr.up()
        fr.rt(90)
        fr.goto(-60,180)
        fr.pd()
        fr.fd(360)
        fr.up()
        fr.goto(60,180)
        fr.pd()
        fr.fd(360)
        fr.up()

    def zero(t):
        t.seth(0)
        t.width(5)
        t.color("green")
        t.up()
        t.fd(50)
        t.lt(90)
        t.pd()
        t.circle(50 , 360)
        t.pu()
        
    def cross(t):
        t.seth(0)
        t.width(5)
        t.color("red")
        t.pu()
        t.fd(50)
        t.rt(90)
        t.fd(50)
        t.rt(135)
        t.pd()
        t.fd(141.421356237)
        t.up()
        t.rt(135)
        t.fd(100)
        t.rt(135)
        t.pd()
        t.fd(141.421356237)
        t.up()

        
class positionset():
    def thebox(x,y):        #use with on screen click
        global joy2
        global t
        if x in range(-180, -60):
            if y in range(60, 180):
                t.pu()
                t.goto(-120, 120)
            elif y in range(-60, 60):
                t.pu()
                t.goto(-120, 0)        
            elif y in range(-180, -60):
                t.pu()
                t.goto(-120,-120)            
            else:
                t.goto(x,y)
        elif x in range(-60, 60):
            if y in range(60, 180):
                t.pu()
                t.goto(0, 120)            
            elif y in range(-60, 60):
                t.pu()
                t.goto(0, 0)
            elif y in range(-180, -60):
                t.pu()
                t.goto(0,-120)
            else:
                t.goto(x,y)
        elif x in range(60, 180):
            if y in range(60, 180):
                t.pu()
                t.goto(120, 120)    
            elif y in range(-60, 60):
                t.pu()
                t.goto(120, 0)
            elif y in range(-180, -60):
                t.pu()
                t.goto(120,-120)
            else:
                t.goto(x,y)
        else:
            t.goto(x,y)
            
        joy2=False
        positionset.no_name()



    def no_name():
        global t
        x,y = t.position()
        global joy
        global elements
        global dict_boxes
        match x,y:
            case 120 , 120:
                d_b['ne']=elements[0]
                joy = True
            case 120 , 0:
                d_b['nc']=elements[0]
                joy = True
            case 120 , -120:
                d_b['nw']=elements[0]
                joy = True
            case 0 , 120:
                d_b['ce']=elements[0]
                joy = True
            case 0 , 0:
                d_b['cc']=elements[0]
                joy = True
            case 0 , -120:
                d_b['cw']=elements[0]
                joy = True
            case -120 , 120:
                d_b['se']=elements[0]
                joy = True
            case -120 , 0:
                d_b['sc']=elements[0]
                joy = True
            case -120 , -120:
                d_b['sw']=elements[0]
                joy = True
            case _:
                joy = False
        if joy == True:
            if elements[0] == 'x':
                switcher.element_switch()
                drawings.cross(t)
                print ('it worked xx')
            elif elements[0] == 'o':
                switcher.element_switch()
                drawings.zero(t)
                print ('it worked oo')

class switcher():
    def element_switch(x=0, y=0):
        global elements
        elements = elements[1:]+elements[:1]
    
    
def main(t):
    drawings.tictac_screen(t)
    global joy2
    turtle.onscreenclick(positionset.thebox)
    return "PLS WORK"

if __name__ == "__main__":
    msg = main(t)
    print(msg)






