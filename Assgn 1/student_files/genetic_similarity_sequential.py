"""
File: genetic_similarity_sequential.py
Author: Nicholas Huang

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use the naive sequential approach.
"""
from classes import GeneList
from classes import Genome, Gene


def genetic_similarity_sequential(first_genome, second_genome):
    """ This function takes two Genome objects, and returns a GeneList
        and an integer. The GeneList is of all genes that are common
        between first_genome and second_genome, while the integer is how many
        comparisons it took to find all the similar genes.
    """
#    filename = 'TestData/test_data-2-1.txt'
#    GA, GB, GC = Genome_slicer(filename)
    
    genome_a_list = genome_to_genelist(first_genome)
    genome_b_list = genome_to_genelist(second_genome)
    
    return comparisons(genome_a_list, genome_b_list)


def genome_to_genelist(genome_a):
    """Takes each sequence from each genomes and puts it into GeneList"""
    
    initialgenelist = GeneList()
    for i in range(len(genome_a)):
        initialgenelist.append(genome_a[i])                 #puts item genome_a[i] into GeneList
    return initialgenelist


def comparisons(genome_a, genome_b):
    """compares genomes the first genome to the second
    """
#    genes_only = len(genome_a) - genome_a.count(' ')
    count = 0
    genelistone = genome_to_genelist(genome_a)
    genelisttwo = genome_to_genelist(genome_b)    
    common_genes = GeneList()               #empty list for common genes
    
    for i in range(len(genelistone)):
        for secondgenome in range(len(genelisttwo)):    
            count += 1
           
            if genelistone[i] == genelisttwo[secondgenome]:            #if the genes are the same
                common_genes.append(genelistone[i])
                break               
    return common_genes, count
