"""
File: genetic_similarity_sequential.py
Author: Nicholas Huang

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use the naive sequential approach.
"""

'TestData/test_data-2-1.txt'
from classes import GeneList

## Uncomment the following line to be able to make your own testing Genes
from classes import Genome, Gene


def genetic_similarity_sequential(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer. The GeneList is of all genes that are common
        between first_genome and second_genome, while the integer is how many
        comparisons it took to find all the similar genes.
    """
#    filename = 'TestData/test_data-2-1.txt'
#    GA, GB, GC = Genome_slicer(filename)
    
    GA_list = Genome_to_GeneList(first_genome)
    GB_list = Genome_to_GeneList(second_genome)
    
    return comparisons(GA_list, GB_list)



def Genome_slicer(filename):
    """Calls the read_test_data function to output slices genomes
    """
    import utilities
    genome_a, genome_b, commone_genes = utilities.read_test_data(filename)
    return genome_a , genome_b, commone_genes



def Genome_to_GeneList(genome_a):
    """Takes each sequence from each genomes and puts it into GeneList"""
    
    GL = GeneList()
    for i in range(len(genome_a)):
        GL.append(genome_a[i])                 #puts item genome_a[i] into GeneList
    return GL


def comparisons(genome_a , genome_b):
    """compares genomes the first genome to the second
    """
#    genes_only = len(genome_a) - genome_a.count(' ')
    count = 0
    GL1 = Genome_to_GeneList(genome_a)
    GL2 = Genome_to_GeneList(genome_b)    
    Common_genes = GeneList()               #empty list for common genes
    
    for i in range(len(GL1)):
        for p in range(len(GL2)):    
            count += 1
           
            if GL1[i] == GL2[p]:            #if the genes are the same
                Common_genes.append(GL1[i])
    
    return Common_genes, count
                          
"""
Helper Functions
----------------
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

a) make genomes into Gene items: g = Gene(genome_a)
b) create GeneList:              Gene_List1 = GeneList()
c) append Genes to the GL        Gene_List1.append(g)
    
use this to iterate



1. break genes up into segments of 16  (extract strings of length 16)
  a)put the extracted strings into a list or bin

for range(len(genome)%16)   'loops the n amount of times there is a full genome
 - use recursion and cut off the first 

2. add common genes to the back of a list/queue

3. 

"""