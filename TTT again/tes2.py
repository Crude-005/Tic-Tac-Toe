from ttt_lib import *
from turtle import *
from time import sleep
Screen()


def main():
    set_up = setup_board.tictac_screen(cursor)
    x,y = position()
    position_set = game.thebox(int(x),int(y))

    
    sleep(2)
    return "tt"
def game_play():
    x,y = position(cursor)
    print (x,y)


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()


moves_record = {"tl":0,"tm":0,"tr":0,"cl":0,"cm":0,"cr":0,"bl":0,"bm":0,"br":0}