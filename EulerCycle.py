__author__ = 'Mohammad Yousuf Ali,fb.com/aliyyousuf,aliyyousuf@gmail.com'

# Solve the Eulerian Cycle Problem (Randomized approach): Just Randomly pick the starting node and pick the
# node when a node contains multiple edges.

# Input: The adjacency list of an Eulerian directed graph.
# Output: An Eulerian cycle in this graph.

# Sample Input:
#     0 -> 3
#     1 -> 0
#     2 -> 1,6
#     3 -> 2
#     4 -> 2
#     5 -> 4
#     6 -> 5,8
#     7 -> 9
#     8 -> 7
#     9 -> 6

#Sample Output:

#     6->8->7->9->6->5->4->2->1->0->3->2->6

#file = open('e_cycle.txt','r')
#D_test = {}
#for line in file:
    #D_test[int((line.rstrip().split('->'))[0])] = line.rstrip().split('->')[1:]

#for k,v in D_test.items():
    #D_test[k] = [i.split(',') for i in D_test[k] ]
#D_test_case = {x:[int(z) for z in y[0]] for x,y in D_test.items()}

def  cycle(D):
     import random
     ran_k = random.choice(list(D.keys()))   # Randomly pick the starting node from all nodes.
     tmp_stk = []
     tmp_stk += [ran_k]
     flag = True
     while flag:
           try:
               if len(D[ran_k]) > 1:
                   ran_k2 = random.choice(D[ran_k])    # When a node contains the multiple edges.
                   tmp_stk += [ran_k2]
                   del D[ran_k][D[ran_k].index(ran_k2)]
                   ran_k = tmp_stk[-1]
               else:
                   tmp_stk += D[ran_k]
                   del D[ran_k]
                   ran_k = tmp_stk[-1]
           except KeyError:
               flag = False
               return D,tmp_stk

def cycle2(D,k):
     import random
     tmp_stk = []
     ran_k = k
     flag = True
     while flag:
           try:
               if len(D[ran_k]) > 1:
                   ran_k2 = random.choice(D[ran_k])
                   tmp_stk += [ran_k2]
                   del D[ran_k][D[ran_k].index(ran_k2)]
                   ran_k = tmp_stk[-1]
               else:
                   tmp_stk += D[ran_k]
                   del D[ran_k]
                   ran_k = tmp_stk[-1]
           except KeyError:
               flag = False
               return D,tmp_stk
def euler_circle(D):
    r_D,tmp_r = cycle(D)
    tmp_r2 = []
    if len(r_D):
       r_node = list(r_D.keys())
       while len(r_D):

            for k in tmp_r:
                if k in r_D.keys():

                   index_n = tmp_r.index(k)
                   r_D,tmp_r1 = cycle2(r_D,k)
                   tmp_r = tmp_r[:index_n+1] + tmp_r1+tmp_r[index_n+1:]


       final_output = tmp_r
       #final_output = [str(i) for i in tmp_r]
       #print('->'.join(final_output))
       return final_output
       #return ('->'.join(final_output))
    else:
       final_output = tmp_r
       #final_output = [str(i) for i in tmp_r]
       #print('->'.join(final_output))
       return final_output
       #return ('->'.join(final_output))

#final = (euler_circle(D_test_case))
#final = [str(x) for x in final]
#print('->'.join(final))





