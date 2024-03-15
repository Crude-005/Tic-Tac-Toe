import random

def dupli_remover(list):
    l1 = []
    for i in list:
        if i not in l1:
            l1.append(i)
    return l1
def obj_inverter(obj):
    if obj == 'o':
        obje = 'x'
    elif obj == 'x':
        obje = 'o'
    return obje

def move_maker(matrix , posi, obj):
    temprory_matrix = []
    for i in range(len(matrix)):
        new = ''
        for j in matrix[i]:
            if j == str(posi):
                new += obj
            else:
                new+=j
        temprory_matrix.append(new)
    return temprory_matrix

def unoccupied(matrix):
    available_places = []
    for i in range(3):
        for j in matrix[i]:
            if j == 'o' or j == 'x':
                continue
            else:
                available_places.append(int(j))
    return available_places

def test1(matrix,obj):
    s1 = [False,]
    for i in matrix:
        if i.count(obj) == 2 and i.count(obj_inverter(obj)) == 0:
            s1[0] = True
            for j in i:
                if j in '123456789':
                    s1.append(j)
    s1= list(dict.fromkeys(s1))
    return s1

def test2(matrix,obj):
    bi_obj = obj_inverter(obj)
    s2 = [False,]
    for i in matrix:
        if i.count(bi_obj) == 2 and i.count(obj) == 0:
            s2[0] = True
            for j in i:
                if j in '123456789':
                    s2.append(j)
    s2= list(dict.fromkeys(s2))
    return s2

    
def test3(matrix,obj):
    s3 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temprory_matrix = move_maker(matrix,i,obj)
        s1 = test1(temprory_matrix , obj)
        if s1[0] == True and len(s1) >= 3:
            s3[0] = True
            s3.append(str(i))
    s3= list(dict.fromkeys(s3))
    return s3

def test4(matrix,obj):
    bi_obj = obj_inverter(obj)
    s4 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temp_matrix = move_maker(matrix,i,obj)
        s2 = test2(temp_matrix,bi_obj)
        if s2[0] == True:
            temp_matrix_2 = move_maker(temp_matrix,int(s2[1]),bi_obj)
            s2 = test2(temp_matrix_2,obj)
            s3 = test3(temp_matrix_2,obj)
            if s3[0] == True and s2[0]== False:
                s4[0] = True
                s4.append(str(i))
            elif s3[0]== True and s2[0] == True :
                if s2[1] in s3:
                    s4[0] = True
                    s4.append(str(i))
    s4= list(dict.fromkeys(s4))
    return s4


def test5(matrix,obj):
    bi_obj = obj_inverter(obj)
    s5 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temp_matrix = move_maker(matrix,i,obj)
        s1 = test1(temp_matrix,bi_obj)
        s2 = test2(temp_matrix,bi_obj)
        s3 = test3(temp_matrix,bi_obj)
        s4 = test4(temp_matrix,bi_obj)
        if s4[0] == False  and s3[0] == False and  s1[0] == False:
            s5[0] = True
            s5.append(str(i))
        
    s5= list(dict.fromkeys(s5))
    return s5

def test6(matrix,obj):
    bi_obj = obj_inverter(obj)
    s6 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temp_matrix = move_maker(matrix,i,obj)
        s2 = test2(temp_matrix,bi_obj)
        s3 = test3(temp_matrix,bi_obj)
        if s3[0] == False or (s3[0] == True and s2[0] == True and s2[1] != s3[1]):
            s6[0] = True
            s6.append(str(i))
            
    s6= list(dict.fromkeys(s6))
    return s6

#------------------------------------------------------------------------------------------------------------
def game_reader(v_n):
    the_matrix = ['123','456','789','147','258','369','159','357']
    for i in v_n:
        val = v_n[i]
        if val != ' ' and val!= '':
            the_matrix = move_maker(the_matrix,i,val)
    return the_matrix

def move_maker_2(v_n,values):
    matrix = game_reader(v_n)
    s1 = test1(matrix,values[0])
    s2 = test2(matrix,values[0])
    s3 = test3(matrix,values[0])
    s4 = test4(matrix,values[0])
    s5 = test5(matrix,values[0])
    s6 = test6(matrix,values[0])
    if s1[0] == True:
        print ('s2',s1)
        move = random.choice(s1[1::])
    elif s2[0] == True:
        print('s2',s2)
        move = random.choice(s2[1::])    
    elif s3[0] == True:
        print('s3',s3)
        move = random.choice(s3[1::])    
    elif s4[0] == True:
        print('s4',s4)
        move = random.choice(s4[1::])
    elif s5[0] == True:
        print('s5',s5)
        move = random.choice(s5[1::])
    elif s6[0] == True:
        print ('s6',s6)
        move = random.choice(s6[1::])
    else:
        print('s7',matrix)
        move = random.choice(unoccupied(matrix))
       
    return int(move)

v_n = {1: '', 2: 'o', 3: 'x', 4: '', 5: 'x', 6: '', 7: '', 8: '', 9: ''}
matrix = game_reader(v_n)
print(matrix)
move = move_maker_2(v_n,['x','o'])
print ('move:', move )
