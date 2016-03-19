__author__ = 'Mohammad Yousuf Ali,aliyyousuf@gmail.com,fb.com/aliyyousuf'
# You now have a method to assemble a genome, since the String Reconstruction
# Problem reduces to finding an Eulerian path in the de Bruijn graph generated
# from reads.

#CODE CHALLENGE: Solve the String Reconstruction Problem.
#     Input: An integer k followed by a list of k-mers Patterns.
#     Output: A string Text with k-mer composition equal to Patterns.
#     (If multiple answers exist, you may
#     return any one.)

def out_degree(k,D):
    return len(D[k])
def in_degree(k,D):
    count = 0
    for i in D.values():
        if len(i) == 1:
            if i[0] == k:
                count +=1
        else:
            for ii in i:
                if ii == k:
                    count +=1
                else:
                    pass
    return count

def degree(D):
    degree_grap = {}
    for k,v in D.items():
        degree_grap[k] = out_degree(k,D) + in_degree(k,D)
    return degree_grap

def tot_odd_degree(D):
    degree_D = degree(D)
    L = []
    for k,v in degree_D.items():
        if v%2 != 0:
           L += [k]
    return L
#print(tot_odd_degree(D))
#D_val = [item for sublist in list(D.values()) for item in sublist]

def unbal_deg(D):
    D_val = [item for sublist in list(D.values()) for item in sublist]
    L = []
    for i in D_val:
        if i not in D.keys():
           L += [i]
    return L
#print(unbal_deg(D))

def path(D):

     L,N = tot_odd_degree(D)
     ran_k = L[0]
     tmp_stk = []
     tmp_stk += [ran_k]
     flag = True
     while flag:
           try:
               if len(D[ran_k]) > 1:
                   ran_k2 = D[ran_k][0]
                   tmp_stk += [ran_k2]
                   del D[ran_k2][0]
                   ran_k = tmp_stk[-1]
               else:
                   tmp_stk += D[ran_k]
                   del D[ran_k]
                   ran_k = tmp_stk[-1]
           except KeyError:
               flag = False
               return D,tmp_stk

def euler_path(D):

    odd_d1 = tot_odd_degree(D)
    odd_d2 = unbal_deg(D)
    if len(odd_d2):
        D[odd_d2[0]] = [odd_d1[0]]
    else:
        D[odd_d1[0]] = D[odd_d1[0]] + [odd_d1[1]]

    from EulerCycle import euler_circle

    circle = euler_circle(D)
    if len(odd_d2) and len(odd_d2):
        Fil = ((circle[circle.index(odd_d2[0])+1:])+circle[1:circle.index(odd_d2[0])+1])
        final_output = [str(i) for i in Fil]
        return Fil
    else:
        Fil = ((circle[circle.index(odd_d1[0])+1:])+circle[1:circle.index(odd_d1[0])+1])
        final_output = [str(i) for i in Fil]

        return Fil
from debruijinKmer import debruijin_k

file = open('str_recon.txt','r')      # Get the test data from file
k_L = []
for line in file:
    k_L += [line.rstrip()]
k_L = k_L[1:]                   # Discard the first line from text line, it contains an int

d_Br = (debruijin_k(k_L))       # Makes a De Bruijin graph
d_Br = dict(d_Br)               # return a default dict, convert it into normal dict

E_Db = (euler_path(d_Br))       # Run the Euler Path over De Bruijin Graph

from genomepath import genome_path   # Import the Genome_Path function
#print(genome_path(E_Db))             # Build the genome path from Euler Path.