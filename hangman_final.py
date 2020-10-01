import random
import os
import time


def main():
    lives, word = difficulty()
    play(word, lives)


hanger = [
"""
  +---+
  |   |
  O   |
 /|\  | RIP
 / \  |
      |
========= """,
"""
  +---+
  |   |
  O   |
 /|\  | CLOSE...
 /    |
      |
========""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
   +---+
   |   |
       |
       |
       |
       |
=========""",
]


def difficulty():
    os.system('clear')
    global lives
    global word
    with open("countries-and-capitals.txt", mode="r") as countries:
        read_in = countries.readlines()
        full_list = list(read_in)
        country_list = []
        for i in full_list:
            country_list.append(i.split(" |")[0])
    print("Welcome in Hangman! Have fun!")
    print("\n")
    print("Please, choose a difficulty level!")
    print("\n")
    choice = input("Type [E] for easy or [H] for hard mode: ").upper()
    while choice not in {"E", "H"}:
        choice = input("Please choose between \"E\" for easy or \"H\" for hard mode: ").upper()
    if choice == "E":
        lives = 6
        word = random.choice(country_list)
        while len(word) > 7:
            word = random.choice(country_list)
    elif choice == "H":
        lives = 4
        word = random.choice(country_list)
        while len(word) <= 7:
            word = random.choice(country_list)
    return lives, word


def casesensitive(guess, guess_pool):
    guess_pool.append(guess.upper())
    guess_pool.append(guess.lower())
    guess_set = set(guess_pool)
    return guess, guess_pool, guess_set


def working(word, guess_pool, guess_set):
    word_as_list = list(word)
    word_comp = "_" * len(word)
    word_board = list(word_comp)
    count = 0
    for i in word:
        if i in guess_pool:
            word_board[count] = word_as_list[count]
        count += 1
    return word_board


def gamestate(lives, word_board):
    os.system('clear')
    str1 = ""
    wordstate = str1.join(word_board)
    if lives == 6:
        print(hanger[lives])
    elif lives == 5:
        print(hanger[lives])
    elif lives == 4:
        print(hanger[lives])
    elif lives == 3:
        print(hanger[lives])
    elif lives == 2:
        print(hanger[lives])
    elif lives == 1:
        print(hanger[lives])
    separator = " "
    print("\n")
    print("Word to Guess: ", separator.join(wordstate), " Chances: ", lives)
    print("\n")


def capitalize_list(item):
    item = ''.join(c for c in item if c.isalpha())
    item = item.upper()
    return list(set(item))


def get_guess(guess_pool):
    global epic
    epic = 0
    guess = input("What's your next guess? Give me a letter: ")
    while len(guess) <= 0:
        guess = input("Empty input! Please give me a letter!")
    letlow = list(word.lower())
    letupp = list(word.upper())
    letters = set(letlow + letupp)
    tester = set(guess_pool)
    casesensitive(guess, guess_pool)
    guess_set = capitalize_list(tester)
    if guess == "quit":
        print("Thanks for playing. Goodbye!")
        print("The word was:", word)
        time.sleep(4)
        os.system('clear')
        os._exit(0)
    elif guess not in letters and guess not in tester:
        print("Not in your word, try something else!")
        print("You already guessed these letters: ", guess_set)
        epic = 1
        time.sleep(1.5)
    elif guess in letters and guess not in tester:
        print("Nice catch!", guess.upper(), " is in your word!")
        epic = 0
        time.sleep(1.2)
    elif guess in tester:
        print("You already guessed that letter:", guess.upper(), "Try something else!")
        print("You guessed these letters so far: ", guess_set)
        epic = 0
        time.sleep(1.5)
    else:
        print("Try again.")
        time.sleep(1)
    return guess_pool, epic


def play(word, lives):
    guess_pool = [' ']
    while lives >= 1:
        word_board = working(word, guess_pool, guess_set)
        gamestate(lives, word_board)
        if word_board == list(word):
            print("Congratulations, You got it! Good job!")
            print("\n")
            replay = input("Wanna play again? [Y]/[N]").upper()
            while replay not in {"Y", "N"}:
                replay = input("Wanna play again? [Y]/[N]").upper()
            if replay == "Y":
                main()
            if replay == "N":
                print("Thanks for playing! Have a nice day!")
                os._exit(3)
            time.sleep(5)
        get_guess(guess_pool)
        if epic == 1:
            lives -= 1
        working(word, guess_pool, guess_set)
        gamestate(lives, word_board)
    if lives < 1:
        os.system('clear')
        print("The word was: ", word)
        print(hanger[lives], "Whoops... that happened! Better luck next time!")
        time.sleep(2)
        print("\n")
        regame = input("Wanna play again? [Y]/[N] ").upper()
        while regame not in {"Y", "N"}:
            regame = input("Wanna play again? [Y]/[N] ").upper()
        if regame == "Y":
            main()
        elif regame == "N":
            print("Thanks for playing! See you soon!")
            os._exit(3)


if __name__ == "__main__":
    guess_pool = [' ']
    word_as_print = ""
    guess_set = set(guess_pool)
    word_as_list = []
    word_sliced = []
    word_board = ""
    main()
