__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


from TheoreticalSpectrum import integer_mass, total_mass
from Trim import trim
from LinearScoring import linear_score
from Score import score

file = open('LBS.txt','r')
file = file.readlines()
N = int(file[0].rstrip()) - 450
spectrum = file[1].rstrip().split()
#print(spectrum)
spectrum = sorted([int(x) for x in spectrum])

amino_table = integer_mass()


def branching(peptide):
    branch = []
    #amino_table = integer_mass()
    for AA in peptide:
        for A in amino_table.keys():
            branch += [AA+A]
    return branch
def single_amino(spectrum):
    amino_table = integer_mass()
    match_AA = []
    for mas in spectrum:
        for aa, mass in amino_table.items():
            if mas == mass:
                match_AA += [aa]
    return list(set(match_AA))
#N = 10
#spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]

#print(single_amino(spectrum))
candidates = single_amino(spectrum)

#winner = ''

#candidates = amino_table.keys()
winner = ''
winner_score = 0
while candidates:
	candidates = branching(candidates)
	new_candidates = []
	for candidate in candidates:
		c_mass = total_mass(candidate)
		t_mass = spectrum[-1]

		if c_mass == t_mass:
			new_candidates.append(candidate)
			c_score = score(candidate, spectrum)
			if c_score > winner_score:
				winner = candidate
				#winner_score = c_score
		elif c_mass < t_mass:
			new_candidates.append(candidate)
	candidates = trim(new_candidates, spectrum, N)

LW = []
for i in winner:
    LW += [str(amino_table[i])]
print('-'.join(LW))



