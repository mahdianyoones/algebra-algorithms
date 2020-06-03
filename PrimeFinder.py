import NumFactors
from termcolor import colored

number = int(input("Enter a number: "))

factors = NumFactors.getFactors(number)

i = 2

foundPrimes = []

while i <= number:
    factors = NumFactors.getFactors(i)
    if(len(factors) == 2):
        foundPrimes.append(i)
    i += 1

print('Primes found:', foundPrimes)