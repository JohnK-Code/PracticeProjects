# The Magic-8-Ball Program
import time
import random

responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely' 'You may rely on it',
             'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
             'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
             'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very Doubtful']

print('Welcome to the magic-8-ball!')

def game():
    input('Please enter your question: ')
    print('thinking...')
    time.sleep(5)  # Sleep function used to pause programme for specified time in brackets (seconds)
    print(random.choice(responses))
    playAgain()


def playAgain():
    play = input('Would you like to play again?? (yes or no): '.lower())
    if play == 'y':
        print("\n\n")
        game()
    else:
        print('Goodbye!')


game()