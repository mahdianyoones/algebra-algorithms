import NumFactors

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

factors = NumFactors.getFactors(dividend)

print('Factors of', dividend, ':', factors)

if divisor in factors:
    print('Devisible. ')
else:
    print('Non-divisible')