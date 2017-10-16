"""
File: patient_queue.py
Author: your name should probably go here

Maintain a patient queue that sorts patients based on the diseases
they have been diagnosed with, and the duration of time since the
diagnosis.
"""

from classes import PriorityQueue, Patient
from utilities import *
from patient_queue import *

class PatientHeapQueue(PriorityQueue):
    """ Implement a queue structure using a 0-indexed heap.
        This particular type of queue holds patient information.
    """

    def __init__(self, start_data=None, fast=False):
        """ Create the patient queue.
        """
        if start_data is None:
            start_data = []
        self.comparisons = 0
        self.data = []
        if fast:
            self._fast_heapify(start_data)
        else:
            self._heapify(start_data)

    def _swap(self, i, j):
        """ Swap the patients at positions i and j.
        """
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _parent_index(self, index):
        """ Determine the parent index of the current index.
            For a binary heap that is zero-indexed, this is
            p = (i - 1) // 2
        """
        return (index - 1) // 2

    def _child_indices(self, index):
        """ Calculate the child indices for the current index.
            For a binary heap that is zero-indexed, this is
            c1 = 2*i + 1
            c2 = 2*i + 2
        """
        return [
            2 * index + delta
            for delta in range(1, 2 + 1)
        ]

    def _max_child_priority_index(self, child_indices):
        """ Find the child among the given indices that has the highest priority.
            If an index is not valid, do not consider it. If none are valid, then
            return None. Assumes the child_indices are in order.
        """
        max_index = None
        for index in child_indices:
            if index >= len(self.data):
                break  # No more valid children
            if max_index is None:  # This is the first child, it's valid, so use it
                max_index = index
            else:
                self.comparisons += 1  # Don't worry, we do the comparison counting here
                if self.data[index].priority > self.data[max_index].priority:
                    max_index = index
        return max_index

    def _sift_up(self, index):
        """ Move the patient at the given index into the correct location
            further up in the heap by swapping with its parents if appropriate.
        """
        right_spot = False
        parent_index = self._parent_index(index)
        
        while right_spot == False:
            self.comparisons += 1
            if self.data[index-1].priority > self.data[parent_index].priority:
                self._swap(index, parent_index)
            else:
                right_spot = True
        

    def _sift_down(self, index):
        """ Move the patient at the given index into the correct location
            further down in the heap by swapping with its children if appropriate.
        """
        pass

    def _heapify(self, data):
        """ Turn the existing data into a heap in O(n log n) time.
        """
        for patient in data:
            self.enqueue(patient)

    def _fast_heapify(self, data):
        """ Turn the existing data into a heap in O(n) time.
        """
        pass

    def enqueue(self, patient):
        """ Add a patient to the queue.
        """
        # We first make sure that we're only including Patients
        assert isinstance(patient, Patient)
        
        self.data.insert(len(self.data), patient) #puts item at end of data list
        self._sift_up(len(self.data))             #moves patient to appropriate spot
        
               
        
    def dequeue(self):
        """ Take a patient off the queue and return the Patient object
        """
        item_off = self.data[0]
        new_list = self.data[1:]
        self.data = new_list
        return item_off


class EditablePatientHeapQueue(PatientHeapQueue):
    """ Implement a queue structure using a 0-indexed heap.
        This particular type of queue holds patient information.
        Additionally, we can remove patients not at the top of
        the heap in O(log n) time.
    """

    def __init__(self, start_data=None, fast=False):
        self.indices = {}  # name -> index;
                          # Keep track of where patients are stored
        for (i, person) in enumerate(start_data):
            self.indices[person.name] = i
        super().__init__(start_data, fast)

    def _swap(self, i, j):
        """ Swap patients at index i and j. Don't forget to change
            their position in self.indices as well!
        """
        pass

    def remove(self, patient_name):
        """ Remove the particular patient from the heap. Remember,
            the index will tell you where the patient is in the heap
            and every sub-heap below an index forms a valid heap.
        """
        pass

    def enqueue(self, patient):
        """ Add a patient to the queue. Let the superclass do
            most of the work.
        """
        pass

    def dequeue(self):
        """ Remove a patient from the front of the queue and return them.
            Again, let the superclass do most of the work.
        """
        pass
