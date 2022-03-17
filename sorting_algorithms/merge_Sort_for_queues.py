from LinkedQueue import LinkedQueue

def merge(S1,S2,S):
    """Merge two sorted queues S1 and S2 into empty queue S"""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())

    # load remaining elements of S1 to S if any
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    
    while not S2.is_empty():
        S.enqueue(S2.dequeue())

def merge_Sort(S):
    """Sort elements of a queue S using the merge sort algorithm"""

    n = len(S)

    if n < 2:
        return
    mid = n //2

    S1 = LinkedQueue()
    S2 = LinkedQueue()

    for i in  range(mid):
        S1.enqueue(S.dequeue())

    while not S.is_empty():
        S2.enqueue(S.dequeue())

    merge_Sort(S1)
    merge_Sort(S2)

    merge(S1,S2,S)

