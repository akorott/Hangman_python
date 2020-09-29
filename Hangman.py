import randomword

class RepeatedGuess(Exception):
    pass

res = [''] * 8

def hang_man(turn_count):
    hangman_full = ['|', 'O', '|', '|', '\\', '/', '/', '\\']


    res[turn_count] = hangman_full[turn_count]

    print('--------')
    print(f"|      {res[0]}")
    print(f"|      {res[1]}")
    print(f"|     {res[4]}{res[2]}{res[5]}")
    print(f"|      {res[3]}")
    print(f"|     {res[6]} {res[7]}")
    print("-")


def underscore_to_letter():
    random_word = randomword.get_random_word()
    random_word_split = list(random_word)
    print(random_word_split)

    res = ['_'] * len(random_word)

    turn_count = 0
    guess_list = []

    while turn_count < 8:
        try:
            guess = input('Enter a letter: ')
            if guess in guess_list:
                raise RepeatedGuess
            guess_list.append(guess)
        except RepeatedGuess:
            print("")
            print("You already guessed that, try again!")
            print("")

        if guess == random_word:
            print('You win!')
            break

        elif guess in random_word_split:
            for count, value in enumerate(random_word_split):
                if guess == value:
                    res[count] = value.upper()

                else:
                    continue
            print(''.join(res))
        else:
            print(guess.upper() + ' is not in the word.')
            hang_man(turn_count)
            turn_count += 1

    print('You lose!')

print('--------')
print(f"|      |")
print(f"|      O")
print(f"|     \|/")
print(f"|      |")
print(f"|     / \\")
print("-")

underscore_to_letter()