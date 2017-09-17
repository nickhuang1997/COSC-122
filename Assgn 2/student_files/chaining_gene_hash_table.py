"""
File: chaining_gene_hash_table.py
Author: your name should probably go here

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use the naive sequential approach.
"""


from classes import GeneLinkedList, GeneLink, BaseGeneHashTable
## Uncomment the following line to be able to make your own testing Genes
# from classes import Gene


class ChainingGeneHashTable(BaseGeneHashTable):
    """ A Chaining Gene Hash Table stores Gene objects for efficient
        matching of genes to diseases, meaning faster diagnosis for
        patients. This particular variation makes use of linked lists
        to handle gene hash collisions.
    """

    def __init__(self, table_size):
        """ Create a hash table of the correct size, reset counters.
            Be sure to use GeneLinkedList objects in your hash table.
        """
        super().__init__(table_size)
        self.hash_table = [GeneLinkedList() for _ in range(table_size)]

    # ---start student section---
    pass
    # ===end student section===
