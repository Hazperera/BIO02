__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


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

    path.extend([k_mer[-1][1:k]])
    my_map = defaultdict(list)
    for i in range(len(path)-1):
        my_map[path[i]] += [path[i+1]]

    return my_map
#LL = 'AAGATTCTCTAAGA'
#kk = 4
#print(de_bruijin(LL,kk))