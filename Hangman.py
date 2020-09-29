import randomword

class RepeatedGuess(Exception):
    pass

# Function that displays the hangman status
def hang_man(turn_count):
    hangman_full = ['|', 'O', '|', '|', '\\', '/', '/', '\\']

    hangman_figure[turn_count] = hangman_full[turn_count]

    print('--------')
    print(f"|      {hangman_figure[0]}")
    print(f"|      {hangman_figure[1]}")
    print(f"|     {hangman_figure[4]}{hangman_figure[2]}{hangman_figure[5]}")
    print(f"|      {hangman_figure[3]}")
    print(f"|     {hangman_figure[6]} {hangman_figure[7]}")
    print("-")

# Main game function
def play():
    random_word = randomword.get_random_word()
    random_word_split = list(random_word)

    res = ['_'] * len(random_word)

    turn_count = 0
    guess_list = []

    while turn_count < 8:
        # Check user input
        try:
            guess = input('Please guess a letter or word: ')
            if guess in guess_list:
                raise RepeatedGuess
            guess_list.append(guess)
            # Display the below if user tries to guess a letter that he/she already guessed
        except RepeatedGuess:
            print("")
            print("You already guessed that, try again!")
            print("")

        # User wins the game if the word is guessed correctly
        if guess == random_word:
            print('You win!')
            break

        # Display a letter instead of underscore if a letter is guessed correctly
        elif guess in random_word_split:
            for count, value in enumerate(random_word_split):
                if guess == value:
                    res[count] = value.upper()
                else:
                    continue
            print(''.join(res))
        # Call the hang_man function and display the current status of hangman
        else:
            print(guess.upper() + ' is not in the word.')
            hang_man(turn_count)
            turn_count += 1

# This list will be used in the hang_man function
hangman_figure = [''] * 8

# The below is printed at the beginning of the game.
print('--------')
print(f"|      |")
print(f"|      O")
print(f"|     \|/")
print(f"|      |")
print(f"|     / \\")
print("-")

# Call the main function to start the game
play()

# Loss message if user doesn't guess the word by the end of the game.
print('You Lose!')