import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congratulate(name: str):
    print(f'Congratulations, {name}!')


def wrong_answer_message(actual, expected):
    print(
        f"'{actual}' is wrong answer ;(. "
        f"Correct answer was '{expected}'"
    )


def get_operation_result(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    else:
        return number1 * number2


def quiz_even():
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
            wrong_answer_message(answer, correct_answer)
            return False
    return True


def quiz_calc():
    counter = 0

    print('What is the result of the expression?')
    while counter < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operation = random.choice(['+', '-', '*'])
        correct_answer = get_operation_result(number1, number2, operation)

        answer = prompt.string(f'Question: {number1} {operation} {number2} ')
        print(f'Your answer: {answer}')

        try:
            answer = int(answer)
        except ValueError:
            wrong_answer_message(answer, correct_answer)
            return False

        if answer == correct_answer:
            counter += 1
            print('Correct!')
        else:
            wrong_answer_message(answer, correct_answer)
            return False
    return True
