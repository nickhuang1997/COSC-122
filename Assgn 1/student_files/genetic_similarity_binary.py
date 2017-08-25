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
    GA_list = Genome_to_GeneList(first_genome)
    GB_list = Genome_to_GeneList(second_genome)
    
    return binary_search(GA_list, GB_list)

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


def binary_search(genome_a, genome_b):
    """uses a binary search to find common genomes genome_a and genome_b
    genome_b must be in lexicographic order
    """
    GL1 = Genome_to_GeneList(genome_a)
    GL2 = Genome_to_GeneList(genome_b) 
    count = 0
    common_genes = GeneList()
    
    for i in range(len(GL1)):
        find_this_genome = GL1[i]
#        print(find_this_genome)
        lower = 0
        upper = len(GL2)

        while lower <= upper:               
            midpoint = (upper + lower)//2               
            count += 1
#            print("mid is "+str(midpoint))
            
            if find_this_genome == GL2[midpoint]:
                common_genes.append(find_this_genome)
#                print('Found it! '+ str(GL2[midpoint]))
                break
            
            elif find_this_genome < GL2[midpoint]:
                if upper == midpoint:
                    break
                upper = midpoint
                
            elif find_this_genome > GL2[midpoint]: 
                if lower == midpoint:
                    break
                lower = midpoint
                
    print(count)
    print(common_genes)
    return common_genes, count
    

a,b,c = Genome_slicer('TestData/test_data-1000-0.txt')
genetic_similarity_binary(a,b)

    