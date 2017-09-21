"""
File: linear_probing_gene_hash_table.py
Author: your name should probably go here

A module to find the genetic similarity between two genomes.
To find how many genes are in common, we use the naive sequential approach.
"""


from classes import Genome, BaseGeneHashTable
## Uncomment the following line to be able to make your own testing Genes
from classes import Gene


class LinearProbingGeneHashTable(BaseGeneHashTable):
    """ A Chaining Gene Hash Table stores Gene objects for efficient
        matching of genes to diseases, meaning faster diagnosis for
        patients. This particular variation makes use of lists to
        handle gene hash collisions.
    """

    def __init__(self, table_size):
        """ Create a hash table of the correct size, reset counters.
        """
        super().__init__(table_size)
        self.hash_table = [None] * table_size
        self.n_slots = table_size
        self.n_items = 0
        self.comparisons = 0
    # ---start student section---
        
    def __str__(self):
        results = []
        for i, row in enumerate(self.hash_table):
            results.append("  {}: {}".format(i, str(row)))
        results = [self.__class__.__name__ + "["] + results + ["]"]
#        results += 'Number of comparisons \n '.format(self.comparisons)
        
        return "\n".join(results)

#    @abstractmethod
    def __getitem__(self, gene):
        
        i = 0
        found = False
        while found == False:
            self.comparisons += 1
            if self.hash_table[i][0] == gene:   #works when its the right Gene, error if wrong
                found = True
                return self.hash_table[i][1]
            
            if i == self.n_slots:
                break
                return None
            i += 1
                
#    @abstractmethod
    def insert(self, gene, disease):
        """inserts both the gene and disease name into a slot"""
        index = hash(gene) % self.n_slots
        print(index)

        if self.hash_table[index] == None:                  #cant get this to equal None
            self.hash_table[index] = (gene,disease)
            self.n_items += 1
            
        else:   #if there is an item in the slot 
            while self.hash_table[index] != None:
                index = (index + 1)%self.n_slots
                self.comparisons += 1
                if self.n_items == self.n_slots:
                    raise IndexError ("Hash table is full")
                    break
                self.n_items += 1
            self.hash_table[index] = (gene,disease)            
         
