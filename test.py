import pyAlgor.test_alg as test
import pyAlgor.math.math_basic as mb

print('test file')

test.test_function('test input')

output = test.squared(4)
print(output)

print('test gcd:')
print(mb.greatest_common_divisor(49, 21))

print('test prime factors:')
print(mb.primeFactors(48*5*17))