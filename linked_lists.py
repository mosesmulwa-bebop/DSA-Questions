from LinkedList import LinkedList

def remove_dups(ll):
    """Write code to remove duplicates from an unsorted linked list.
    ll is a singly linked list so we only have access to next value 
    ---my solution-----
    A set of all the node elements will be used.
    Run through entire linked list
    For each node, check if it's element exists in the set .
    If it doesn't exist:
        add the element contained to the set
    If it does exist:
        delete the node.(or remove it from the linked list)

    Why set- sets do not allow for duplicates
    Set are usually implemented as hash tables in python so have O(1) access time
    """

    #return immediately for empty linked lists
    if ll.head is None:
        return

    current_node = ll.head
    # create a new set with the value of the head as it's first value
    seen_values = set([current_node.value])

    #run through entire linked list
    while current_node.next is not None: # as long as we are not at the tail
        # check if value of the next node is in seen_values
        if current_node.next.value in seen_values:
            # to remove it from the linked list,set the next to the node after that node
            # e.g 1-2-2-3
            #becomes 1-2-3 . we set next of 2 to be 3 as opposed to the original node with 2
            current_node.next = current_node.next.next     
        else:
            seen_values.add(current_node.next.value) # add value to seen values
            current_node = current_node.next         # go to next node

    return ll # return the new linked list

def kth_to_last(ll, k):
    """Implement an algorithm to find the kth to last element of a singly linked list
    
    --my solution--
    Use double runner technique
    Have two pointers, one starting at head, the other k nodes away from first one
    For each step,move the two pointers by one node
    When the runner pointer gets to the end(tail), then the first pointer is at the kth to last
    element 
    """

    # preliminary - empty list
    if ll.head is None:
        return
    
    current_node = ll.head
    runner = ll.head
    # move runner k nodes away
    for _ in range(k):
        # implemented a check to make sure that at least k elements are in the ll
        if runner.next is not None:
            runner = runner.next
            if runner is None:
                return
        
    
    while runner.next is not None: # as long as runner is not at tail
        runner = runner.next
        current_node = current_node.next

    return current_node.value

    

if __name__ == "__main__":
    #1
    # ll = LinkedList()
    # ll.generate(100, 0, 9)
    # print(ll)
    # remove_dups(ll)
    # print(ll)
    #2
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    print(kth_to_last(ll, 3))


