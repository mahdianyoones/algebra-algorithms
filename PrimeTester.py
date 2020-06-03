from termcolor import colored

number = int(input('Enter a counting number: '))

if(number < 2):
    print(colored('Number can\'t be smaller than 2!', 'red'))

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
    print(colored(str(number) + ' is not prime! Found factor: ' + str(divisor), 'blue'))
else:
    print(colored(str(number) + ' is prime!', 'green'))