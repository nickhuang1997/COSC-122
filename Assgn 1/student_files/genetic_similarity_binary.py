"""
File: genetic_similarity_binary.py
Author: Nicholas Huang

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use a binary search
"""


from classes import GeneList
## Uncomment the following line to be able to make your own testing Genes
# from classes import Gene, Genome




def genetic_similarity_binary(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer. The GeneList is of all genes that are common
        between first_genome and second_genome, while the integer is
        how many comparisons it took to find all the similar genes.
        Hint: it might pay to define a helper function.
    """


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
                break
                
                
    return Common_genes, count

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x
            
def alphabetical_order(stringA, stringB):
    """sees if stringA is before or after stringB alphabetically"""
    
    