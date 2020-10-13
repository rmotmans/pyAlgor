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
