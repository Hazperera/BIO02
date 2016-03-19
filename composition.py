__author__ = 'Mohammad Yousuf Ali'

#file = open('composition.txt','r')
#file = file.readlines()
#K = int(file[0].rstrip())
#S = file[1].rstrip()


def composition(k,s):
    L = []
    for i in range(len(s)-k+1):
        L += [s[i:i+k] ]
    return L
#final_out = composition(K,S)
#out_file1 = open('out_composition.txt','w')
#for i in final_out:
    #out_file1.write(i +'\n')
