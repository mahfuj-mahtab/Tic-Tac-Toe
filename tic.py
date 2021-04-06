TheBoard={'1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' '}

Board_key=[]
for key in TheBoard:
    Board_key.append(key)
    #print(key)

def boardprint(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        boardprint(TheBoard)
        print('Its Your Turn ' + turn + '.Tell which position\n')
        move = input()
        if(TheBoard[move] == ' '):
            TheBoard[move] = turn
            count+=1
        else:
            print('Sorry This is already filled.Try another position\n')
            continue
        if(count>=5):
            if TheBoard['1'] == TheBoard['2'] == TheBoard['3'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['4'] == TheBoard['5'] == TheBoard['6'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['7'] == TheBoard['8'] == TheBoard['9'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['1'] == TheBoard['4'] == TheBoard['7'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['2'] == TheBoard['5'] == TheBoard['8'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['3'] == TheBoard['6'] == TheBoard['9'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard['9'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
            elif TheBoard['3'] == TheBoard['5'] == TheBoard['7'] != ' ':
                boardprint(TheBoard)
                print("Yeah "+ turn + " Won")
                break
        if(turn == 'x'):
            turn = 'o'
        else:
            turn ='x'
    
    if(count == 9):
        print('Tie. Game Over')
    restart = input('Do You Want To Play?(Y/N)')
    if restart == 'y' or restart == 'Y':
        for key in Board_key:
            TheBoard[key] = " "

        game()

game()