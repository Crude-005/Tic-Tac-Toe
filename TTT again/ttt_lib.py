from turtle import *
import turtle



cursor = Turtle()
cursor.shape("circle")    
cursor.width(3)
cursor.speed(10)
st = 2 #(0 --> ON click work , 1 --> on click dont work, 2 --> ended )

values = ['x','o']

v_n = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '} #value noter


def state(d=3):
    global st
    if d == 0 or d == 1 or d == 2:
        st = d
    
    return st

def game_2(x,y):
    global values
    if state() == 0:
        return
    cursor.goto(x,y)
    if state() == 2:
        return 
    elif state() == 1:
        if v_n[1] == v_n[2] == v_n[3] != ' ' :
            start = (-170,120)
            end = (170,120)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif v_n[4] == v_n[5]== v_n[6] != ' ' :
            start = (-170,0)
            end = (170,0)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif v_n[7] == v_n[8] == v_n[9] != ' ':
            start = (-170,-120)
            end = (170,-120)
            print (f"{values[1]} wins")
            st = state(2)          
            elements.victor_line(start,end)  
        elif v_n[1] == v_n[4] == v_n[7] != ' ' :
            start = (-120,170)
            end = (-120,-170)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif v_n[2] == v_n[5]== v_n[8] != ' ' :
            start = (0,170)
            end = (0,-170)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif v_n[3] == v_n[6] == v_n[9] != ' ':
            start = (120,170)
            end = (120,-170)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif v_n[1] == v_n[5] == v_n[9] != ' ' :
            start = (-170,170)
            end = (170,-170)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif v_n[3] == v_n[5]== v_n[7] != ' ':
            start = (-170,-170)
            end = (170,170)
            print (f"{values[1]} wins")
            st = state(2)
            elements.victor_line(start,end)
        elif ' ' not in  list(v_n.values()):
            print ("Draw")
            st = state(2)
        else:
            print ((f"{values[0]} turn"))
            place = (game.thebox(x,y))
            if place not in range(1,10):
                return
            if v_n[place] != ' ':
                return
            elif values[0] == 'o':
                v_n[place]= 'o'
                values = values[::-1]
                elements.zero()
            elif values[0] == 'x':
                v_n[place]= 'x'
                values = values[::-1]
                elements.cross()
            else:
                print ("some error has occured")
        return
    else:
        print ("NO ONE WILL EVER READ THIS.")
        return
            

class setup_board():
    def tictac_screen():
        state(0)
        cursor.color("brown")
        cursor.clear()
        cursor.pu() 
        cursor.home()
        cursor.goto(-180,-60)   
        cursor.pd() 
        cursor.fd(360)  
        cursor.up() 
        cursor.goto(-180,60)    
        cursor.pd() 
        cursor.fd(360)  
        cursor.up() 
        cursor.rt(90)   
        cursor.goto(-60,180)    
        cursor.pd() 
        cursor.fd(360)  
        cursor.up() 
        cursor.goto(60,180) 
        cursor.pd() 
        cursor.fd(360)  
        cursor.up()
        cursor.home()
        st = state(1)
        return True  

class elements():
    def zero():
        st = state(0)
        cursor.seth(0)
        cursor.width(5)  
        cursor.color("green")    
        cursor.up()  
        cursor.fd(50)    
        cursor.lt(90)    
        cursor.pd()  
        cursor.circle(50 , 360)  
        cursor.pu()  
        st = state(1)
        return 1
            
    def cross():
        st = state(0)
        cursor.seth(0)   
        cursor.width(5)
        cursor.color("red")
        cursor.pu()
        cursor.fd(50)
        cursor.rt(90)
        cursor.fd(50)
        cursor.rt(135)
        cursor.pd()
        cursor.fd(141.421356237)
        cursor.up()
        cursor.rt(135)
        cursor.fd(100)
        cursor.rt(135)
        cursor.pd()
        cursor.fd(141.421356237)
        cursor.up()
        st = state(1)
        return 2
    def victor_line(start , end):
        x =start[0]
        y = start[1]
        x_ = end[0]
        y_ = end[1]
        st = state(0)
        cursor.pu()
        cursor.goto(x,y)
        cursor.pd()
        cursor.goto(x_,y_)
        cursor.pu()
        st = state(2)

class game():
    """def ok(x,y):
        game_2()"""


    def thebox(x,y):        #use with on screen click)
        if x in range(-180, -60):
            if y in range(60, 180):
                cursor.pu()
                cursor.goto(-120, 120)
                place = 1
            elif y in range(-60, 60):
                cursor.pu()
                cursor.goto(-120, 0) 
                place = 4      
            elif y in range(-180, -60):
                cursor.pu()
                cursor.goto(-120,-120) 
                place = 7          
            else:
                cursor.goto(x,y)
                place = 0
        elif x in range(-60, 60):
            if y in range(60, 180):
                cursor.pu()
                cursor.goto(0, 120) 
                place = 2           
            elif y in range(-60, 60):
                cursor.pu()
                cursor.goto(0, 0)
                place = 5
            elif y in range(-180, -60):
                cursor.pu()
                cursor.goto(0,-120)
                place = 8
            else:
                cursor.goto(x,y)
                place = 0
        elif x in range(60, 180):
            if y in range(60, 180):
                cursor.pu()
                cursor.goto(120, 120)   
                place = 3 
            elif y in range(-60, 60):
                cursor.pu()
                cursor.goto(120, 0)
                place = 6
            elif y in range(-180, -60):
                cursor.pu()
                cursor.goto(120,-120)
                place = 9
            else:
                cursor.goto(x,y)
                place = 0
        else:
            cursor.goto(x,y)
            place = 0
        return place                                
    def movement():
        listen()
        onscreenclick(game_2)
        onkey(main,'space')


def main():
    if state() == 0 :
        return
    global v_n
    set_up = setup_board.tictac_screen()
    v_n = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    game.movement()
    
    return True


    





"""?????????????????????????????????????????????????????????"""
