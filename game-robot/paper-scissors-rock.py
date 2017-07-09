import random

run = True
print('Paper, scissors, rock playing program! Made by Me')
five = input('Best out of ten mode? (y/n) ')

count = 0
bestOutOfFive = False
if five == 'y':
    bestOutOfFive = True

results = {
    'player' : 0,
    'computer' : 0,
    'tie' : 0
}

while run:
    print('Enter p (paper), s (scissors), r (rock)')

    userIn = input(': ') #Get user input
    user = ''

    #Convert input to legal operation or else quit
    if userIn == 'p' or userIn == 'P':
        user = 'p'
    elif userIn == 's' or userIn == 'S':
        user = 's'
    elif userIn == 'r' or userIn == 'R':
        user = 'r'
    else:
        run = False

    #Work out computers answer
    options = ['p', 's', 'r']
    computer = random.choice(options)

    #Convert player to words
    player = ''
    if user == 'p':
        player = 'paper'
    elif user == 's':
        player = 'scissors'
    elif user == 'r':
        player = 'rock'

    #Convert computer to words
    computerWord = ''
    if computer == 'p':
        computerWord = 'paper'
    elif computer == 's':
        computerWord = 'scissors'
    elif computer == 'r':
        computerWord = 'rock'


    #Possible options:
    #Computer   Player  Outcome
    #P          P       Tie
    #S          S       Tie
    #R          R       Tie

    #P          S       Player
    #S          R       Player
    #R          P       Player

    #P          R       Computer
    #S          P       Computer
    #R          S       Computer

    #Work out who won!
    if user == computer:
        #Tie
        results['tie'] += 1
        print('You played ', player, ' but so did the computer! It was a tie.')
    elif computer == 'p' and user == 's' or computer == 's' and user == 'r' or computer == 'r' and user == 'p':
        #Player wins
        results['player'] += 1
        print('You played ', player, ' and the computer played ', computerWord, '. So you win!!')
    elif computer == 'p' and user == 'r' or computer == 's' and user == 'p' or computer == 'r' and user == 's':
        #Computer wins
        results['computer'] += 1
        print('You played ', player, ' but the computer played ', computerWord, '. So you lose. :(')

    count += 1
    if count == 10:
        run = False

print('')
print('Summary statistics:')
total = 0
for item in results:
    print(item, ' : ', results[item])
    total += results[item]

wins = results['player'] / total * 100
print('This means that you won ', wins, '% of the time')

if results['player'] > results['computer']:
    print('and you won more often than the computer!')
else:
    print('and the computer won more often than you.')