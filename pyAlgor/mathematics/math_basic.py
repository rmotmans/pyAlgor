#import math

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
Extended Euclidian Algorithm.
As extension on the Euclidian algorithm, this algorithm computes the coefficients x and y such that:
a*x + b*y = gcd(a,b)l
'''
def extended_euclidian_algorithm(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a!= 0:
        q, r = b//a, b%a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y                           




'''
Calculate the least common multiple of two integers a and b.
Using the greatest common divisor algorithm
'''
def least_common_multiple(a, b):
    return a*b/greatest_common_divisor(a, b)



'''
Calculates the prime factors of an integer a
Returns an list
'''
def prime_factors(a):
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


'''
Primality check.
Returns True or Falses
'''
def is_prime(a):
    return ''



'''
Fibonacci sequence
Returns the n'th value of the sequence
'''
def fibonacci(n, memo = {}):
    if n == 1:
        return 0
    if n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]



'''
howSum function
Input an integer and a list of integers.
Returns a list of integers from the input list that sum up to the input integer if possible, 
otherwise returns null (None)
'''
def how_sum(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for number in numbers:
        remainder = targetSum - number
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            remainder_result.append(number)
            memo[targetSum] = remainder_result
            return remainder_result
    
    memo[targetSum] = None
    return None
