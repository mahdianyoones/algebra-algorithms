def factors(number):
    divisor = 1
    quotient = number # just to make it bigger than the divisor for the while below to work

    factors = [] # list, ordered

    while quotient > divisor:
        if number % divisor == 0:
            quotient = number // divisor
            factors.append(quotient)
            factors.append(divisor)
        divisor += 1

    factors.sort()
    return factors

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

_factors = factors(dividend)

print(_factors)

if divisor in _factors:
    print('Devisible. ')
else:
    print('Non-divisible')