import random

def main():
    hangman()


def hangman():
    # sowpods = <set equal to the location of sowpods.txt on your drive>
    dictionary = []  # stores list of words
    with open(sowpods,'r') as x:
        line = x.readline().strip()  
        while line:
            dictionary.append(line)
            line = x.readline().strip()
    
    turn_counter = 0
    figure = ['_','   |','   O','   |','  -|','  -|-','  /','  / \\']  # List of stick figure elements
    guessed_letters = []  # tracks previously guessed letters
    random_word = dictionary[random.randint(0,len(dictionary)-1)]  # Generates a random word from the dictionary list.
    answer = ""  # empty string to store the correctly guessed characters in their correct order
    for i in range(len(random_word)):  # sets answer variable equal to an amount of underscores that represent each character in the answer
        answer = answer + "_"
    
    word_value = 0  # variable that stores the value of the random word by converting each character to its ascii value and adding them together
    for i in range(len(random_word)):  # sets an integer value for the random word
        word_value = word_value + ord(random_word[i])

    print(f">>>> Welcome to Hangman!\n{answer}")

    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) > 1:  # if user inputs more than one character at a time, prompts the user to enter a new value
            print("Please select only one alphabetical character")
        elif guess == "" or not 64 < ord(guess) < 91:  # if the user enters nothing or anything other than a letter, prompts the user to enter a new value
            print("Please select an alphabetical character")
        elif guess in guessed_letters:  # if user enters a letter they've previously guessed, prompts the user to enter a new value
            print(f"You've already guessed {guess}!")
        else:
            guessed_letters.append(guess)
            for i in range(len(random_word)):
                if guess in random_word[i]:
                    answer = answer[:i] + guess + answer[i + 1:]  # replaces the underscores in the answer variable with the correct letter

            if guess not in random_word:  # lets the player know the letter is not in the answer and prints hangman
                print("Incorrect!")
                if turn_counter < 4:  # prints out gallows
                    print(figure[0] * (turn_counter + 1))
                elif turn_counter == 4:  # prints out the noose
                    print(f"{figure[0] * 4}\n{figure[1]}")
                elif turn_counter == 5:  # prints out the head
                    print(f"{figure[0] * 4}\n{figure[1]}\n{figure[2]}")
                elif 5 < turn_counter < 9:  # prints the torso
                    print(f"{figure[0] * 4}\n{figure[1]}\n{figure[2]}\n{figure[turn_counter - 3]}")
                else:  # prints the legs
                    print(f"{figure[0] * 4}\n{figure[1]}\n{figure[2]}\n{figure[5]}\n{figure[turn_counter - 11]}")

                print(answer)
                turn_counter += 1
                if turn_counter == 11:  # ends game after too many attempts
                    print(f"Game over!\nThe word was '{random_word}'")
                    break
            else:  # prints the letter(s) in the correct position
                print(answer)

            guess_value = 0  # variable that stores the value of the guessed letters by converting each character to its ascii value and adding them together
            for i in range(len(random_word)):  # gives guess_value an integer value to be compared against word_value
                if ord(answer[i]) != 95:  # only adds the correct letters to the guess_value and ignores underscores
                    guess_value = guess_value + ord(answer[i])
            
            if word_value == guess_value:  # breaks the loop once the word has been guessed
                print("You guessed the word!")
                break

            print(f"Guessed letters: {guessed_letters}")


main()