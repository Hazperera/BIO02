__author__ = 'Mohammad Yousuf Ali,fb.com/aliyyousuf,aliyyousuf@gmail.com'



# Solve the Eulerian Cycle Problem (Not Randomized approach)
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

file = open('dd.txt','r')                  # Obtaining data from the file and
D = {}                                     # Building the Graph
for line in file:
    D[int((line.rstrip().split('->'))[0])] = line.rstrip().split('->')[1:]

for k,v in D.items():
    D[k] = [i.split(',') for i in D[k] ]
D = {x:[int(z) for z in y[0]] for x,y in D.items()}

def  cycle(D):
     ran_k = list(D.keys())[0]            # Select the first node as starting node
     tmp_stk = []                         # Temporary stack to save edges
     tmp_stk += [ran_k]                   # Keep the first node in temporary stack
     flag = True
     while flag:
           try:
               if len(D[ran_k]) > 1:      # Check if any node has two or more edges.
                   ran_k2 = D[ran_k][0]   # Then take the first one.
                   tmp_stk += [ran_k2]    # Add the first edge into temporary stack
                   del D[ran_k][0]        # Delete the edge from Graph
                   ran_k = tmp_stk[-1]    # Select the last node to keep growing path
               else:                      # When a node has a edge.
                   tmp_stk += D[ran_k]
                   del D[ran_k]
                   ran_k = tmp_stk[-1]
           except KeyError:               # If the node doesn't exist in graph.
               flag = False
               return D,tmp_stk           # Return rest Graph and Temporary stack

def cycle2(D,k):                          # Start another cycle for rest Graph
     tmp_stk = []
     ran_k = k                            # k = node that still has two edges in Graph
     flag = True
     while flag:
           try:
               if len(D[ran_k]) > 1:
                   ran_k2 = D[ran_k][0]
                   tmp_stk += [ran_k2]
                   del D[ran_k][0]
                   ran_k = tmp_stk[-1]
               else:
                   tmp_stk += D[ran_k]
                   del D[ran_k]
                   ran_k = tmp_stk[-1]
           except KeyError:
               flag = False
               return D,tmp_stk

def euler_circle(D):                       # Now build the main function.
    r_D,tmp_r = cycle(D)                   # Obtain the first the Cycle.
    if len(r_D):                           # Check if the Graph is empty after first cycle.
       r_node = list(r_D.keys())           # Find all nodes after first cycle
       while len(r_D):                     # Run till the Graph is not empty.
            for k in tmp_r:                # Check which node still has the multiple edges.
                if k in r_D.keys():        # Check which node still has the multiple edges.
                   index_n = tmp_r.index(k)     # Keep the index of node of multiple edges
                   r_D,tmp_r1 = cycle2(r_D,k)
                   tmp_r = tmp_r[:index_n+1] + tmp_r1+tmp_r[index_n+1:] # re-add the path
       final_output = tmp_r
       final_output = [str(i) for i in tmp_r]
       return ('->'.join(final_output))
       #return final_output
    else:
       final_output = tmp_r
       final_output = [str(i) for i in tmp_r]
       return ('->'.join(final_output))
       #return final_output

print(euler_circle(D))





