import random
bord = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  
# this for display    
def disp(bord):
    print('---------')
    print('|',bord[0][2],bord[1][2],bord[2][2],'|')
    print('|',bord[0][1],bord[1][1],bord[2][1],'|')
    print('|',bord[0][0],bord[1][0],bord[2][0],'|')
    print('---------')
    
def evaluate(bord):
    for row in range(0,3):
        if (bord[0][row] == bord[1][row] == bord[2][row]):
            if bord[0][row] == 'X':
                return 10
            elif bord[0][row] == 'O':
                return  -10
    for col in range(0,3):
        if (bord[col][0] == bord[col][1] == bord[col][2]):
            if bord[col][0] == 'X':
                return 10   
            elif bord[col][0] == 'O':
                return -10
    if (bord[0][2] == bord[1][1] == bord[2][0]) or (bord[2][2] == bord[1][1] == bord[0][0]):
        if bord[1][1] == 'X':
            return 10
        else:
            return -10  
    return 0
    


def minimax(bord,dept,ismax):
    score = evaluate(bord)
    if score == 10:
        return score
    if score == -10:
        return score
    if draw(bord) == 'draw':
        return 0
    if ismax:
        best = -1000
        for i in range(0,3):
            for j in range(0,3):
                if bord[i][j] == ' ':
                    bord[i][j] = 'X'
                    beat = max(best,minimax(bord,dept+1,not ismax ))
                    bord[i][j] = ' ' 
        return best
    else:
        best = 1000
        for i in range(0,3):
            for j in range(0,3):
                if bord[i][j] == ' ':
                    bord[i][j] = 'O'
                    best = min(best, minimax(best,dept+1,not ismax))
                    bord[i][j] = ' '
        return best

def findmove(bord):
    bestval = -1000
    r = -1
    c = -1
    for i in range(0,3):
        for j in range(0,3):
            if bord[i][j] == ' ':
                bord[i][j] = 'X'
                moveval = minimax(bord, 0,False) 
                bord[i][j] = ' '
                if moveval>bestval:
                    r = i
                    c = j
                    bestval = moveval
    return [r,c]
        
# this is for check condition
def check_condition():
    while True:
        inpt = input('Enter the coordinates:')
        if all([i.isdigit() for i in inpt if i != ' ']) == False:
            print('You should enter numbers!')
            continue
        elif int(inpt[0]) > 3 or int(inpt[2]) > 3:
            print('Coordinates should be from 1 to 3!')
            continue
        if bord[int(inpt[0])-1][int(inpt[2])-1] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            return inpt
    
def draw(bord):
    if all([bord[i][j] for i in range(0,3) for j in range(0,3)]):
        return 'draw'

#this is for o computer        
def comp(bord):
    print('Making move level "easy" ')
    while True:
        n1 = random.randint(0,2)
        n2 = random.randint(0,2)
        
        if bord[n1][n2] == ' ':
            bord[n1][n2] = 'O'
            disp(bord)
            break
        else:
            print('This cell is occupied! Choose anothor one!')
            continue

def compx(bord):
    print('Making move level "easy" ')
    while True:
        n1 = random.randint(0,2)
        n2 = random.randint(0,2)
        if bord[n1][n2] == ' ':
            bord[n1][n2] = 'X'
            disp(bord)
            break
        else:
            print("This cell is occupied! Choose another one!")
            continue
        
def compmed(bord):
    dat = compxmed(bord)
    bord[int(dat[0])][int(dat[1])] = 'O'
    

   
# this is for x computer
def compxmed(bord):
    print('Making move level "medium" ')
    if ((bord[0][2] == bord[0][1] == 'O' or bord[0][2] == bord[0][1] == 'X') and bord[0][0] == ' ') or ((bord[1][0] == bord[2][0] == 'O' or bord[1][0] == bord[2][0] == 'X') and bord[0][0] == ' ') or((bord[1][1] == bord[2][2] == 'O' or bord[1][1] == bord[2][2] == 'X') and bord[0][0] == ' '):
        bord[0][0] = 'X'
        return '00'
        
    elif ((bord[0][0] == bord[0][2] == 'O' or bord[0][0] == bord[0][2] == 'X') and bord[0][1] == ' ') or ((bord[1][1] == bord[2][1] == 'O' or bord[1][1] == bord[2][1] == 'X') and bord[0][1] == ' '):
        bord[0][1] = 'X'
        return '01'
    
    elif ((bord[0][1] == bord[0][0] == 'O' or bord[0][1] == bord[0][0] == 'X') and bord[0][2] == ' ') or ((bord[1][2] == bord[2][2] == 'O' or bord[1][2] == bord[2][2] == 'X') and bord[0][2] == ' ') or ((bord[1][1] == bord[2][2] == 'O' or bord[1][1] == bord[2][2] == 'X') and bord[0][2] == ' '):   
        bord[0][2] = 'X'
        return '02'
    
    elif ((bord[0][2] == bord[2][2] == 'O' or bord[0][2] == bord[2][2] == 'O') and bord[1][2] == ' ') or ((bord[1][1] == bord[1][0] == 'O' or bord[1][1] == bord[1][0] == 'X') and bord[1][2] == ' '):
        bord[1][2] = 'X'
        return '12'
    elif ((bord[0][2] == bord[2][0] == 'O' or bord[0][2] == bord[2][0]  == 'X') and bord[1][1] == ' ') or ((bord[0][1] == bord[2][1] == 'O' or bord[0][1] == bord[2][1] == 'X') and bord[1][1] == ' ') or((bord[1][2] == bord[1][0] == 'O' or bord[1][2] == bord[1][0] == 'X') and bord[1][1] == ' ') or ((bord[2][2] == bord[0][0] == 'O' or bord[2][2] == bord[0][0] == 'X') and bord[1][1] == ' '):
        bord[1][1] = 'X'
        return '11'
    elif ((bord[1][2] == bord[1][1] == 'O' or bord[1][2] == bord[1][1] == 'X') and bord[1][0] == ' ') or ((bord[0][0] == bord[2][0] == 'O' or bord[0][0] == bord[2][0] == 'X') and bord[1][0] == ' '):
        bord[1][0] = 'X' 
        return '10'
    elif ((bord[0][2] == bord[1][2] == 'O' or bord[0][2] == bord[1][2] == 'X') and bord[2][2] == ' ') or ((bord[0][0] == bord[1][1] == 'O' or bord[0][0] == bord[1][1] == 'X') and bord[2][2] == ' ') or ((bord[2][0] == bord[2][1] == 'O' or bord[2][0] == bord[2][1] == 'X') and bord[2][2] == ' '):
        bord[2][2] = 'X'
        return '22'
    elif ((bord[0][1] == bord[1][1] == 'O' or bord[0][1] == bord[1][1] == 'X') and bord[2][1] == ' ') or ((bord[2][2] == bord[2][0] == 'O' or bord[2][2] == bord[2][0] == 'X') and bord[2][0] == ' '):
        bord[2][1] == 'X'
        return '21'
    elif ((bord[0][0] == bord[1][0] == 'O' or bord[0][0] == bord[1][0] == 'X') and bord[2][0] == ' ') or ((bord[0][2] == bord[1][1] == 'O' or bord[0][2] == bord[1][1] == 'X') and bord[2][0] == ' ') or ((bord[2][2] == bord[2][1] == 'O' or bord[2][2] == bord[2][1] == 'X') and bord[2][0] == ' '):
        bord[2][0] = 'X'
        return '20'
    else:
        while True:
            n1 = random.randint(0,2)
            n2 = random.randint(0,2)
        
            if bord[n1][n2] == ' ':
                bord[n1][n2] = 'X'
                disp(bord)
                break
            else:
                print('This cell is occupied! Choose another one!')
                continue
        return str(n1)+str(n2)


while True:  
    choose = input('Input command:')      
    if choose == 'exit':
        break
    else:
        if len(choose.split()) == 3:
            if choose.split() == ['start','easy','easy']:
                while True:
                    disp(bord)
                    compx(bord)
                    if (bord[0][2] == bord[1][1] == bord[2][0] == 'X') or (bord[2][2] == bord[1][1] == bord[0][0] == 'X') or (bord[0][2] == bord[1][2] == bord[2][2] == 'X') or (bord[0][1] == bord[1][1] == bord[2][1] == 'X') or (bord[0][0] == bord[1][0] == bord[2][0] == 'X') or (bord[0][2] == bord[0][1] == bord[0][0] == 'X') or (bord[1][2] == bord[1][1] == bord[1][0] == 'X') or (bord[2][2] == bord[1][2] == bord[0][2] == 'X'):
                        print('X wins')
                        break
                    d = draw(bord) 
                    if d == 'draw':
                        print("Draw")
                        break
                    comp(bord)
                    if (bord[0][2] == bord[1][1] == bord[2][0] == 'O') or (bord[2][2] == bord[1][1] == bord[0][0] == 'O') or (bord[0][2] == bord[1][2] == bord[2][2] == 'O') or (bord[0][1] == bord[1][1] == bord[2][1] == 'O') or (bord[0][0] == bord[1][0] == bord[2][0] == 'O') or (bord[0][2] == bord[0][1] == bord[0][0] == 'O') or (bord[1][2] == bord[1][1] == bord[1][0] == 'O') or (bord[2][2] == bord[1][2] == bord[0][2] == 'O'):
                        print('O wins')
                        break
                    d = draw(bord) 
                    if d == "draw":
                        print("Draw")
                        break
            elif choose.split() == ['start','medium','medium']:
                while True:
                    disp(bord)
                    compxmed(bord)
                    ans = evaluate(bord)  
                    if ans == 10:
                        print("X wins")
                        break
                    d = draw(bord) 
                    if d == 'draw':
                        print("Draw")
                        break 
                    compmed(bord)
                    ass = evaluate(bord) 
                    if ass == -10:
                        print("O wins")
                        break 
                        
                    d = draw(bord) 
                    if d == "draw":
                        print("Draw")
                        break
                        
            
            elif choose.split() == ['start','easy','user']:
                while True:
                    disp(bord)
                    compx(bord) 
                    ans = evaluate(bord)
                    if ans == 10:
                        print("X wins")
                        break
                    d = draw(bord) 
                    if d == "draw":
                        print("Draw")
                        break
                    
                    inpt = check_condition()
                
                    bord[int(inpt[0])-1][int(inpt[2])-1] = 'O'
                    ass = evaluate(bord)
                    if ass == -10:
                        print("O wins")
                        break
                        
                
                    if all([bord[i][j] != ' ' for i in range(0,3) for j in range(0,3)]):
                        print("Draw")
                        break
            elif choose.split() == ['start','medium','user']:
                while True:
                    disp(bord)
                    compxmed(bord) 
                    ans = evaluate(bord) 
                    if ans == 10:
                        print("X wins")
                        break
                    d = draw(bord)
                    if d == "draw":
                        print("Draw")
                        break
                    inpt = check_condition()
                    bord[int(inpt[0])-1][int(inpt[2])-1] = 'O'
                    ass = evaluate(bord)
                    if ass == -10:
                        print("O wins")
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
                    
            
            elif choose.split() == ['start','user','easy']:
                disp(bord)
                while True:
                
        
                    inpt = check_condition()
    
                    bord[int(inpt[0])-1][int(inpt[2])-1] = 'X'
                    disp(bord)
                    ans = evaluate(bord)
                    if ans == 10:
                        print('X wins')
                        break
                    d = draw(bord)
                    if d == "draw":
                        print("Draw")
                        break
                    comp(bord)
                    #disp(bord)
                    ass = evaluate(bord)
                    if ass == -10:
                        print('O wins')
                        break
                    elif all([bord[i][j] != ' ' for i in range(0,3) for j in range(0,3)]):
                        print('Draw') 
                        break
            elif choose.split() == ["start","user","medium"]:
                disp(bord)
                while True:
                    inpt = check_condition()
                    bord[int(inpt[0])-1][int(inpt[2])-1] = 'X'
                    disp(bord)
                    ans = evaluate(bord)
                    if ans == 10:
                        print("X wins")
                        break
                    d = draw(bord)
                    if d == "draw":
                        print("Draw")
                        break
                    compmed(bord)
                    ass = evaluate(bord)
                    if ass == -10:
                        print("O wins")
                        break
                    d = draw(bord)
                    if d == "draw":
                        print("Draw")
                        break
            elif choose.split() == ["start","medium","easy"]:
                while True:
                    disp(bord) 
                    compxmed(bord) 
                    disp(bord) 
                    ans = evaluate(bord) 
                    if ans == 10:
                        print("X wins")
                        break
                    d = draw(bord)
                    if d == "draw":
                        print("Draw")
                        break 
                    comp(bord) 
                    ass = evaluate(bord)

                    if ass == -10:
                        print("O wins")
                        break
                    d = draw(bord) 
                    if d == 'draw':
                        print('Draw') 
                        break 
            elif choose.split() == ["start","easy","medium"]:
                while True:
                    disp(bord)
                    compx(bord)
                    ans = evaluate(bord) 
                    if ans == 10:
                        print("X wins")
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print("Draw")
                        break
                    compmed(bord)
                    disp(bord)
                    ass = evaluate(bord) 
                    if ass == -10:
                        print('O wins')
                        break
                    d = draw(bord) 
                    if d == 'draw':
                        print('Draw') 
                        break 
                    
            elif choose.split() == ["start","user","user"]:
                disp(bord)
                while True:
                    
                    inpt = check_condition()
                    rnd = 1
                    
                    if rnd % 2 != 0:
                        bord[int(inpt[0])-1][int(inpt[2])-1] = 'X'
                        rnd += 1
                        ans = evaluate(bord)
                        if ans == 10:
                            print('X wins')
                            break
                        d = draw(bord)
                        if d == "draw":
                            print("Draw")
                            break
                    else:
                        bord[int(inpt[0])-1][int(inpt[2])-1] = 'O'
                        rnd += 1
                        ass = evaluate(bord) 
                        
                        if ass == -10:
                            print('O wins')
                            break
                        if all([bord[i][j] != ' ' for i in range(0,3) for j in range(0,3)]):
                            print('Draw')
                            break
            elif choose.split() == ['start','hard','user']:
                while True:
                    print('Making move level "hard" ')
                    r,c = findmove(bord)
                    bord[c][r] = 'X'
                    disp(bord) 
                    ans = evaluate(bord)
                    if ans == 10:
                        print('X wins')
                        break 
                    d = draw(bord) 
                    if d == 'draw':
                        print('Draw')
                        break 
                    inpt = check_condition() 
                    bord[int(inpt[0])-1][int(inpt[2]) -1] = 'O'
                    ass = evaluate(bord) 
                    if ass == -10:
                        print('O wins')
                        break 
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw') 
                        break
            elif choose.split() == ['start', 'user', 'hard']:
                while True:
                    inpt = check_condition()
                    bord[int(inpt[0])-1][int(inpt[2])-1] = 'X'
                    disp(bord)
                    ans = evaluate(bord) 
                    if ans == 10:
                        print('X wins')
                        break 
                    d = draw(bord)
                    if d == 'draw':
                        print('draw') 
                        break
                    r,c = findmove(bord) 
                    bord[c][r] = 'O'
                    disp(bord) 
                    ass = evaluate(bord) 
                    if ass == -10:
                        print("O wins")
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break 
            elif choose.split() == ['start','hard','hard']:
                while True:
                    print('Making move level "hard" ')
                    r,c = findmove(bord)
                    bord[c][r] = 'X'
                    disp(bord)
                    ans = evaluate(bord)
                    if ans == 10:
                       print('X wins')
                       break
                    d =  draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
                    print('Making move level  "hard" ')
                    r,c = findmove(bord)
                    bord[c][r] = 'O'
                    disp(bord)
                    ass = evaluate(bord)
                    if ass == -10:
                        print('O wins')
                        break 
                    d = draw(bord) 
                    if d == 'draw':
                        print('Draw')
                        break 
            elif choose.split() == ['start','medium','hard']:
                while True:
                    compxmed(bord)
                    ans = evaluate(bord)
                    if ans == 10:
                        print('X wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw') 
                        break
                        
                    r,c = findmove(bord)
                    bord[c][r] = 'O'
                    disp(bord) 
                    ass  = evaluate(bord) 
                    if ass == -10:
                        print('O wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break 
                        
            elif choose.split() == ['start','hard','medium']:
                while True:
                    r,c = findmove(bord)
                    bord[c][r] = 'X'
                    disp(bord)
                    ans = evaluate(bord)  
                    if ans == 10:
                        print('X wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
                    compmed(bord)
                    ass = evaluate(bord) 
                    if ass == -10:
                        print('O wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw') 
                        break 
            elif choose.split() == ['start','easy','hard']:
                while True:
                    compx(bord)
                    ans = evaluate(bord)
                    if ans == 10:
                        print('X wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
                    r,c = findmove(bord)
                    bord[c][r] = 'O'
                    disp(bord)
                    ass = evaluate(bord)
                    if ass == -10:
                        print('O wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
            elif choose.split() == ['start','hard','easy']:
                while True:
                    r,c = findmove(bord)
                    bord[c][r] = 'X'
                    disp(bord)
                    ans = evaluate(bord)
                    if ans == 10:
                        print('X wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
                    comp(bord)
                    ass = evaluate(bord)
                    if ass == -10:
                        print('O wins')
                        break
                    d = draw(bord)
                    if d == 'draw':
                        print('Draw')
                        break
                        
                    
                       
                    
                    
        else:
            print("Bad parameters") 
            continue   
                
             
            
            
            
    
    
