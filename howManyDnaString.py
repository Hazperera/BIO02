__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'

# How many DNA strings of length 30 transcribe and translate into Tyrocidine B1?

# Recall that the amino acid sequence of Tyrocidine B1 is:
# Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr.
# We also reproduce the genetic code figure below.

def rna_codon(file_name):            # this function will make a dictionary of codon to amino acid

    file_name = open(file_name,'r')
    D = {}
    L = []
    for line in file_name:
        L += [line.rstrip().split()]
    for i in L:
        if len(i) == 1:
            D[i[0]] = ''
        else:
            D[i[0]] = i[1]
    return D

D = rna_codon('rna_codon.txt')
amino_acid1 = 'Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr' # Convert them into single codon
amino_acid2 = 'VKLFPWFNQY'
codon = list(D.values())
how = 1
for aa in amino_acid2:
    how *= codon.count(aa)
print(how)