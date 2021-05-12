
board = {'7':' ','8':' ','9':' ',
         '4':' ','5':' ','6':' ',
         '3':' ','2':' ','1':' '}

boardStart = {'7':'7','8':'8','9':'9',
            '4':'4','5':'5','6':'6',
            '3':'3','2':'2','1':'1'}
def displayBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def choosePlayer():

    print("Choose your opponent")
    print("Input 1 : You will play with a player")
    print("Input 2 : You will play with a computer")
    player = input()

    if player == '1':
        print("You play with player")
        play()
    elif player == '2':
        print("You play with computer")
        playWithComp()

def winPattern(board, turn,win):
    win = False
    
    if board['1'] == board['2'] == board['3'] == turn:
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['1'] == board['5'] == board['9'] == turn:
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['1'] == board['4'] == board['7'] == turn:
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['4'] == board['5'] == board['6'] == turn:
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['7'] == board['8'] == board['9'] == turn:
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['8'] == board['5'] == board['2']== turn :
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['9'] == board['6'] == board['3']== turn:
            win = True
            print("congrats \"" + turn +"\" won")
    elif board['7'] == board['5'] == board['3']== turn:
            win = True
            print("congrats \"" + turn +"\" won")
    return win

def playWithComp():
    
    win = False

    print("Your turn : X and Computer turn : O")    
    while win == False:    
        
        turn = 'X'
        print("Turn :" + turn )
        print("Using your keypad on the keyboard to choose the block")

        place = False
        while place == False :
            move = input()
            if board[move] == ' ' :
                board[move] = turn
                place = True
                
            else:
                print("That place is already filled. Choose other one")
        
        win = winPattern(board, turn,win)
        displayBoard(board)
        if win == True :
            break
        

        
        turn = 'O'
        import random
        comp = str(random.randint(1,9))
        if board[comp] == 'O' or board[comp]== 'X':
            while comp == turn or board[comp] == 'O' or board[comp] == 'X' or board[comp] != ' ':
                comp = str(random.randint(1,9))
            board[comp] = 'O'
            print("Computer turn")
            displayBoard(board)
            print("Computer made a move to : " + comp)
        else:
            print("Computer turn")
            board[comp] = 'O'
            displayBoard(board)
            print("Computer made a move to : " + comp)    
        win = winPattern(board, turn,win)


        

def play():

    turn = ''
    win = False

    print("First turn : X and second turn : O")    
    while win == False:    

        if turn == 'X' :
            turn = 'O'
        else :
            turn = 'X'

        print("Your turn :" + turn )
        print("Using your keypad on the keyboard to choose the block")

        place = False
        while place == False :
            move = input()
            try :
                if move == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
                    if board[move] == ' ' :
                        board[move] = turn
                        place = True
                else:
                    print("That place is already filled. Choose other one")
            except:
                print("problem with input!")
            
        win = winPattern(board, turn, win)

        displayBoard(board)

def gameManagement():
    game = False
    while game == False:
        print("Wellcome to TicTacToe")
        print("1: Start")
        print("2: Exit")
        inputGame = input()
        if inputGame == '1':
            print("Game is starting")
            print("Play with your keypad")
            displayBoard(boardStart)
            choosePlayer()
            print("game finish")
            continue
        elif inputGame == '2':
            import sys
            sys.exit()
        else:
            print("You have put wrong input!")
        
    

if __name__ == '__main__':
    gameManagement()


    