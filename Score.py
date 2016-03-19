__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


from TheoreticalSpectrum import integer_mass, total_mass


def cyclic_spectra(peptide):
    out_spectrum = [0, total_mass(peptide)]
    peptide_2 = peptide + peptide
    for k in range(1, len(peptide)):
        for n in range(len(peptide)):
            subpep = peptide_2[n:n+k]
            out_spectrum.append(total_mass(subpep))
    return sorted(out_spectrum)

def score(peptide,spectrum):

    th_spectrum = cyclic_spectra(peptide)
    count = 0

    for i in spectrum:
        if i in th_spectrum:
            count += 1
            th_spectrum.remove(i)
    return count

#peptide = 'NQEL'
#spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
#print(score(peptide,spectrum))