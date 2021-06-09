import sys
import random
import time


def hangman_screen(tries):
    stages = [  # 0
        """
                   --------
                   |      |
                   |      O
                   |     /|\ 
                   |      |
                   |     / \ 
                   |
                   -
                """,
        # 1
        """
                   --------
                   |      |
                   |      O
                   |     /|\ 
                   |      | 
                   |
                   |
                   -
                """,
        # 2
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   |
                   -
                """,
        # 3
        """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   |
                   -
                """,
        # 4
        """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


fin = open('words.txt')

words = [line.strip().lower() for line in fin.readlines()]

print("Welcome to Hangman game!")
print('Type "exit" to exit the game!')


def play_again():
    again = str(input("Do you want to play again (type y / n): "))
    if again == "y":
        play_game()
    else:
        print("Goodbye!")
        time.sleep(0.5)
        sys.exit()


def check_for_Blanks(myString):

    if myString and myString.strip():
        return False
    return True


def play_game():
    tries = 4
    hangman_screen(tries)

    while True:
        word = random.choice(words)

        length = len(word)

        print(f"Guess the word with {length} letters!")

        word_list = []

        for i in range(length):
            word_list.append('_')

        print(*word_list)

        used_chars = []

        while True:
            print("\n")
            letter = input("Guess a letter: ")

            if letter in used_chars:
                print("You have already guessed this letter")
                continue
            used_chars.append(letter)

            for i in range(length):
                if letter == word[i]:
                    word_list[i] = letter
            if '_' not in word_list:
                print("\n")
                print(f"You won! The word was: ", word)
                print("\n")
                time.sleep(0.5)
                play_again()
                break
            elif 'exit' in letter:
                print("Goodbye!")
                time.sleep(0.5)
                sys.exit()

            if letter not in word:
                if tries > 0:
                    print(hangman_screen(tries))
                    print(f"You have {tries} left")
                    tries -= 1
                elif tries == 0:
                    print(hangman_screen(tries))
                    print("\n")
                    print(f"You failed. The word was: ", word)
                    print("\n")
                    time.sleep(0.5)
                    play_again()
                    break

            print(*word_list)


play_game()
