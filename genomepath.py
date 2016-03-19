__author__ = 'Mohammad Yousuf Ali. aliyyousuf@gmail.com'


#String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
# #Input: A sequence of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of
# Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
#Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni
# (for 1 ≤ i ≤ n).
# Sample Input:
# ACCGA
# CCGAA
# CGAAG
# GAAGC
# AAGCT

# Sample Output:
# ACCGAAGCT

def genome_path(L):
    LL = L[0]
    for i in range(1,len(L)):
        LL += L[i][-1]
    return LL

#f = open('genomepath.txt','r')
#f = f.readlines()
#s = []
#for line in f:
    #s += [line.rstrip()]
#print(s)
#L =['GGC', 'GCT', 'CTT', 'TTA', 'TAC', 'ACC', 'CCA']
#print(genome_path(s))