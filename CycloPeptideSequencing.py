__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail'

# Please take a look at my explantion of this problem
# at: https://sites.google.com/site/aliyyousuf/genome-sequencing-bioinformatics-ii/cyclo-peptide-sequencing



spectrum = []
file = open('peptide.txt','r')
for line in file:
    spectrum += line.rstrip().split()
spectrum = [int(x) for x in spectrum]



from TheoreticalSpectrum import integer_mass, total_mass
amino_acid = integer_mass()

def single_amino(spectrum):
    amino_table = integer_mass()
    match_AA = []
    for mas in spectrum:
        for aa, mass in amino_table.items():
            if mas == mass:
                match_AA += [aa]
    return list(set(match_AA))


def branching(peptide):
    branch = []
    amino_table = integer_mass()
    for AA in peptide:
        for A in amino_table.keys():
            branch += [AA+A]
    return branch




def check_consistency(peptide, spectrum):
    def linear_spectrum(peptide):
	     out_spectrum = [0]

	     for i in range(0, len(peptide)):
		     for j in range(i, len(peptide)):
			     subpep = peptide[i:j+1]
			     out_spectrum.append(total_mass(subpep))
	     return sorted(out_spectrum)
    peptide = linear_spectrum(peptide)
    import collections
    c_counter = collections.Counter(peptide)
    t_counter = collections.Counter(spectrum)

    for mass in c_counter:
        if mass not in t_counter:
            return False
        if c_counter[mass] > t_counter[mass]:
            return False
    return True





def cyclic_spectra(peptide):
    out_spectrum = [0, total_mass(peptide)]
    peptide_2 = peptide + peptide
    for k in range(1, len(peptide)):
        for n in range(len(peptide)):
            subpep = peptide_2[n:n+k]
            out_spectrum.append(total_mass(subpep))
    return sorted(out_spectrum)



def output_format(pep):
	masses = []
	for amino_acidS in pep:
		masses.append(amino_acid[amino_acidS])
	return '-'.join(map(str,masses))





candidates = single_amino(spectrum)
while candidates:
    candidates = branching(candidates)
    winners = []
    new_candidates = []
    for peptide in candidates:
        if cyclic_spectra(peptide) == spectrum:
            winners.append(peptide)
        elif check_consistency(peptide,spectrum):
            new_candidates.append(peptide)
    candidates = new_candidates


out_put = []
for pep in winners:
    out_put += [output_format(pep)]
#for i in (list(set(out_put))):
    #print(i,end = ' ')






