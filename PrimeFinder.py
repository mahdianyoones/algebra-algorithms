import NumFactors
from termcolor import colored

number = int(input("Enter a number: "))

factors = NumFactors.getFactors(number)

i = 2

while i <= number:
    factors = NumFactors.getFactors(i)
    if(len(factors) == 2):
        print(colored(str(i) + ' is a prime. Factors', 'green'), colored(factors, 'green'))
    else:
        print(i, 'is not a prime. Factors', factors)
    i += 1