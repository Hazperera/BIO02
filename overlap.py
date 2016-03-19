__auther__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'

#  Input: A collection Patterns of k-mers.
# Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the edges in any order.)

def overlap(L):
    D = {}
    LL = []
    for i in L:
        D[i] = [i[0:len(i)-1]] + [i[1:len(i)]]
    #return D
    for i in L:
        for k, v in D.items():
            if D[i][0] == v[1]:
                LL += [str((k+' -> ' +i))]

    return [i.split() for i in LL]
#fi = open('overlap.txt','r')
#L2 = []
#for line in fi:
    #L2 += [line.rstrip()]
#st = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT']
#ss = overlap(L2)
#fo = open('overlap_output.txt','w')
#for i in ss:
    #fo.write((' '.join(i) + '\n'))
