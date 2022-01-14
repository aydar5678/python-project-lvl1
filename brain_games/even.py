#!/usr/bin/env python

import prompt

import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello ' + name + '!')
    return name


def brain_even(name):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    you_winner = True
    for _ in range(0, 3):
        number = random.randint(1, 15)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and number % 2 == 0) or (answer == 'no' and number % 2 != 0):
            print("Correct!")
        if answer == 'yes' and number % 2 != 0:
            print(
                """'yes' is wrong answer ;(.
                Correct answer was 'no'.\nLet's try again, """ + name + '!')
            you_winner = False
            break
        if answer == 'no' and number % 2 == 0:
            print(
                """'no' is wrong answer ;(.
                Correct answer was 'yes'.\nLet's try again, """ + name + '!')
            you_winner = False
            break
        if answer != 'no' and answer != 'yes':
            print(answer + """ is not correct answer ;(.
            Let's try again, """ + name + '!')
            you_winner = False
            break
    if you_winner is True:
        print('Congratulation ' + name + '!')
