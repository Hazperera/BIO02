__author__ = 'Mohammad Yousuf Ali, fb.com/aliyyousuf,aliyyousuf@gmail.com'

# CODE CHALLENGE: Solve the String Reconstruction from Read-Pairs Problem.
#     Input: Integers k and d followed by a collection of paired k-mers PairedReads.
#     Output: A string Text with (k, d)-mer composition equal to PairedReads.


def data_parser(file_name):

    '''
    :param file_name: file name that contains the data, use quote like 'data.txt'
    :return: graph to be used by euler path, K and D both are integer
    '''

    file = open(file_name,'r')
    file_line = []
    for line in file:
        file_line += [line.rstrip()]

    K_D = file_line[0].split()
    file_line = file_line[1:]
    K,D = int(K_D[0]),int(K_D[1])        # taking the value of K and D
    l = []
    graph = {}
    for item in file_line:
        l += [item.split('|')]

    for i in l:
        graph[(i[0][:(len(i[0])-1)],i[1][:len(i[1])-1])] = [(i[0][1:],i[1][1:])]  #Keys = Suffix and values = Prefixes
    return graph,K,D

from stringReconstructionEuPath import euler_path
graph,k,d = (data_parser('str_recon_rp.txt'))


def recon_str_pair(graph):
    '''
    :param graph: Constructed graphs from data_parser function.
    the basic graph struture is: {(prefix1,prefix2) = [(suffix1,suffix2)]}
    :return:  string or reads.
    '''

    euler_pth = euler_path(graph)
    prefix = ''
    suffix = ''
    for i in euler_pth[:-1]:
        prefix += i[0][0]                # Adding the first letter from each except last from suffix
        suffix += i[1][0]                # Adding the first letter from each except last from prefix
    prefix += euler_pth[-1][0]           # Adding the whole of last prefix.
    suffix += euler_pth[-1][1]           # Adding the whole of last suffix
    string = prefix[:k+d]+suffix         # Rebuilding the string.
    return string

print(recon_str_pair(graph))