import sys
from termcolor import colored
import PrimeTester
import PrimeFinder

def FindPrimeFactorsLadder(number):
    
    if number == 1 or PrimeTester.IsPrime(number):
        return str(number) + ' is not composite'
            
    primeFactors = []
    dividend = number
    divisor = PrimeFinder.FindPrimes(number, 2, 1)

    while True:        
        if dividend % divisor > 0:
            divisor = PrimeFinder.FindPrimes(number, divisor + 1, 1)
            continue

        primeFactors.append(divisor)

        dividend = dividend // divisor

        if(PrimeTester.IsPrime(dividend)):
            primeFactors.append(dividend)
            break
    
    return primeFactors

if __name__ == '__main__':
    number = int(input('Enter a composite number: '))
    print(FindPrimeFactorsLadder(number))