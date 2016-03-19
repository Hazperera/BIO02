__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


D2 = {0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]}
def data_parser():
    file = open('e_path.txt','r')
    D = {}
    for line in file:
        D[int((line.rstrip().split('->'))[0])] = line.rstrip().split('->')[1:]
    for k,v in D.items():
        D[k] = [i.split(',') for i in D[k] ]
    D = {x:[int(z) for z in y[0]] for x,y in D.items()}
    return D
D = data_parser()
#D = {'TA': ['AC'], 'GC': ['CT'], 'AC': ['GC'], 'CT': ['TT', 'TT'], 'CC': ['AC'], 'TT': ['CC', 'TA']}

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
     import random
     L,N = tot_odd_degree(D)
     #ran_k = random.choice(L)
     #ran_k = 4
     ran_k = L[0]
     tmp_stk = []
     tmp_stk += [ran_k]
     #print(ran_k)
     flag = True
     while flag:
           try:
               if len(D[ran_k]) > 1:
                   #ran_k2 = random.choice(D[ran_k])
                   ran_k2 = D[ran_k][0]
                   tmp_stk += [ran_k2]
                   #del D[ran_k][D[ran_k].index(ran_k2)]
                   del D[ran_k2][0]
                   ran_k = tmp_stk[-1]
               else:
                   tmp_stk += D[ran_k]
                   del D[ran_k]
                   ran_k = tmp_stk[-1]
           except KeyError:
               flag = False
               return D,tmp_stk
#print(data_parser())
#print(tot_odd_degree(D))
#print(unbal_deg(D))
#print(D[685])

odd_d1 = tot_odd_degree(D)
print(odd_d1)
odd_d2 = unbal_deg(D)
#print(odd_d2)
#De = {}
if len(odd_d2):
    D[odd_d2[0]] = [odd_d1[0]]
else:
    #De[odd_d2[0]] = [odd_d1[0]]
    D[odd_d1[0]] = D[odd_d1[0]] + [odd_d1[1]]
#print(D[685])

from EulerCycle import euler_circle

circle = euler_circle(D)
if len(odd_d2) and len(odd_d2):
    Fil = ((circle[circle.index(odd_d2[0])+1:])+circle[1:circle.index(odd_d2[0])+1])
    final_output = [str(i) for i in Fil]
    print('->'.join(final_output))
else:
    Fil = ((circle[circle.index(odd_d1[0])+1:])+circle[1:circle.index(odd_d1[0])+1])
    final_output = [str(i) for i in Fil]
    print('->'.join(final_output))

