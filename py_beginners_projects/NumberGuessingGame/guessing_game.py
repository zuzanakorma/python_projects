from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


logo = """
  _____                   ________         _  __           __          
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   
                                                                       
"""
print(logo)

# function = check guess against actual number
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        # track number of guesses and reduce by one
        return turns - 1
    elif guess < answer:
        print("Too low")
        # track number of guesses and reduce by one
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# let user choose difficulty
def set_difficulty():
    level = input("Choose difficulty, easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # choosing random number between 1 and 100
    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f" Secret number is {answer}")

    turns = set_difficulty()

    
    # repeate guessing if they are wrong
    guess = 0

    while guess != answer:
        print(f"you have {turns} attempts remaining to guess.")

        # let user guess a number
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            # return statment to exit the game == close the function game!
            return
        elif guess != answer:
            print("Guess again: ")


game()


