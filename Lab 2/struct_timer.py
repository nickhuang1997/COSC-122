import sys
import time
from stack import Stack
from queue122 import Queue
from deque import Deque

# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method
# define get_time to be the appropriate time counter
if sys.version_info < (3, 3):
    get_time = time.clock
    print("Using time.clock for timing - Python ver < 3.3")
else:
    get_time = time.perf_counter
    print("Using time.perf_counter for timing - Python ver >= 3.3")
    REZ = time.get_clock_info('perf_counter').resolution
    print('Smallest unit of time is ' + str(REZ) + ' seconds')



def time_stack_push(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    s = Stack()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    for _ in range(initial_size):
        s.push(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        s.push(0)
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/push for {:,d} pushes is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))




# Do some creative copy and pasting here to make functions for other time trials
# ---start student section---
def time_stack_pop(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    s = Stack()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    
    for _ in range(initial_size):
        s.push(0)

    # time some pushes
    
    
    ###############################################
    

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        s.pop()
        
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/pop for {:,d} pops is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))

def time_stack_peek(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    s = Stack()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    
    for _ in range(initial_size):
        s.push(0)


    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        s.peek()
        
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/peek for {:,d} peeks is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))


###########################################################################################
    
def time_stack_enqueue(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    q = Queue()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    for _ in range(initial_size):
        q.enqueue(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        q.enqueue(0)
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/enqueue for {:,d} enqueues is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))

def time_stack_dequeue(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    q = Queue()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    for _ in range(initial_size):
        q.enqueue(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        q.dequeue()    
    
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/dequeue for {:,d} dequeues is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))


#################################################################################
    

def time_stack_enqueue_front(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    d = Deque()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    
    #for _ in range(initial_size):
        #d.enqueue_front(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        d.enqueue_front(0)    
    
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/enqueue_front for {:,d} enqueue_fronts is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))


def time_stack_enqueue_rear(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    d = Deque()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    
    #for _ in range(initial_size):
        #d.enqueue_front(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        d.enqueue_rear(0)    
    
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/enqueue_rear for {:,d} enqueue_rear is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))


def time_stack_dequeue_front(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    d = Deque()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    
    for _ in range(initial_size):
        d.enqueue_front(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        d.dequeue_front()    
    
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/dequeue_front for {:,d} dequeue_front is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))


def time_stack_dequeue_rear(initial_size, n_trials):
    """ Finds average time for pushing onto a stack """
    d = Deque()
    # s._items = [0] * initial_size  # is cunning but causes weird timings
    # so simply push lots of items onto the stack
    # pre_fill stack with initial_size zeros (feel free to push other things)
    
    for _ in range(initial_size):
        d.enqueue_front(0)

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        d.dequeue_rear()    
    
    end_time=get_time()
    time_per_operation=(end_time - start_time)/n_trials
    fmt = "Initial Stack size = {:,d} -> avg. time/dequeue_rear for {:,d} dequeue_rear is {:10.8f}"
    print((fmt.format(initial_size, n_trials, time_per_operation)))
# ===end student section===



def run_tests():
    """ Runs as many or as few tests as you call,
    initially just runs the test for stack pushes
    """
    print('\n'*3)
    initial_size = 100000  # start with this many items in data structure
    n_trials = 100  # run this many trials and take the average time

    #time_stack_push(initial_size, n_trials)
    ## call your shiny new test functions here
    #time_stack_pop(initial_size, n_trials)
    #time_stack_peek(initial_size, n_trials)
    
    #time_stack_enqueue(initial_size, n_trials)
    #time_stack_dequeue(initial_size, n_trials)

    #time_stack_enqueue_rear(initial_size, n_trials)    
    #time_stack_enqueue_front(initial_size, n_trials)
    time_stack_dequeue_front(initial_size, n_trials)    
    time_stack_dequeue_rear(initial_size, n_trials) 

run_tests()
