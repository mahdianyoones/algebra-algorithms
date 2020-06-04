import sys
from termcolor import colored

def IsPrime(number):
    divisor = 2
    quotient = number
    foundFactor = 0

    while quotient > divisor:
        if(number % divisor == 0):
            foundFactor = divisor
            break
        quotient = number // divisor
        divisor += 1

    if(foundFactor > 0):
        return False
    else:
        return True

if __name__ == '__main__':
    number = int(input('Enter a counting number: '))
    if(number == 1):
        print('1 is neither prime nor composite.')
        sys.exit(0)

    if(number < 1):
        print(colored('Number can\'t be smaller than 1!', 'red'))
        sys.exit(0)

    if IsPrime(number):
        print(colored(str(number) + ' is prime!'))
    else:
        print(colored(str(number) + ' is a composite number.'))