__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



from TheoreticalSpectrum import integer_mass, total_mass

mass_table = integer_mass()


def cyclic_spectra(peptide):
    out_spectrum = [0, total_mass(peptide)]
    peptide_2 = peptide + peptide
    for k in range(1, len(peptide)):
        for n in range(len(peptide)):
            subpep = peptide_2[n:n+k]
            out_spectrum.append(total_mass(subpep))
    return sorted(out_spectrum)


spectrum = []
L = []
file = open('score.txt','r')
L = file.readlines()

peptide = L[0].rstrip()


for item in L[1:]:
    spectrum += item.rstrip().split()
ex_spectrum = [int(x) for x in spectrum]
th_spectrum = cyclic_spectra(peptide)       # For cyclic mass spectrum

count = 0
for i in ex_spectrum:
    if i in th_spectrum:
            count += 1
            th_spectrum.remove(i)
print(count)


