# Code taken and adapted from memory.py

import random
import os
import time

# Constants
DEFAULT_SPLITTER = ' '
MY_DIR = os.path.realpath(os.path.dirname(__file__))
DICTIONARIES_DIR = os.path.join(MY_DIR, 'dictionaries')

CORRECT_RESPONSE = ['correct', 'correct', 'well done', 'thats it', 'your on your way', 'nice', 'good job']
INCORRECT_RESPONSE = ['wrong', 'incorrect', 'incorrect', 'try again later', 'you will get there', 'oh no', 'wrong']

# Settings
WORD_LENGTH = 8

# os.system("clear")
# os.system("say " + {{WORD}})

def respond (correct):
    if correct:
        response = random.choice(CORRECT_RESPONSE)
        os.system('say ' + response)
    else:
        response = random.choice(INCORRECT_RESPONSE)
        os.system('say ' + response)

def learn (words):
    '''Actually run the loops of code'''
    incorrect = []
    stats = {
        'first_correct' : 0,
        'first_incorrect' : 0,
        'round' : 1,
        'total_correct' : 0,
        'total_incorrect' : 0
    }
    random.shuffle(words)
    for word in words:
        word = word.lower()
        # Test the person
        os.system('clear')
        while True:
            os.system('say ' + word)
            print('DEBUG: ', word)
            spell = input('?= ')

            if spell.lower() == word:
                # They got it right
                print('Correct!')
                respond(True)
                stats['first_correct'] += 1
                stats['total_correct'] += 1
                time.sleep(1.5)
                break

            elif spell == '-':
                # They want to hear the word again
                continue

            else:
                # They got it wrong
                incorrect.append(word)
                respond(False)
                stats['first_incorrect'] += 1
                stats['total_incorrect'] += 1
                print('Incorrect.\nCorrect spelling was',word)
                halt = input('(Press enter to continue)')
                time.sleep(0.5)
                break
    while incorrect.__len__() > 0:
        os.system('clear')
        stats['round'] += 1
        print('Round', stats['round'], '. Retesting on', incorrect)
        halt = input('(Enter to resume)')
        random.shuffle(incorrect)
        to_remove = []
        for word in incorrect:
            word = word.lower()
            os.system('clear')
            while True:
                os.system('say ' + word)
                print('DEBUG: ', word)
                spell = input('?= ')

                if spell.lower() == word:
                    # They got it right
                    respond(True)
                    print('Correct!')
                    stats['total_correct'] += 1
                    to_remove.append(word)
                    time.sleep(1.5)
                    break

                elif spell == '-':
                    # They want to hear the word again
                    continue

                else:
                    # They got it wrong
                    respond(False)
                    stats['total_incorrect'] += 1
                    print('Incorrect.\nCorrect spelling was', word)
                    halt = input('(Press enter to continue)')
                    time.sleep(0.5)
                    break
        # Remove all words spelled correct
        for word in to_remove:
            incorrect.remove(word)

    os.system('clear')
    print('Summary stats...')
    os.system('say done!')

    first_per = round((stats['first_correct']/(stats['first_incorrect']+stats['first_correct'])*100), 2)
    total_per = round((stats['total_correct'] / (stats['total_incorrect'] + stats['total_correct'])*100), 2)

    message = {
    1 : ('You spelt ' + str((stats['total_incorrect'] + stats['total_correct'])) + ' words over ' + str(stats['round']) + ' rounds.'),
    2 : ('You spelt ' + str(stats['first_correct']) + ' words right and ' + str(stats['first_incorrect']) + ' words wrong in your first round which gave you a ' + str(first_per) + '% word success rate'),
    3 : ('In total you spelt ' + str(total_per) + '% of your words right in all your rounds.'),
    4 : ('Thanks for playing!')
    }

    for i in message:
        print(message[i])
def setup (words):
    '''Setup the words and use any custom settings'''

    # Take a five hundred words sample if words are over this limit
    if words.__len__() > 500:
        words = random.sample(words, 500)
        print('Taking 500 word sample')

    # Do any settings the user wants
    print('Removing words longer than', WORD_LENGTH, 'characters.')
    to_remove = []
    for word in words:
        # Do something...
        if word.__len__() > 8:
            to_remove.append(word)

    # Remove the words
    for word in to_remove:
        words.remove(word)

    if words.__len__() > 30:
        # Choose 30 words from this list
        final_words = random.sample(words, 30)
    else:
        final_words = words

    print('Words to be tested on:\n', final_words)
    halt = input('Ready? (Enter)')
    learn(final_words)

def main():
    print('Learn Spelling Words App')
    method = input('Would you rather input your words manually (1), or randomise a loaded dictionary (2)?\n: ')

    if method == '1':
        # They want to paste in words
        print('Enter the character that you want to have your words split by. Usually a space or newline character.')
        splitter = input('Press enter for default (space) or enter yours here: ')
        if splitter == '':
            splitter = DEFAULT_SPLITTER
        message = 'Please paste or type your words below seperated by "' + splitter + '"s\n'
        words_raw = input(message)
        words = words_raw.split(splitter)
        setup(words)

    elif method == '2':
        # They want to load a dictionary
        available = os.listdir(DICTIONARIES_DIR)
        print('Please choose a number from one of the available dictionaries below:')
        count = 0
        for dictionary in available:
            print(count, ' : ', dictionary)
            count += 1
        number = int(input(': '))
        try:
            dictionary = available[number]
        except:
            print('There was an error with your input')
            return
        print(dictionary)

        try:
            fname = os.path.join(DICTIONARIES_DIR, dictionary)
            with open(fname, 'r') as input_file:
                words_raw = input_file.read()
        except:
            print('There was an error loading your dictionary')
            return
        words = words_raw.split('\n')
        setup(words)

    else:
        print('Error: Invalid option')
        return

if __name__ == '__main__':
    main()
