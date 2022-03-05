import os
import random


def clear(): return os.system('cls')


def play_again():

    while True:
        again = input('Would you like to play again?? Y/N ').lower()
        if again == 'y' or again == 'yes':
            clear()
            return True
        elif again == 'n' or again == 'no':
            return False
        else:
            print("This character is not valid")


def game(chance, word, correct_guess_list, total_guess_list):

    i = 0
    while i < chance:

        print_hangman(i)
        print_word(word, correct_guess_list)

        user_guess = input('\Please guess:  ').lower()
        if user_guess.isalpha() == False or len(user_guess) != 1:
            clear()
            print("This character is not valid")
            continue

        if user_guess in total_guess_list:
            clear()
            print('\you have used this before!\n')
            continue
        else:
            if user_guess in word:
                correct_guess_list.append(user_guess)
            else:
                i += 1

        total_guess_list.append(user_guess)

        if game_over(correct_guess_list, word):
            return True

        clear()

    print_hangman(i)
    return False


def game_over(correct_guesses, word):
    for l in word:
        if l not in correct_guesses:
            return False
    return True


def print_word(word, guess):
    print('\n')
    for l in word:
        if l in guess:
            print(l, end=' ')
        else:
            print('_', end=' ')


def print_hangman(stage):
    hangman = [
        '''
        
        
        
        
        
      __|__
        ''',

        '''
        
        |
        |
        |
        |
        |
      __|__
      
        ''',

        '''
         _____
        |
        |
        |
        |
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |
        |
        |
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |     0
        |
        |
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |     0
        |    /
        |
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |     0
        |    /|
        |
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |     0
        |    /|\\
        |
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |     0
        |    /|\\
        |    /
        |
      __|__
      
        ''',

        '''
         _____
        |     |
        |     0
        |    /|\\
        |    / \\
        |
      __|__
      
        '''
    ]

    print('\n', hangman[stage])


word_list = ['canada', 'chile', 'danmark', 'iran', 'germany', 'holland', 'india','japan','turkey']
chances = 10

while True:

    correct_guess_list = ['']
    total_guess_list = ['']

    word = random.choice(word_list)

    win = game(chances, word, correct_guess_list, total_guess_list)

    if win == True:
        print('\n\n!!good job, You WIN!!\n')
    else:
        print('\n\n!!i am sorry!!\n')

    if play_again() == False:
        break