import prompt
import random
import math


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


def convert_to_int(data):
    try:
        int_data = int(data)
    except ValueError:
        return False
    return int_data


def check_answer(actual, expected):
    if actual == expected:
        print('Correct')
        return True
    else:
        return False


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

        if not check_answer(answer, correct_answer):
            wrong_answer_message(answer, correct_answer)
            return False
        counter += 1
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

        answer_int = convert_to_int(answer)
        if not answer_int:
            wrong_answer_message(answer, correct_answer)
            return False

        if not check_answer(answer_int, correct_answer):
            wrong_answer_message(answer, correct_answer)
            return False
        counter += 1
    return True


def quiz_gcd():
    counter = 0

    print('Find the greatest common divisor of given numbers.')
    while counter < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        correct_answer = math.gcd(number1, number2)

        answer = prompt.string(f'Question: {number1} {number2} ')
        print(f'Your answer: {answer}')

        answer_int = convert_to_int(answer)
        if not answer_int:
            wrong_answer_message(answer, correct_answer)
            return False

        if not check_answer(answer_int, correct_answer):
            wrong_answer_message(answer, correct_answer)
            return False
        counter += 1
    return True


def quiz_progression():
    counter = 0

    print('Find the greatest common divisor of given numbers.')
    while counter < 3:
        progression = []
        start_number = random.randint(0, 99)
        step = random.randint(1, 10)
        for i in range(6):
            progression.append(start_number)
            start_number += step
        index_of_random_element = random.randint(0, len(progression) - 1)
        correct_answer = progression.pop(index_of_random_element)
        progression.insert(index_of_random_element, '..')
        question_string = ' '.join(str(i) for i in progression)

        answer = prompt.string(f'Question: {question_string} ')
        print(f'Your answer: {answer}')

        answer_int = convert_to_int(answer)
        if not answer_int:
            wrong_answer_message(answer, correct_answer)
            return False

        if not check_answer(answer_int, correct_answer):
            wrong_answer_message(answer, correct_answer)
            return False
        counter += 1
    return True
