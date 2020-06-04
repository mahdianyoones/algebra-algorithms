import NumFactors
from termcolor import colored

def FindPrimes(end = 0, start = 2, howMany = 0):

    i = start

    foundPrimes = []

    while i <= end:
        factors = NumFactors.getFactors(i)
        if(len(factors) == 2):
            foundPrimes.append(i)
        if howMany > 0 and len(foundPrimes) == howMany:
            break;
        i += 1

    if howMany == 1:
        return foundPrimes[0]
    else:
        return foundPrimes

if __name__ == '__main__':

    number = int(input("Enter a number: "))
    print('Primes found:', FindPrimes(number))