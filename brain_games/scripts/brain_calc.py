#!/usr/bin/env python
from brain_games.utils import greet, welcome_user, quiz_calc, congratulate


def main():
    greet()
    name = welcome_user()
    if quiz_calc():
        congratulate(name)
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
