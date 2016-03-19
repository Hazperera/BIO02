__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'


#graph = {1:[2],2:[3],3:[4,5],6:[7],7:[6]}

def data_parser():
    file = open('dd2.txt','r')
    D = {}
    for line in file:
        D[int((line.rstrip().split('->'))[0])] = line.rstrip().split('->')[1:]
    for k,v in D.items():
        D[k] = [i.split(',') for i in D[k] ]
    D = {x:[int(z) for z in y[0]] for x,y in D.items()}
    return D

graph = data_parser()

def all_node(graph):
    import itertools
    nodes = []
    for k,v in graph.items():
        if len(graph[k])>1:
            tmp_k = list(itertools.repeat(k,len(v)))
            nodes.extend(tmp_k)
        else:
            nodes += [k]
    return nodes
#print(all_node(graph))



def starting_node(graph):
    import itertools
    D = {}
    all_keys = list(graph.keys())
    all_val = list(itertools.chain.from_iterable(list(graph.values())))

    for node in graph:
        if node not in all_val and len(graph[node]) == 1:
            D[node] = True
        elif node in all_val and len(graph[node])>1:
            D[node] = True
        elif node in all_keys and all_val.count(node)>1:
            D[node] = True
        else:
            D[node] = False
    return D

#print(starting_node(graph))

def ending_node(graph):
    import itertools
    D = {}
    all_keys = list(graph.keys())
    all_val = list(itertools.chain.from_iterable(list(graph.values())))
    for node in all_val:
        if node not in all_keys:
            D[node] = True
        elif node in all_keys and all_val.count(node)>1:
            D[node] = True
        elif node in all_keys and len(graph[node])>1:
            D[node] = True
        else:
            D[node] = False
    return D

def isolate_cycle(graph):
    path = []

    flag = True
    node = list(graph.keys())[0]

    while flag:
        tmp_path = []
        try:
            if len(graph[node])>1:
                tmp_path = [node,graph[node][0]]
                del graph[node][0]
                while tmp_path[-1] in list(graph.keys()):
                    tmp_path.extend(graph[tmp_path[-1]])
                    del graph[tmp_path[-2]]
                path += [tmp_path]
            else:
                tmp_path = [node,graph[node][0]]
                del graph[node]
                while tmp_path[-1] in list(graph.keys()):
                    tmp_path.extend(graph[tmp_path[-1]])
                    del graph[tmp_path[-2]]
                path += [tmp_path]
        except KeyError:
            flag = False
    return path




def non_iso(graph):

   D1 = starting_node(graph)
   D2 = ending_node(graph)

   path = []
   node2 = all_node(graph)

   for key in node2:
        tmp_path = []
        if D1[key]:
            #node2.remove(key)
            try:
            #graph[key]
                if len(graph[key]) > 1:
                    tmp_path = [key,graph[key][0]]
                    del graph[key][0]
                    while not D2[tmp_path[-1]]:
                        tmp_path.extend(graph[tmp_path[-1]])
                        del graph[tmp_path[-2]]
                    path += [tmp_path]
                else:
                    tmp_path = [key,graph[key][0]]
                    del graph[key]
                    while not D2[tmp_path[-1]]:
                        tmp_path.extend(graph[tmp_path[-1]])
                        del graph[tmp_path[-2]]
                    path += [tmp_path]

            except KeyError:
                pass
   return path




def final(graph):
    p,g = non_iso(graph)
    fg = []
    while g:
        fg += isolate_cycle(g)
    return fg+p






