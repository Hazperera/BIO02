__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf, aliyyousuf@gmail.com'

# DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
# Input: A collection of k-mers Patterns.
# Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

# Sample Case:
# Input:
# GAGG
# CAGG
# GGGG
# GGGA
# CAGG
# AGGG
# GGAG

# Sample Output:
# AGG -> GGG
# CAG -> AGG,AGG
# GAG -> AGG
# GGA -> GAG
# GGG -> GGA,GGG


from collections import defaultdict

def debruijin_k(kmer):

    prep_sufx = []                                            # collection of prefix and suffix
    for mer in kmer:
        inti_prep_sufx = ()
        inti_prep_sufx = (mer[0:len(mer)-1],mer[1:len(mer)])  # find out prefix and suffix
        prep_sufx += [(inti_prep_sufx)]                       # collects them as tuple as pair [(prefix,suffix)]
    D = defaultdict(list)

    for k,v in prep_sufx:                                     # Visits each edge.
        D[k].append(v)                                      # Keep track of adjacency list.

    return D

#data_file = open('d_kmer.txt','r')
#data_file = data_file.readlines()
#data_in_List = []
#for line in data_file:
    #data_in_List += [line.rstrip()]                          # remove new line character
#test = debruijin_k(data_in_List)
#for k in sorted(test):
   #print(k, "->", ",".join(test[k]))                         # Print as question wants us to do that.
