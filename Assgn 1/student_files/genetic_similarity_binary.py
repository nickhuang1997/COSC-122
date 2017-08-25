"""
File: genetic_similarity_binary.py
Author: Nicholas Huang

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use a binary search
"""


from classes import GeneList
## Uncomment the following line to be able to make your own testing Genes
from classes import Gene, Genome




def genetic_similarity_binary(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer. The GeneList is of all genes that are common
        between first_genome and second_genome, while the integer is
        how many comparisons it took to find all the similar genes.
        Hint: it might pay to define a helper function.
    """
    ga_list = genome_to_genelist(first_genome)
    gb_list = genome_to_genelist(second_genome)
    
    return binary_search(ga_list, gb_list)

def genome_to_genelist(genome_a):
    """Takes each sequence from each genomes and puts it into GeneList"""
    
    initialgenelist = GeneList()
    for i in range(len(genome_a)):
        initialgenelist.append(genome_a[i])                 #puts item genome_a[i] into GeneList
    return initialgenelist

def binary_search(genome_a, genome_b):
    """uses a binary search to find common genomes genome_a and genome_b
    genome_b must be in lexicographic order
    """
    count = 0
    common_genes = GeneList()
    
    for i in range(len(genome_a)):
        find_this_genome = genome_a[i]
        lower = 0
        upper = len(genome_b) - 1

        while lower < upper:               
            midpoint = (upper + lower)//2                           
            
            count += 1
            if find_this_genome <= genome_b[midpoint]:
                upper = midpoint
            else:
                lower = midpoint + 1

        count += 1
        #print(midpoint)
        if find_this_genome == genome_b[upper]:
            #print(find_this_genome)
            common_genes.append(find_this_genome)

                    
    #print(count)
    #print(common_genes)
    return common_genes, count
    

#a,b,c = Genome_slicer('TestData/test_data-1000-250.txt')
#binary_search(a,b)
#genetic_similarity_binary(a,b)

