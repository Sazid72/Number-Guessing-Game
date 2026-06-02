from random import randint


def main():
    n = int(input("Input a number. Computer will choose a number between 1 and your choosed number\n"))
    print(f"computer has choosed a number between 1 and {n}. Starting the game...")
    guess(n)
    print("Yey!!! You won...")








def guess(x):
    number = randint(1, x)
    guess = 0

    while guess != number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < number:
            print("You guissed a lower number! Please guess a higher number.")
        elif guess > number:
            print("You guessed a higher number! Please guess a lower one.")
        
            

if __name__ == "__main__":
    main()

