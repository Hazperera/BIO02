
__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



from convolSpectrum import convolution
from TheoreticalSpectrum import integer_mass, total_mass
from Trim import trim
from Score import score



file = open('specon.txt','r')
file = file.readlines()
M = int(file[0].rstrip())
N = int(file[1].rstrip()) - 300
spectrum = file[2].rstrip()
spectrum = sorted([ int(x) for x in spectrum.split()])
convol = (convolution(spectrum))

filtered = [c for c in convol if c >= 57 and c <= 200]






def most_freq(convol,M):
    final_out = []

    if len(convol) <= M:
        return convol
    else:
        final_out = convol[:M]
        for kk in range(0,len(convol) - M):
          if convol[M-1+kk] == convol[M+kk]:
              final_out.append(convol[M+kk])
          else:
             break
        return final_out


most_freq_M = most_freq(convol,M)


amino_table = integer_mass()


def branching(peptide):
    branch = []
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

candidates = single_amino(most_freq_M)

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
		elif c_mass < t_mass:
			new_candidates.append(candidate)
	candidates = trim(new_candidates, spectrum, N)

LW = []
for i in winner:
    LW += [str(amino_table[i])]
print(' '.join(LW))
