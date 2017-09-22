"""
File: chaining_gene_hash_table.py
Author: Nicholas Huang

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use the naive sequential approach.
"""


from classes import GeneLinkedList, GeneLink, BaseGeneHashTable
## Uncomment the following line to be able to make your own testing Genes
from classes import Gene


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
        
        self.n_slots = table_size
        
        self.comparisons = 0
        self.hashes = 0
        
        
     
    # ---start student section---
        
    def __str__(self):
        results = []
        for i, row in enumerate(self.hash_table):
            results.append("  {}: {}".format(i, str(row)))
        results = [self.__class__.__name__ + "["] + results + ["]"]
        
        return "\n".join(results)

    def __getitem__(self, gene):
        """finds the gene in the hash table"""
        self.hashes += 1
        index = hash(gene) % self.n_slots 
        currenthead = self.hash_table[index].head
        if currenthead != None:
            while currenthead.next_node != None:
                self.comparisons += 1
                if currenthead.data[0] == gene:
                    return currenthead.data[1]
                currenthead = currenthead.next_node
            self.comparisons += 1
            if currenthead.data[0] == gene:
                return currenthead.data[1]
        return None
            
        
    def insert(self, gene, disease):
        """inserts both the gene and disease name into a slot"""
        self.hashes += 1
        index = hash(gene) % self.n_slots        
        
        temp = GeneLink((gene,disease))
        temp.next_node = self.hash_table[index].head
        self.hash_table[index].head = temp
        
