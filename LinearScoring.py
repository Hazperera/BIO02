__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


from TheoreticalSpectrum import total_mass, integer_mass


def linear_spectrum(peptide):
	out_spectrum = [0]

	for i in range(0, len(peptide)):
		for j in range(i, len(peptide)):
			subpep = peptide[i:j+1]
			out_spectrum.append(total_mass(subpep))
	return sorted(out_spectrum)

def data_parser(filename):
    spectrum = []
    L = []
    file = open(filename,'r')
    L = file.readlines()

    peptide = L[0].rstrip()
    for item in L[1:]:
	    spectrum += item.rstrip().split()
    ex_spectrum = [int(x) for x in spectrum]
    return peptide, ex_spectrum

#peptide, ex_spectrum = data_parser('l_peptide.txt')


def linear_score(peptide,ex_spectrum):

	th_spectrum = linear_spectrum(peptide)
	count = 0
	for i in ex_spectrum:
		if i in th_spectrum:
			count += 1
			th_spectrum.remove(i)
	return count

#print(linear_score(peptide,ex_spectrum))
