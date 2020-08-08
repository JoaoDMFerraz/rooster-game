import pandas as pd
game=pd.DataFrame({1:['_','_','_'] ,2:['_','_','_'],3:['_','_','_'] })
keyboard_positions=pd.DataFrame({1:[7,4,1],2:[8,5,2],3:[9,6,3]})

# function to check who's the winner ; x-columns; y-rows
def winner(plA,plB):
    
    win=False
    winnerAB=''
    
    #check columns
    for x in range(1,4):
        if (game[x][0]==u"\u25A0" and game[x][1]==u"\u25A0" and game[x][2]==u"\u25A0"):
            win=True
            winnerAB = plA
        elif (game[x][0]==u"\u25A1" and game[x][1]==u"\u25A1" and game[x][2]==u"\u25A1"):
            win=True
            winnerAB = plB
            
    #check rows
    for y in range(3):
        if (game[1][y]==u"\u25A0" and game[2][y]==u"\u25A0" and game[3][y]==u"\u25A0"):
            win=True
            winnerAB = plA
        elif (game[1][y]==u"\u25A1" and game[2][y]==u"\u25A1" and game[3][y]==u"\u25A1"):
            win=True
            winnerAB = plB
            
    #check diagonals
    if (game[1][0]==u"\u25A0" and game[2][1]==u"\u25A0" and game[3][2]==u"\u25A0"):
        win=True
        winnerAB = plA
    elif (game[1][0]==u"\u25A1" and game[2][1]==u"\u25A1" and game[3][2]==u"\u25A1"):
        win=True
        winnerAB = plB
    
    if (game[3][0]==u"\u25A0" and game[2][1]==u"\u25A0" and game[1][2]==u"\u25A0"):
        win=True
        winnerAB = plA
    elif (game[3][0]==u"\u25A1" and game[2][1]==u"\u25A1" and game[1][2]==u"\u25A1"):
        win=True
        winnerAB = plB
    
    #check if it is a draw
    drawf=False
    
    if (game[1][0]!='_' and game[2][0]!='_' and game[3][0]!='_' and game[1][1]!='_' and game[2][1]!='_' and game[3][1]!='_' and game[1][2]!='_' and game[2][2]!='_' and game[3][2]!='_'):
        drawf=True
        
    return win , winnerAB, drawf

# the function that displays each player move; x-columns; y-rows
def jogada(a,TurnAB):
    for x in range(1,4):
        for y in range(3):
            if keyboard_positions[x][y]==a:
                if game[x][y]!='_':
                    exit()
                elif TurnAB=='A':
                    game[x][y]=u"\u25A0"
                elif TurnAB=='B':
                    game[x][y]=u"\u25A1"
    
    return print(game.head())

#The program starts here.

draw=False
win=False

print('This is the matrix to play the rooster game, where each number in your keyboard')
print('corresponds to one of the squares in the rooster game!')
print('7 | 8 | 9')
print('4 | 5 | 6')
print('1 | 2 | 3')
print('Write your names and good luck! \n')

player_A = input('What is the name of the 1st player? ')
player_B = input('What is the name of the 2nd player? ')

while (win==False or draw==False):
    draw=False
    
    print('\n')
    ja=input(player_A + ': ')
    ja=int(ja)
    jogada(ja,'A')
    
    if winner(player_A,player_B)[0]==True:
        win = True
        print('\n The winner is ',winner(player_A,player_B)[1])
        break
    elif winner(player_A,player_B)[2]==True:
        draw = True
        print('\n It is a draw')
        break
    
    print('\n')
    jb=input(player_B + ': ')
    jb=int(jb)
    jogada(jb,'B')
    
    if winner(player_A,player_B)[0]==True:
        win = True
        print('\n The winner is ',winner(player_A,player_B)[1])
        break
    elif winner(player_A,player_B)[2]==True:
        draw = True
        print('\n It is a draw')
        break
