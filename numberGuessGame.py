import random


def main():
    name = input("Please enter your lovely name: ")
    print("hello {}".format(name))
    select()

def select():
    opt = input("Do you like to play number guessing game with me?(y/n)")
    if (opt == 'n'):
        print('Hey thanks being with me! Have a lovely journey')
    elif (opt == 'y'):
        start()
    else:
        print('Please enter valid option!')
        select()



def start():
    print('OK, lets play a game')
    lower, upper = [x for x in input('type a number for lower and upper bound').split()]
    if lower.isdigit():
        lower = int(lower)
    if upper.isdigit():
        upper = int(upper)

    secret = random.randint(lower, upper)
    guess = None
    count = 1

    while guess != secret:
        guess = input('Can you guess what number I am thinking between {} & {}'.format(lower, upper))
        if guess.isdigit():
            guess = int(guess)

        if guess == secret:
            print('Well done! You got it')
        elif guess < secret:
            print('You are close to answer, number is greater than you guessed ')
            count += 1
        elif guess > secret:
            print('You are close to answer, number is smaller than you guessed ')
            count += 1

    print('It took you ', count, 'guess/guesses')


main()







