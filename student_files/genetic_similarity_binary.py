"""
File: genetic_similarity_binary.py
Author: your name should probably go here

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
