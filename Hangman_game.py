import random

# List of words 
words = ['apple', 'banana', 'orange', 'grape', 'pineapple','watermelon', 'strawberry', 'blueberry', 'peach', 'mango',
'cherry', 'lemon', 'kiwi', 'pear', 'plum', 'apricot', 'raspberry', 'blackberry', 'avocado', 'coconut',
'pomegranate', 'melon', 'lime', 'fig', 'papaya', 'cantaloupe', 'nectarine', 'passionfruit', 'guava', 'lychee',
'date', 'mulberry', 'dragonfruit', 'quince', 'cranberry']
# Game registration
gammer_title = input('Please Enter Mr. or Mrs.\n')
Gammer_name = input('Please Enter your name: \n')
# game_score = 0

#Choose game diff(iculty levels
# game_levels = int(input('''
# ******** Choose game difficulty levels**********       
#         <<<<<<   1.Normal 2.Medium 3.Hard >>>>>>
#             Please Enter a choice 1 or 2 or 3
# Enter Choice'''))
#game score initialization
#Select random words
def Select_rendom():
    return random.choice(words)
# display word status
def word_status(word, guessed_letters):
    display_word = ""
    for latter in word:
        if latter in guessed_letters:
            display_word += latter + ' '
        else:
            display_word +="_ "
    print(display_word)

def validate_guess(guess, guessed_letters):
    if len(guess) != 1:
        print('Please Enter Only Single Letter')
        return False
    elif  guess in guessed_letters :
        print('You already guessed that letter')
        return False
    elif not guess.isalpha():
        print('Please Enter a Letter')
        return False
    else:
        return True
    
def played_again():
    while True:
        play_again =input('Do you want to Play again or Quit This game ? \n (y/n):')
        if play_again.lower()== 'y':
            return True
        elif play_again.lower()== 'n':
            return False
        else:
            print('Kindly check your input- Invalid Input!, Enter only (y/n)')

def main_game():
#Game Start message
    print(f'::::::: welcome to Hangman Game :::::::\n :::::::::     {gammer_title} {Gammer_name}    :::::::::')
    word =Select_rendom()
    guessed_letters = []
    incorrect_attempts = 0
    while True:
        word_status(word, guessed_letters)
        guess = input('Guess a letter: ').lower()

        if not validate_guess(guess, guessed_letters):
            continue

        if guess in word:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print(f'Congratulations! You guessed the word {word} correctly. You win!')
                # game_score=game_score+1
                break
            else:
                print('Incorrect guess!')
                incorrect_attempts += 1
                if incorrect_attempts == 26:
                    print('You have run out of attempts. Game Over!')
                    break
    if not played_again():
        print(f'Thank you for playing Hangman, {gammer_title} {Gammer_name}.')
    else:
        print('Starting a new game...\n')
        main_game()
main_game()



# if game_levels ==1:
#     print(f''' ===== Hangman Game===== 
#           |||--- Player Name : {gammer_title} {Gammer_name} ______
#           |||--- Game mode   : <<<< Normal >>>> --Game Score -<< {game_score} >>''')
