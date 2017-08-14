"""Complete the Queue2 class so that it makes use of the head/tail pointers
Make sure you keep the new doctests given below.
"""
import doctest
import os


class Node:
    """A node for a linked list."""

    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None
        self.previous = None


class Queue2(object):
    """ Implements a Queue using a Linked List with head and tail pointers
    You should be able to copy a lot of your code from your Queue class
    but you will be able to make efficiency gains via the use of a tail pointer
    >>> q = Queue2()
    >>> len(q)
    0
    >>> print(q)
    List for queue is: None
    >>> result = q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from empty queue.
    >>> q.enqueue('a')
    >>> print(q)
    List for queue is: a -> None
    >>> print(q.tail.data)
    a
    >>> print(q.head.data)
    a
    >>> len(q)
    1
    >>> q.dequeue()
    'a'
    >>> len(q)
    0
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> print(q)
    List for queue is: a -> b -> None
    >>> q.enqueue('c')
    >>> print(q)
    List for queue is: a -> b -> c -> None
    >>> len(q)
    3
    >>> q.dequeue()
    'a'
    >>> print(q)
    List for queue is: b -> c -> None
    >>> q.enqueue('z')
    >>> print(q.head.data)
    b
    >>> print(q.tail.data)
    z
    >>> q.dequeue()
    'b'
    >>> q.dequeue()
    'c'
    >>> q.dequeue()
    'z'
    >>> print(q.head)
    None
    >>> print(q.tail)
    None
    """

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        
        fresh_node = Node(item)
        if self.head is None and self.tail is None:
            self.head = fresh_node
            self.tail = self.head
        else:
            self.tail.next_node = fresh_node
            self.tail = fresh_node
        
        
#        new = Node(item)
#        new.next_node = None
#        if self.head.is_empty:
#            self.head = new
#            self.tail = new
#        else:
#            self.tail.next_node = new
#            new.next_node = self.tail
#            self.tail = new
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error if stack is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        
        if self.is_empty():
            
            raise IndexError("Can't dequeue from empty queue.")
        else:
            data = self.head.data
            
            if self.head.next_node is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
            return data

#        else:
#            self.temp = self.head
#            self.head = self.head.next
#            return self.temp
#        else:
#            temp = self.head
#            self.head = self.head.next_node
#            if self.is_empty():
#                self.tail = None
#            return temp.data
#                
        # ===end student section===

    def is_empty(self):
        """ Returns True if the Queue is empty """
        # ---start student section---
        return self.head is None
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method"""
        # ---start student section---
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next_node
        
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue
        starting from the beginning of the list.
        Items are separated by ->
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        listdata = []
        temp = self.head
        while temp is not None:
            listdata.append(str(temp.data))
            temp = temp.next_node
        listdata.append('None')
        return 'List for queue is: ' + (' -> '.join(listdata)) 
        # ===end student section===


if __name__ == '__main__':
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    # Uncomment the testmod() line to run the tests
    # Can enter an infinite loop if your Stack isn't implemented correctly
    doctest.testmod()
#
#q = Queue2()
#print('length =', len(q))
#print(q)
