__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# How many sub peptides does a cyclic peptide of length n have?

def cyclic_peptide(n):
    return n * (n-1)

print(cyclic_peptide(31315))