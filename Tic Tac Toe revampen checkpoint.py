from turtle import *

t = Turtle() 
def tictac_screen(fr):
    fr.clear()
    fr.shape("circle")
    fr.hideturtle()
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


def cross(t):
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
    t.seth(0)

def zero(t):
    t.width(5)
    t.color("green")
    t.up()
    t.fd(50)
    t.lt(90)
    t.pd()
    t.circle(50 , 360)
    t.pu()
    t.seth(0)

def alt(num):
    if num == 'x':
        num = 'o'
    elif num == 'o':
        num = 'x'
    else:
        num = 'o'
    return num
        

def thebox(x,y,num):
    if x in range(-180, -60):
        if y in range(60, 180):
            pu()
            goto(-120, 120)
            nw = num
            num = alt(num)
            return num , True
        elif y in range(-60, 60):
            pu()
            goto(-120, 0)
            cw = num
            num = alt(num)
            return num , True
        elif y in range(-180, -60):
            pu()
            goto(-120,-120)
            sw = num
            num = alt(num)
            return num , True
        else:
            goto(x,y)
            return num , False
    elif x in range(-60, 60):
        if y in range(60, 180):
            pu()
            goto(0, 120)
            nc = num
            num = alt(num)
            return num , True
        elif y in range(-60, 60):
            pu()
            goto(0, 0)
            cc = num
            num = alt(num)
            return num , True
        elif y in range(-180, -60):
            pu()
            goto(0,-120)
            sc = num
            num = alt(num)
            return num , True
        else:
            goto(x,y)
            return num , False
    elif x in range(60, 180):
        if y in range(60, 180):
            pu()
            goto(120, 120)
            ne = num
            num = alt(num)
            return num , True
        elif y in range(-60, 60):
            pu()
            goto(120, 0)
            ce = num
            num = alt(num)
            return num , True
        elif y in range(-180, -60):
            pu()
            goto(120,-120)
            se = num
            num = alt(num)
            return num , True
        else:
            goto(x,y)
            return num , False
    else:
        goto(x,y)
        return num , False

def win_check(nw,nc,ne,cw,cc,ce,sw,sc,se,mod2):
    if nw == nc == ne:
        goto(-170,120)
        pd()
        goto(170,120)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif cw == cc == ce:
        goto(-170,0)
        pd()
        goto(170,0)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif sw == sc == se:
        goto(-170,-120)
        pd()
        goto(170,-120)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif nw == cw == sw:
        goto(-120,170)
        pd()
        goto(-120,-170)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif nc == cc == sc:
        goto(0,170)
        pd()
        goto(0,-170)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif ne == ce == se:
        goto(120,170)
        pd()
        goto(120,-170)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif nw == cc == se:
        goto(-170,170)
        pd()
        goto(170,-170)
        up()
        print (f"{nw} Wins")
        mod2 = False
    elif ne == cc == sw:
        goto(170,170)
        pd()
        goto(-170,-170)
        up()
        print (f"{nw} Wins")
        mod2 = False
    else:
        print ("rrr")
    return nw,nc,ne,cw,cc,ce,sw,sc,se,mod2

def cord(x,y):
    return x , y
    
def play(t,roo, num):
    onscreenclick(goto)
    x,y = position()
    num , joy = thebox(x,y,num)
    if joy == True:
        if num == 'x':
            cross(t)
        elif num == 'o':
            zero(t)
    roo += 1
    return roo , num
    
def main():
    tictac_screen(t)
    roo = 0
    tr = 0
    num = '1'
    while tr == roo:
        tr , num  = play(t ,tr, num)
        roo = tr
    
    return "PLS WORK"

if __name__ == "__main__":
    msg = main()
    print(msg)

    
    
    

    
