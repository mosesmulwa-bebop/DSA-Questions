from LinkedQueue import LinkedQueue

def quick_sort(S):

    n = len(S)

    if n < 2:
        return

    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    pivot =S.first()

    for i in range(n):
        value = S.dequeue()
        if value < pivot:
            L.enqueue(value)
        elif value == pivot:
            E.enqueue(value)
        elif value > pivot:
            G.enqueue(value)

    quick_sort(L)
    quick_sort(G)

    while not L.is_empty():
        S.enqueue(L.dequeue())

    while not E.is_empty():
        S.enqueue(E.dequeue())

    while not E.is_empty():
        S.enqueue(E.dequeue())