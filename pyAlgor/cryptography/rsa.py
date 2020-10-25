#This import doesn't work, to be investigated
import mathematics.math_basic as mb

'''

'''
def generate_keys(p, q):
    n = p*q
    l = mb.least_common_multiple(p-1, q-1)
    #e should be coprime to l, we chose e as 3 to make it easy but in practise this is not secure
    e = 3
    d = mb.extended_euclidian_algorithm(e, l)[0]
    return n, e, d



'''
Encrypt a message
'''
def encrypt(message, key):
    return message, key



'''
Decrypt the cypher text
'''
def decrypt(cypher_text, key):
    return cypher_text, key