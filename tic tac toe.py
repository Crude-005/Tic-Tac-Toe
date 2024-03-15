from turtle import *

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()

        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

def tictac_screen():
    clear()
    resetscreen()
    speed(10)
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
    
def main():
    global colors
    shape("circle")
    resizemode("user")
    shapesize(.5)
    width(3)
    colors=["red", "green", "blue", "yellow"]
    color(colors[0])
    switchupdown()
    onkeypress(tictac_screen(),"n")
    onscreenclick(goto,1)
    onscreenclick(changecolor,2)
    onscreenclick(switchupdown,3)
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
