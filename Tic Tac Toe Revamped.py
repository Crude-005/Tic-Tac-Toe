from turtle import *
from time import sleep

def tictac_screen():
    shape("circle")
    hideturtle()
    resetscreen()
    color("black")
    width(3)
    pu()
    goto(-180,-60)
    pd()
    fd(360)
    up()
    goto(-180,60)
    pd()
    fd(360)
    up()
    rt(90)
    goto(-60,180)
    pd()
    fd(360)
    up()
    goto(60,180)
    pd()
    fd(360)
    up()

def cross():
    width(5)
    color("red")
    pu()
    fd(50)
    rt(90)
    fd(50)
    rt(135)
    pd()
    fd(141.421356237)
    up()
    rt(135)
    fd(100)
    rt(135)
    pd()
    fd(141.421356237)
    up()
    seth(0)

def zero():
    width(5)
    color("green")
    up()
    fd(50)
    lt(90)
    pd()
    circle(50 , 360)
    pu()
    seth(0)

def alt(num):
    if num == 'x':
        num = 'o'
    elif num == 'o':
        num = 'x'
    else:
        num = 'x'
    return num
        

def thebox(x,y):
    num = 0
    if x in range(-180, -60):
        if y in range(60, 180):
            pu()
            goto(-120, 120)
        elif y in range(-60, 60):
            pu()
            goto(-120, 0)        
        elif y in range(-180, -60):
            pu()
            goto(-120,-120)            
        else:
            goto(x,y)
    elif x in range(-60, 60):
        if y in range(60, 180):
            pu()
            goto(0, 120)            
        elif y in range(-60, 60):
            pu()
            goto(0, 0)
        elif y in range(-180, -60):
            pu()
            goto(0,-120)
        else:
            goto(x,y)
    elif x in range(60, 180):
        if y in range(60, 180):
            pu()
            goto(120, 120)    
        elif y in range(-60, 60):
            pu()
            goto(120, 0)
        elif y in range(-180, -60):
            pu()
            goto(120,-120)
        else:
            goto(x,y)
    else:
        goto(x,y)

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

def no_name():
    x,y = position()
    match x,y:
        case 120 , 120:
            joy = True
        case 120 , 0:
           joy = True
        case 120 , -120:
            joy = True
        case 0 , 120:
            joy = True
        case 0 , 0:
            joy = True
        case 0 , -120:
            joy = True
        case -120 , 120:
            joy = True
        case -120 , 0:
            joy = True
        case -120 , -120:
            joy = True
        case _:
            joy = False
    return joy
    
    
def play(roo,num):
    onscreenclick(thebox)
    joy = no_name()
    
    
    if joy == True:
        if num == 'x':
            cross()
        elif num == 'o':
            zero()
        elif num == '1':
            num = 'x'
    num = alt(num)
    roo += 1
    return roo , num

def main():
    tictac_screen()
    roo = 0
    tr = 0
    num = 'x'
    while roo == tr :
        roo, num = play(roo,num)
        tr +=1
    return "PLS WORK"

if __name__ == "__main__":
    msg = main()
    print(msg)

    
    
    

    
