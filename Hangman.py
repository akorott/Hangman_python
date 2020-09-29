import randomword
import time

def hanging():
    guess1 = '|'
    guess2 = 'O'
    guess3 = '|'
    guess4 = '\\'
    guess5 = '/'
    guess6 = '|'
    guess7 = '/'
    guess8 = '\\'

    print('--------')
    print(f"|     {guess1}")
    print(f"|     {guess2}")
    print(f"|    {guess4}{guess3}{guess5}")
    print(f"|     {guess6}")
    print(f"|    {guess7} {guess8}")
    print("-")

print('Welcome to Hangman!')

# time.sleep(1)
print('You have 8 tries to guess the word!')

print(hanging())

print("Let's begin!")
print("Please guess a letter or word:")

random_word = randomword.get_random_word()
print(random_word)
blank_spaces = '_ ' * len(random_word)
print(blank_spaces)

def user_guess():
    counter = 0
    answer = ''
    try:
        guess = input()
    except:
        ValueError

print(user_guess())








