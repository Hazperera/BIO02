__author__ = ('Mohammad Yousuf Ali,fb.com/aliyyousuf, aliyyousuf@gmail.com')

# Special Thanks to: Sanyk28 (san-heng-yi-shu@163.com) for generate_binary()

# Solve the k-Universal Circular String Problem.
#     Input: An integer k.
#     Output: A k-universal circular string.

# Sample Input:
#     4

# Sample Output:
#     0000110010111101


def generate_binary(k):                               # all the kmers
    return [bin(i)[2:].zfill(k) for i in range(2**k)]

from debruijinKmer import debruijin_k
from EulerCycle import euler_circle

#print(generate_binary(4))
binary_kmer = generate_binary(9)

debruijin_graph = (debruijin_k(binary_kmer))
debruijin_graph = dict(debruijin_graph)
euler_cycle = (euler_circle(debruijin_graph))
L = ''
for i in range(len(euler_cycle)-1):
    L += euler_cycle[i][0]
print(L)
#print(len(L))
#print(len(euler_cycle))
