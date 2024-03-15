def criss_cross(dict1):
    for i in dict1:
        val = dict1[i]
        if val  == 'o' or val  == 'x':
            continue
        else:
            dict1[i]  = ' '
    print ("         |         |         ")
    print (f"   {dict1[1]}     |    {dict1[2]}    |    {dict1[3]}    ")
    print ("         |         |         ")
    print ("_ _ _ _ _|_ _ _ _ _|_ _ _ _")
    print ("         |         |         ")
    print (f"   {dict1[4]}     |    {dict1[5]}    |    {dict1[6]}    ")
    print ("         |         |         ")
    print ("_ _ _ _ _|_ _ _ _ _|_ _ _ _")
    print ("         |         |         ")
    print (f"   {dict1[7]}     |    {dict1[8]}    |    {dict1[9]}    ")
    print ("         |         |         ")

def game():
    v_n = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '} #value noter
    global values
    in_process = True
    while in_process:
        if v_n[1] == v_n[2] == v_n[3] != ' ' or v_n[4] == v_n[5]== v_n[6] != ' ' or v_n[7] == v_n[8] == v_n[9] != ' ':
            score_updater(values[1])
            print (f"{values[1]} wins")
            in_process = False
        elif v_n[1] == v_n[4] == v_n[7] != ' ' or v_n[2] == v_n[5]== v_n[8] != ' ' or v_n[3] == v_n[6] == v_n[9] != ' ':
            print (f"{values[1]} wins")
            score_updater(values[1])
            in_process = False
        elif v_n[1] == v_n[5] == v_n[9] != ' ' or v_n[3] == v_n[5]== v_n[7] != ' ':
            print (f"{values[1]} wins")
            score_updater(values[1])
            in_process = False
        elif ' ' not in  list(v_n.values()):
            print ("Draw")
            in_process = False
        else:
            print ((f"{namefier(values[0])} turn"))
            wrong_input = False
            place = input("Enter the position: ")            
            try:
                int(place)
            except:
                wrong_input = True
            if wrong_input == False and int(place) in range(0,10):
                place = int(place)
                if v_n[place] != ' ':
                    print ("Wrong input.Place already occupied.")
                elif values[0] == 'o':
                    v_n[place]= 'o'
                    values = values[::-1]
                elif values[0] == 'x':
                    v_n[place]= 'x'
                    values = values[::-1]
                else:
                    print ("some error has occured")
            else:
                print ("wrong input")
        
            criss_cross(v_n)
    score_board(0)
    return True

def score_board(fn = 0):
    global info_chart
    global values
    if fn == 0:
        print(info_chart[0],"[o]: ", info_chart[2])
        print(info_chart[1],"[x]: ", info_chart[3])
    elif fn == 1:
        player1 = input("Enter player 1 name: ")
        info_chart[0] = player1
    elif fn == 2:
        player2 = input("Enter player 2 name: ")
        info_chart[1] = player2
    elif fn == 3 :
        info_chart[2]+=1
    elif fn == 4 :
        info_chart[3]+=1
    elif fn == 5:
        info_chart = ["Player1",'Player2',0,0]
        values = ['o','x']


def state(st=0):
    global _state
    if st == 0:
        _state = 0 #New game (just strted)
    elif st == 1:
        _state = 1 #continue game
    else:
        _state = 4 #End

def score_updater(wi):
    if wi == 'o':
        score_board(3)
    elif wi == 'x':
        score_board(4)
    else:
        return
def namefier(wi):
    if wi == 'o':
        return info_chart[0]
    elif wi == 'x':
        return info_chart[1]
    else:
        return

values = ['o','x']
info_chart = ["Player1",'Player2',0,0]  #player1_name , player_2 name , player1 score , player 2 score


#-----------------------------------------------------------------------------------------------------------------#

_state = 0 
print ("----WELCOME TO TIC TAC TOE GAME----")
print ("Credits - Chirag Sugla")
mod = True
while mod:
    print ("Enter \n [0] to exit \n [1] to start for 2 players \n [2] to atart player vs bot")
    _start = input(": ")
    if _start == '0':
        mod = False
        score_board(0)
        state(4)
    elif _start == '2':
        print ("Coming soon")
    elif _start == '1':
        mod2 = True
        while mod2:
            if _state == 0:
                print ("Enter \n [0] to exit \n [1] to start new game ")
                _play = input(": ")
                if _play == '0':
                    mod2 = False
                elif _play == '1':
                    score_board(1)
                    score_board(2)
                    game()
                    state(1)
            elif _state == 1:
                print ("Enter \n [0] to exit \n [1] to continue \n [2] to start new game \n [3] to change player name")
                _play = input(": ")
                if _play == '0':
                    mod2 = False
                elif _play == '1':
                    game()
                    state(1)
                elif _play == '2':
                    score_board(5)
                    score_board(1)
                    score_board(2)
                    game()
                elif _play == '3':
                    score_board(1)
                    score_board(2)
                    print ("Score Board updated successfully :)")
                else:
                    print("Wrong input")
            else:
                continue
else:
    print ("Thanks for playing.")
            
