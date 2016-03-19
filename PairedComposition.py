__author__ = ('Mohammad Yousuf Ali,fb.com/aliyyousuf,aliyyousuf@gmail.com')


#                From composition to paired composition

#  Given a string Text, a (k,d)-mer is a pair of k-mers in Text separated by distance d.
#  We use the notation (Pattern1|Pattern2) to refer to a (k,d)-mer whose k-mers are Pattern1
#  and Pattern2. For example, (ATG|GGG) is a (3,4)-mer in TAATGCCATGGGATGTT. The (k,d)-mer
#  composition of Text, denoted PairedCompositionk,d(Text), is the collection of all
#  (k,d)- mers in Text (including repeated (k,d)-mers). For example, here is

# Input:   PairedComposition 3,1(TAATGCCATGGGATGTT):
# output:  [(AAT|CCA) (ATG|CAT) (ATG|GAT) (CAT|GGA) (CCA|GGG) (GCC|TGG) (GGA|GTT) (GGG|TGT) (TAA|GCC) (TGC|ATG) (TGG|ATG)]

T = 'TAATGCCATGGGATGTT'

def pair_composition(T,k,d):

   first_text = T[:len(T)-(d+k)]              #Split text from first to kMer length + distance
   second_text = T[k+d:]                      #Split text from length+distance  to end
   first_pair = []
   second_pair = []
   for i in range(len(first_text)-k+1):       # Make all kmers from first text
       first_pair += [first_text[i:i+k]]
   for i in range(len(second_text)-k+1):      # Make all kMers from second text.
       second_pair += [second_text[i:i+k]]
   final_pair = []
   for chr1, chr2 in zip(first_pair,second_pair):   # Now make the pairs
       final_pair += [(chr1+' | '+chr2)]
   return sorted(final_pair)

print(pair_composition(T,3,1))
