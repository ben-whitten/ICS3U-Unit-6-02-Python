#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This is a program which generates 10 random numbers and finds the average.

import random


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def greatest_number(list_of_numbers, rounds):

    highest_number = 0

    for loop_counter_2 in range(0, rounds):
        if list_of_numbers[loop_counter_2] > highest_number:
            highest_number = list_of_numbers[loop_counter_2]

    return highest_number


def main():
    # This is what runs the program.

    random_number = []

    string_of_rounds = input("Input how many numbers you'd like to generate: ")
    min_as_string = input("What do you want the minimum number to be: ")
    max_as_string = input("What do you want the maximum number to be: ")

    try:
        number_of_rounds = int(string_of_rounds)
        minimum = int(min_as_string)
        maximum = int(max_as_string)

        for loop_counter in range(0, number_of_rounds):
            number = random.randint(minimum, maximum)
            random_number.append(number)
            print(color.YELLOW + "{0}".format(random_number[loop_counter]),
                  end=" | " + color.END)

        highest_number = greatest_number(random_number, number_of_rounds)
        print("")
        print(color.GREEN + "Highest = {0}".format(highest_number) + color.END)

    except Exception:
        print('')
        print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
              ' number...' + color.END)
        print("")
        print("")


if __name__ == "__main__":
    main()
