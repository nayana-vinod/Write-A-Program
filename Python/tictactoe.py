print("\n ***Note the number on the board goes in the order 1-9 from bottom left. So, choose your move accordingly.*** \n")
GameBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

gameboard_keys = []

for key in GameBoard:
    gameboard_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(GameBoard)
        print("Your turn," + turn + ". What is your move?\n")

        move = input()        

        if GameBoard[move] == ' ':
            GameBoard[move] = turn
            count += 1
        else:
            print("Oh no, you can't play that move! That place is already filled! \nMove to which place instead?\n")
            continue

        if count >= 5:
            if GameBoard['7'] == GameBoard['8'] == GameBoard['9'] != ' ':
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")                
                break
            elif GameBoard['4'] == GameBoard['5'] == GameBoard['6'] != ' ':
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break
            elif GameBoard['1'] == GameBoard['2'] == GameBoard['3'] != ' ':
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break
            elif GameBoard['1'] == GameBoard['4'] == GameBoard['7'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break
            elif GameBoard['2'] == GameBoard['5'] == GameBoard['8'] != ' ': 
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break
            elif GameBoard['3'] == GameBoard['6'] == GameBoard['9'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break 
            elif GameBoard['7'] == GameBoard['5'] == GameBoard['3'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break
            elif GameBoard['1'] == GameBoard['5'] == GameBoard['9'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(" *** " +turn + " WON!!! Congratulations! ***\n")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It is a Tie!!!\n")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        

    restart = input("Do want to play again?(y/n): \n")
    if restart == "y" or restart == "Y":  
        for key in gameboard_keys:
            GameBoard[key] = " "

        game()

if __name__ == "__main__":
    game()