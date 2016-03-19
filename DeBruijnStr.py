__author__ = 'Mohammad Yousuf Ali,fb.com/aliyyousuf,aliyyousuf@gmail.com'



# Special thanks: Jhon La Rooy, dawg,Garret R from stackoverflow.com
# De Bruijn Graph from a String
# Sample input: text = 'AAGATTCTCTAAGA', k = 4
# Sample output:
# AAG -> AGA,AGA
# AGA -> GAT
# ATT -> TTC
# CTA -> TAA
# CTC -> TCT
# GAT -> ATT
# TAA -> AAG
# TCT -> CTA,CTC
# TTC -> TCT

def composition(k,s):                                   # This function will make all kMers
    L = []
    for i in range(len(s)-k+1):
        L += [s[i:i+k] ]
    return L

def de_bruijin(text,k):
    from collections import defaultdict

    D = defaultdict(list)                               # Value will be saved in list format for each node.
    k_mer = composition(k,text)                         # Make all the Kmers
    path = [k_mer[0][:k-1]]                             # add the prefix of first kMer.

    for indx in range(0,len(k_mer)-1):
         if k_mer[indx][1:] == k_mer[indx+1][0:k-1]:    # if suffix == prefix of each kMer
             path.extend([k_mer[indx][1:k]])

    path.extend([k_mer[-1][1:k]])                       # Add the prefix of last Kmer
    adjaceny_list = zip(path,path[1:])                  # Make adjaceny list of all edges by 1st node with its adjacent node

    for chr1, chr2 in adjaceny_list:
        D[chr1].append(chr2)

    return D                                            # This function will return D containing the key as node and
                                                        # value as its adjacent node.
#LL = 'GTAGCATTTAACATCACACGGCTCCCTCCGAATAGCAAGTCTAATACAACCGGTTACAGTTCAGGTCGGCGCAAGAAAGTCAGCGCCAATTTATGTTCCCTGATCATACCGTCTCGTCGTATTCGGGATTAGGTGGACGTTGAGCTATCACCCAAAAGAGGTACATCCGCCGTCTGCACGTATGTAAGAACAGTACACTACTTCAGACGGCACGACATATATGAATACGGATAAGTTCTCGTACGGTGGAGAGCCTCAAGATCTGAGACCTTTTTGGCGACGTGTAGCTACGGCCGTATACTCGTGCCAATATGTTATAGCGCGATTTCCCTCCGCAAAATGACTCGACTAACAAGGTCGTTCTGTAGAAACTATATACCACCTTTGTGTCAATGGAAAGAGCTATCATCTGCGGGCGTTAACACACCCTTCAGGACTCGTTTGAAAGAAACACTGTTCTAGGTCGCCTCTGCCCCCCAGTGCGCATGCAAGGCATGAACAAAAACTTGACGTTACCGGCGGGTTGAGACGTTCAGTAGGGTGGCCCACGTGGATGATAAACAAAGCGAACTGTCAACCAACAGAGGAGGGGGCCCACACGCCTGTTGTCGTCTGACCCTCTCTCTTGGATTGGATACAAATTGTACCAGCTCAACACTATCTAAGGCCAGGGAGTAGTTTTATGGAGGGTGGCCAGGTGTAAATCTATTGGAAGCTCGGGTAAAGGAGCCCTGTCTTACACTTAATAGACAACGATCTCCGGGATTTGTCATTAATTAACATCACTACAAGTGCATAGTCAGGCCACCCCCGAGCCTACCCGGGAAGATCGCACATCATCCTCCGTAGGTCATTAAGCAAAACTAGATGCTACGCGTGGGAAGCCAGTGAGCATCGATTCGAGGTCTGGCCCGTATCGGATACTCAACCGTCCTTAGACGCTCTAAATATAACGTGGTGACGCATATCAGGTAGCCATGGGGGCCCTTGGTTCCTTGTGCTAAGTTTCTGGAATAAGGGGCAGGGATCCTCGCGGCCAATCCTCTCGTGGGATTCAACGACGCCGACGCGAAGGCCGTAACTCCTCTTTGGTCACCACCTTCGTACAGCCTTGCCACGAGCGGTATGTCCATACACACGCGCCTCGCTGGTCCGTAAGGATGTCTTAAGTCCGGTCAAAATCGAGACATGAACTAGCGCTATACGTCCATACGTCAGATGTTGTGTAAGCGCTAATTGCGCCACCACGAATCGGAGATTCCGGCATGTATATGCTGCCCCACATAATTCGGTACTCGGGTACACTTAGGTTACAAGATCTCTGAGGGTCTAGTAGGGGTGAGGTACCTGAGCCGAATATGTCCAGTTTCACTTGCTGTCAAAAGGTGCTTGTAGGACGACGTCCAAGTTCAATAGCAATGCCGACGGCTTGCGCGCAGGTGGACTAATGTGAAGAGGTTTTGCTTCGACGAATCGGCTGGTAATTGATCGCGGAACGCCTTTATTAACACACAATCAATAAAAGGTATAGTTTTTGCAAGACTGCAGATTTACCACAATGAAAGCGCTCCCCGACCTCCGACACGTGTCAAAAGTTTCCGTGTATCTGCCTATGGCTCTCTAGAGTTCAGCGTCCTGAGGAAGGGCTTATGGCCCGGCTGTCCGCAAACTTGACGCGTCGATACAATTGTGTCAGCGGAGAACGGTGAAGCGTTTAGCAAGTGGCGACGAAGCTCCCTCCACTGGCGCAAGGGTGCCAACGTTTGTGGCGTCAACCTCCCATTGCGGCGCAACCAGTCTACTGCGACCCTCTGGACGTGACGGTCTGTTCGCGCAGCAGATGCCGATCGAGTAATTCGCTACCCGGCCCCGGATTGCCAGTGGCCGCGACCGGTCGAGCCCGTAGTTGGACTATATACATGATGGGTCCACCACAAATTCCTTCAACTCTGACAATTACGGCGCTGAGCTCCCTCCACAGAGTGATGACTTAAGGAGCA'

#kk = 12
#testing_case = de_bruijin(LL,kk)
#for k in sorted(testing_case):
   #print(k, "->", ",".join(testing_case[k]))            # Here we printing out the way instruction wants us to print.