import pyAlgor.test_alg as test
import pyAlgor.mathematics.math_basic as mb
import pyAlgor.sort.sorting as sort
import pyAlgor.cryptography.rsa as rsa

print('test file')

# test.test_function('test input')

# output = test.squared(4)
# print(output)

# print('test gcd:')
# print(mb.greatest_common_divisor(49, 21))

# print('test extended euclidian alg')
# print(mb.extended_euclidian_algorithm(48, 21))

# print('test prime factors:')
# print(mb.prime_factors(48*5*17))

# print('test bubble sort')
# print(sort.bubble_sort([1,5,2,14,7,9,3]))

print('test rsa')
print(rsa.generate_keys(17, 41))