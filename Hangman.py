import randomword
import time

print('--------')
print(f"|     |")
print(f"|     O")
print(f"|    \|/")
print(f"|     |")
print(f"|    / \\")
print("-")

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


print('You have 8 tries to guess the word!')

random_word = randomword.get_random_word()
random_word_split = list(random_word)

print(random_word_split)
blank_spaces = '_ ' * len(random_word)
print(blank_spaces)

# def user_guess():
#     counter = 0
#     answer = ''
#     try:
#         guess = input()
#     except:
#         ValueError
#
# print(user_guess())



count = 0
while count < 8:
    guess = input('Guess a letter or word: ')
    if guess in random_word_split or guess == random_word:
        hanging(guess)
        print('Nice!')
    else:
        count += 1
        print('incorrect')

print('You lose!')








