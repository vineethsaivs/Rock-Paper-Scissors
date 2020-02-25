from random import randint
player = input('fire(f), logs(l) or water(w)?')
print(player,'vs', end=' ')
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
    computer = 'f'
elif chosen == 2:
    computer = 'l'
else:
    computer = 'w'
print (computer)
    
if player == computer:
    print('Draw!')
elif player == 'f' and computer == 'l':
    print('Player Wins!!')
elif player == 'f' and computer == 'w':
    print('Computer Wins!!')
elif player == 'l' and computer == 'w':
    print('Player Wins')
elif player == 'l' and computer == 'f':
    print('Computer Wins!!')
elif player == 'w' and computer == 'l':
    print('Computer Wins!!')
elif player == 'w' and computer == 'f':
    print('Player Wins!!')
