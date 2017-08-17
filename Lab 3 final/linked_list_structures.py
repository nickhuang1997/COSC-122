<<<<<<< HEAD
'''Data structures implemented with linked lists.'''
import doctest
import os


class Node:
    '''A node for a linked list.'''

    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None


class Stack(object):
    """ Implements a Stack using a Linked List"
    >>> s = Stack()
    >>> print(s)
    List for stack is: None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    List for stack is: a -> None
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> print(s)
    List for stack is: None
    >>> s.push('b')
    >>> print(s)
    List for stack is: b -> None
    >>> s.push('c')
    >>> print(s)
    List for stack is: c -> b -> None
    >>> len(s)
    2
    >>> s.peek()
    'c'
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    List for stack is: b -> None
    >>> e = Stack()
    >>> e.peek()
    Traceback (most recent call last):
    ...
    IndexError: Can't peek at empty stack.
    """

    def __init__(self):
        self.head = None
        
        
    def push(self, item):
        """push a new item on to the stack
        inserts item at head of list
        """
        # ---start student section---
        
        temp = Node(item)
        temp.next_node = self.head
        self.head = temp
        
        # ===end student section===

    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't pop from empty stack.")
        # ---start student section---
        
        if self.is_empty():
            raise IndexError("Can't pop from empty stack.")
        
        else:
            temp = self.head.data
            self.head = self.head.next_node
            return temp
        
       
        # ===end student section===

    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it.
        If stack is empty you should raise an IndexError as per
        the comment below.
        """
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't peek at empty stack.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't peek at empty stack.")
        else:
            return self.head.data
        # ===end student section===

    def is_empty(self):
        """ Returns True if stack is empty """
        return self.head is None

    def __len__(self):
        """ Returns the length --- calling len(s) will invoke this method """
        # ---start student section---
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next_node
        
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the stack starting
        from the beginning of the list. Items are separated by ->
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
        return 'List for stack is: ' + (' -> '.join(listdata))
    
        
        # ===end student section===

#    >>> len(q)
#    0
#    >>> print(q)
#    List for queue is: None
#    >>> result = q.dequeue()
#    Traceback (most recent call last):
#    ...
#    IndexError: Can't dequeue from empty queue.
class Queue(object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()

    >>> q.enqueue('a')
    >>> print(q)
    List for queue is: a -> None
    >>> len(q)
    1
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
    
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        # ---start student section---
        #while current.nextnode is not none...
        # then change current to equal current.nextnode
        
        if self.is_empty():
            self.head = Node(item)
        else:
            temp = self.head
            while temp.next_node is not None:
                temp = temp.next_node
            temp.next_node = Node(item)
#                
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when queue is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't dequeue from empty queue.")
        
        else:
            temp = self.head
            self.head = self.head.next_node
            return temp.data
        # ===end student section===

    def is_empty(self):
        """ returns True if the queue is empty """
        # ---start student section---
        return self.head is None
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next_node
        
        return count        
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting
        from the beginning of the list. Items are separated by ->
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

=======
'''Data structures implemented with linked lists.'''
import doctest
import os


class Node:
    '''A node for a linked list.'''

    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None


class Stack(object):
    """ Implements a Stack using a Linked List"
    >>> s = Stack()
    >>> print(s)
    List for stack is: None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    List for stack is: a -> None
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> print(s)
    List for stack is: None
    >>> s.push('b')
    >>> print(s)
    List for stack is: b -> None
    >>> s.push('c')
    >>> print(s)
    List for stack is: c -> b -> None
    >>> len(s)
    2
    >>> s.peek()
    'c'
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    List for stack is: b -> None
    >>> e = Stack()
    >>> e.peek()
    Traceback (most recent call last):
    ...
    IndexError: Can't peek at empty stack.
    """

    def __init__(self):
        self.head = None
        
        
    def push(self, item):
        """push a new item on to the stack
        inserts item at head of list
        """
        # ---start student section---
        
        temp = Node(item)
        temp.next_node = self.head
        self.head = temp
        
        # ===end student section===

    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't pop from empty stack.")
        # ---start student section---
        
        if self.is_empty():
            raise IndexError("Can't pop from empty stack.")
        
        else:
            temp = self.head.data
            self.head = self.head.next_node
            return temp
        
       
        # ===end student section===

    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it.
        If stack is empty you should raise an IndexError as per
        the comment below.
        """
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't peek at empty stack.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't peek at empty stack.")
        else:
            return self.head.data
        # ===end student section===

    def is_empty(self):
        """ Returns True if stack is empty """
        return self.head is None

    def __len__(self):
        """ Returns the length --- calling len(s) will invoke this method """
        # ---start student section---
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next_node
        
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the stack starting
        from the beginning of the list. Items are separated by ->
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
        return 'List for stack is: ' + (' -> '.join(listdata))
    
        
        # ===end student section===

#    >>> len(q)
#    0
#    >>> print(q)
#    List for queue is: None
#    >>> result = q.dequeue()
#    Traceback (most recent call last):
#    ...
#    IndexError: Can't dequeue from empty queue.
class Queue(object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()

    >>> q.enqueue('a')
    >>> print(q)
    List for queue is: a -> None
    >>> len(q)
    1
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
    
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        # ---start student section---
        #while current.nextnode is not none...
        # then change current to equal current.nextnode
        
        if self.is_empty():
            self.head = Node(item)
        else:
            temp = self.head
            while temp.next_node is not None:
                temp = temp.next_node
            temp.next_node = Node(item)
#        newnode = Node(item)
#        if self.head is None and self.tail is None:
#            self.head = newnode
#            self.tail = self.head
#        else:
#            self.tail.next_node = newnode
#            self.tail = newnode
#            
#        current = self.head
#        
#        found = False

#

#        while current.next_node != None and not found:
#            if current.data == item:
#                found = True
#            else:
#                current = current.next_node
#        
#                
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when queue is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't dequeue from empty queue.")
        
        else:
            temp = self.head
            self.head = self.head.next_node
            return temp.data
        # ===end student section===

    def is_empty(self):
        """ returns True if the queue is empty """
        # ---start student section---
        return self.head is None
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next_node
        
        return count        
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting
        from the beginning of the list. Items are separated by ->
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

>>>>>>> dcd2562de721186341eb5cf957d33142bd94e945
