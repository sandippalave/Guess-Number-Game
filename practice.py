import random

def guess(x):
    random_number = random.randint(1,x)

    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number: "))
        print(guess)
        if guess > x:
            print('Take a number between 1 and {}'.format(x))
        else:
            if guess<random_number:
                print('Too low.. Guess Again!')
            elif guess>random_number:
                print('Too high, Guess Again!')
            elif guess == random_number:
                print('Congratulations, You guessed right...')
                print('The Random Number was - ', random_number)



guess(10)

