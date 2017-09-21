"""
File: chaining_gene_hash_table.py
Author: Nicholas Huang

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
        self.n_slots = table_size
        self.n_items = 0
        self.comparisons = 0
        self.hashes = 0
        
        self.head = None
        
     
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
        pass
    
#    @abstractmethod
    def insert(self, gene, disease):
        """inserts both the gene and disease name into a slot"""
        index = hash(gene) % self.n_slots
        
        self.comparisons += 1
        if self.hash_table[index] == None:                  #cant get this to equal None
            print('no other things here')
            self.hash_table[index] = GeneLink((gene,disease))
            print('just inserted it')
            
        else:   #if there is an item in the slot 
            temp = GeneLink((gene,disease))
            print(temp)
            print(temp.data)
            temp.next_node = self.hash_table[index]
            self.hash_table[index] = temp
            


#    def get(self, item):
#        """finds the item in the hash table"""
#        
#        startslot = self._hash(item)
#        
#        data = None
#        stop = False
#        found = False
#        position = startslot
#        while self.hash_table[position] != None and not found and not stop:
#            if self.hash_table[position] == item:
#                found = True
#                data = self.hash_table[position]
#            else:
#                position = self.has
#                if position == startslot:
#                    stop = True
#        return data
#        
#def get(self,key):
#  startslot = self.hashfunction(key,len(self.slots))
#
#  data = None
#  stop = False
#  found = False
#  position = startslot
#  while self.slots[position] != None and  \
#                       not found and not stop:
#     if self.slots[position] == key:
#       found = True
#       data = self.data[position]
#     else:
#       position=self.rehash(position,len(self.slots))
#       if position == startslot:
#           stop = True
#  return data
#        
#        