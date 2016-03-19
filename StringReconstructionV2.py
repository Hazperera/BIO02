__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


file = open('str_recon.txt','r')
k_L = []
for line in file:
    k_L += [line.rstrip()]
k_L = k_L[1:]
from stringReconstructionEuPath import euler_path
from debruijinKmer import debruijin_k
from genomepath import genome_path

DB = debruijin_k(k_L)
EP = euler_path(DB)
print(genome_path(EP))


