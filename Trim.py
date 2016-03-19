__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



from LinearScoring import linear_score

def data_trim(filename):

    file = open(filename,'r')
    file = file.readlines()
    L = []
    for line in file:
        L += [line.rstrip().split()]
    col_peptide = L[0]
    N = int(L[-1][0])
    ex_spectrum = [int(x) for x in L[1]]
    return col_peptide, ex_spectrum, N




def trim(col_peptide2,ex_spectrum2,N2):
    l_score2 = []

    for i in col_peptide2:
        l_score2 += [(i,linear_score(i,ex_spectrum2))]

    l_score2 = sorted(l_score2, key = lambda x: x[1], reverse = True)


    final_out = []

    for i in l_score2[:N2]:

       final_out += [i[0]]
    if len(final_out) <= N2:
        return final_out
    else:
        for kk in range(0,len(l_score2) - N2):
          if l_score2[N2-1+kk][1] == l_score2[N2+kk][1]:
              final_out.append(l_score2[N2+kk][0])
          else:
              break
    return final_out

#final_out = trim(col_peptide2,ex_spectrum2,N2)
#for i in final_out:
    #print(i, end = ' ')

file = open('specon.txt','r')
file = file.readlines()
#print(file)
M = int(file[0].rstrip())
N = int(file[1].rstrip())
spectrum = file[2].rstrip()
spectrum = sorted([ int(x) for x in spectrum.split()])











