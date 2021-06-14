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


def startInterface():
    print(' 1.English')
    print(' 2.Deutsche')
    print(' 3.Español')
    choice = input('Input Selection: ')
    return choice


def startInterface2():
    print(' 1.Easy')
    print(' 2.Medium')
    print(' 3.Expert')
    choice = input('Input Selection: ')
    return choice


sel = startInterface()
sel2 = startInterface2()

print("Welcome to Hangman game!")
print('Type "exit" to exit the game!')


def play_again():
    again = str(input("Do you want to play again (type y / n): "))
    if again == "y":
        process_file()
    else:
        print("Goodbye!")
        time.sleep(0.5)
        sys.exit()


def process_file():
    if sel == '1' and sel2 == '1':
        lang = 'english'
        mode = 'easy'
    elif sel == '1' and sel2 == '2':
        lang = 'english'
        mode = 'medium'
    elif sel == '1' and sel2 == '3':
        lang = 'english'
        mode = 'expert'
    elif sel == '2' and sel2 == '1':
        lang = 'deutsche'
        mode = 'easy'
    elif sel == '2' and sel2 == '2':
        lang = 'deutsche'
        mode = 'medium'
    elif sel == '2' and sel2 == '3':
        lang = 'deutsche'
        mode = 'expert'
    elif sel == '3' and sel2 == '1':
        lang = 'español'
        mode = 'easy'
    elif sel == '3' and sel2 == '2':
        lang = 'español'
        mode = 'medium'
    elif sel == '3' and sel2 == '3':
        lang = 'español'
        mode = 'expert'
    else:
        print("choose language and mode")

    fin = open(f"data/{lang}/{mode}.txt", encoding='utf-8')
    words = [line.strip().lower() for line in fin.readlines()]

    words = random.choice(words)
    word = words.split(" - ", 1)

    length = len(word[0])
    word_list = []
    print(f"Guess the word with {length} letters!")
    for i in range(length):
        word_list.append('_')
    print(*word_list)
    tries = 4
    hangman_screen(tries)

    used_chars = []
    g_score = 10
    while True:
        print("for hint write word hint")
        print("\n")

        letter = input("Guess a letter: ")

        if letter == 'hint':
            print(word[1])
            g_score -= 5
            continue

        if letter in used_chars:
            print("You have already guessed this letter")
        used_chars.append(letter)

        for i in range(length):
            if letter == word[0][i]:
                word_list[i] = letter

        if '_' not in word_list:
            print("\n")
            print(f"You won! The word was: ", word[0])
            print('Your score is: ', g_score)
            print("\n")
            time.sleep(0.5)
            play_again()
            break
        elif 'exit' in letter:
            print("Goodbye!")
            time.sleep(0.5)
            sys.exit()

        if letter not in word[0]:
            if tries > 0:
                print(hangman_screen(tries))
                print(f"You have {tries} left")
                tries -= 1
                g_score -= 1
            elif tries == 0:
                print(hangman_screen(tries))
                print("\n")
                print(f"You failed. The word was: ", word[0])
                print('Your score is: ', g_score)
                print("\n")
                time.sleep(0.5)
                play_again()
        print(*word_list)


process_file()
