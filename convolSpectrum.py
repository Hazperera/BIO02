__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



file = open('convol.txt','r')
spectrum = []
for line in file:
    spectrum += line.rstrip().split()
spectrum = [int(x) for x in spectrum]
spectrum = sorted(spectrum)


def convolution(spectrum):
    L = []
    for i in spectrum:
         for k in spectrum:
             if i -k > 0:
                 L += [i-k]
    return L
#print(convolution(spectrum))