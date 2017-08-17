"""
File: genetic_similarity_sequential.py
Author: Nicholas Huang

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use the naive sequential approach.
"""

'TestData/test_data-2-1.txt'
from classes import GeneList

## Uncomment the following line to be able to make your own testing Genes
# from classes import Genome, Gene


def genetic_similarity_sequential(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer. The GeneList is of all genes that are common
        between first_genome and second_genome, while the integer is how many
        comparisons it took to find all the similar genes.
    """


def Genome_slicer(filename):
    """Calls the read_test_data function to output slices genomes
    """
    import utilities
    genome_a, genome_b, commone_genes = utilities.read_test_data(filename)
    return genome_a , genome_b, commone_genes

def comparisons(genome_a , genome_b):
    """compares genomes the first genome to the second
    """
    for range(len(str(genome_a)))
    
"""
Helper Functions
----------------

1. break genes up into segments of 16  (extract strings of length 16)
  a)put the extracted strings into a list or bin

for range(len(genome)%16)   'loops the n amount of times there is a full genome
 - use recursion and cut off the first 

2. add common genes to the back of a list/queue

3. 

"""