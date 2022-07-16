import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def quiz():
    counter = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < 3:
        number = random.randint(1, 99)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = prompt.string(f'Question: {number} ')
        print(f'Your answer: {answer}')
        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            return False
    return True


def congratulate(name: str):
    print(f'Congratulations, {name}!')
