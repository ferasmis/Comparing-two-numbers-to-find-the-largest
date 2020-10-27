
## Author: Feras Isied
## Problem: A function called compare that compares two numbers
##  and returns the larger number between the two 

print('This program compares two integer numbers and displays the larger number!')
inputOne = int(input('Please enter a integer number: \n'))
inputTwo = int(input('Please enter a second integer number: \n'))


def compare(inputOne,inputTwo):
    if inputOne > inputTwo:
        print(str(inputOne) + ' is larger than ' + str(inputTwo) + '!')
    elif inputTwo > inputOne:
        print(str(inputTwo) + ' is larger than ' + str(inputOne) + '!')
    elif inputTwo == inputOne:
        print(str(inputOne) + ' is equal to ' + str(inputTwo) + '!')
    else:
        print('Error, please enter a valid integer!')
compare(inputOne,inputTwo)