#!/usr/bin/env python
from brain_games.utils import greet, welcome_user, quiz_even, congratulate


def main():
    greet()
    name = welcome_user()
    if quiz_even():
        congratulate(name)
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
