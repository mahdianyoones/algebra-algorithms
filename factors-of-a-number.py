number = int(input("Enter a number: "))

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

print(factors)