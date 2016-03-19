__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



def integer_mass():
    D = {}
    file = open('integer_mass_table.txt','r')
    L = []
    for line in file.readlines():
        L = line.rstrip().split()
        D[L[0]] = int(L[1])
    return D
mass_table = integer_mass()

def sub_peptide(peptide):

    cyclic_peptide = peptide * 2
    sub_peptide = []

    for i in range(1,len(peptide)):
        for k in range(len(peptide)):
            sub_peptide += [cyclic_peptide[k:k+i]]
    return sub_peptide


def total_mass(sub_peptide):
    mass_table = integer_mass()
    total_mass = 0
    for i in sub_peptide:
        total_mass += mass_table[i]
    return total_mass


def theoretical_spec(peptide):
    #mass_table = integer_mass()
    sub_pept = sub_peptide(peptide)
    sub_spectrum = [0,total_mass(peptide)]
    for pep in sub_pept:
        sub_spectrum.extend([total_mass(pep)])
    return sorted(sub_spectrum)


#out = theoretical_spec('IPSWSQHQAKCEHS')
#print(' '.join(map(str,out)))
