import math
'''
Calculate the greatest common divisor of two integers a and b.
Using the Euclidian algorithm
'''
def greatest_common_divisor(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b
    
    return b

'''
Calculates the prime factors of an integer a
Returns an list
'''
def primeFactors(a):
    output = []
    
    while a % 2 == 0:
        output.append(2)
        a = a/2

    index = 3
    while index <= a:
        while a % index == 0:
            output.append(index)
            a = a/index
        index += 2

    return output