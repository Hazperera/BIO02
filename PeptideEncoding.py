__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide. For example, the DNA string GAAACT is transcribed into GAAACU and translated into ET. The reverse complement of this DNA string, AGTTTC, is transcribed into AGUUUC and translated into SF. Thus, GAAACT encodes both ET and SF.”

# Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
#     Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
#     Output: All substrings of Text encoding Peptide (if any such substrings exist).



def dna_codon():                                     # Amino Acids relevant to DNA codes
    D = {}
    L = []
    file = open('dna_codon.txt','r')
    L = []
    for line in file:
        L += [line.rstrip().split()]
    for i in L:

            D[i[0]] = i[1]
    return D

def dna2prot(string):
    D = dna_codon()
    trans_string = ''
    for ind in range(0,len(string),3):
        #if not D[string[ind:3+ind]]:
            #break
        #else:
            trans_string += D[string[ind:3+ind]]
    return trans_string

def reverse_com(dna):
    complement_strand = ''
    D = {'A':'T','T':'A','C':'G','G':'C'}
    for i in dna:
        complement_strand += D[i]

    return complement_strand[::-1]

file = open('pept_encode.txt','r')
file = file.readlines()
dna = file[0].rstrip()
peptide = file[1].rstrip()

#dna = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'

#peptide = 'MA'

dna_parts = []

for part in range(0,len(dna)-3*len(peptide)+1):
    dna_parts =dna[part:len(peptide)*3+part]
    dna_trans = dna2prot(dna_parts)
    dna_part_rev = reverse_com(dna_parts)
    dna_trans_rev = dna2prot(dna_part_rev)

    if dna_trans == peptide or dna_trans_rev == peptide:
        print(dna_parts)
