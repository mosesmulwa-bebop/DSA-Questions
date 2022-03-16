from LinkedList import LinkedList
import math


"""Workimg with linked lists.

If we want to move pointer to the tail or some values then 

while current_node.next is not None:
    current_node = current_node.next

Will work perfectly.


However, if we are also operating on the values in each node, then the loop above will not 
work for the tail node since it will not run.
You can solve this by manually running the final iteration yourself.

Or you can use a do while loop though I have not tested it yet.

"""











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

def delete_middle_node(ll, given_node):
    """
    Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    lnput:the node c from the linked lista->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

    --my solution--
    To delete a node, you need the next value of the previous node to the one after the current node
    Think of a ll with 1-2-3
    Given node 2
    We can easily get 3 from the next value of 2
    TO get 1, go through the ll as look for node whose next value is 2.
    Also confirm that the next of that 2 is the 3 you expect.
    This prevents deleting the wrong node
    Then set next of 1 as 3. Then you're done

    --very easy solution-----
    given 1-2-3-4
    we want to delete 2.
    replace value and next of 2 with those of it's next node. In this case 3
    so it becomes 1-3-4 since value of 3 was 3 and it's next was 4
    so instead of next being 3 we go to 4 thus basically eliminating the original 3 node
    """
    # preliminary - empty list
    if ll.head is None:
        return

    node_3 = given_node.next
    current_node = ll.head
    # find node_1
    while current_node.next is not None:
        if current_node.next == given_node: # suspected node_2
            if current_node.next.next == node_3: # confirmed node_2
                break
        current_node = current_node.next
    
    current_node.next = given_node.next
    return ll

def partition(ll, x):
    """
    Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

    -----------my solution---------
    create a left partition and a right partition
    Go through the ll. Anything less than x goes to left partition.
    Else right partition.
    After,join left and right partition.
    Return final linked list

    """
    # preliminary - empty list
    if ll.head is None:
        return

    current_node = ll.head
    left_partition = LinkedList()
    right_partition_array = []

    while current_node.next is not None:
        if current_node.value < x :
            left_partition.add(current_node.value)
            current_node = current_node.next
        else:
            right_partition_array.append(current_node.value)
            current_node = current_node.next

    for i in range(len(right_partition_array)):
        left_partition.add(right_partition_array[i])
    
    

    return left_partition
    
def sum_lists(ll1, ll2):
    """You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
    ----my solution---------------
    Read each ll and store the values in an array.
    Reverse the arrays and join into a string which can be converted to an int
    The int can be converted to a string and then to an array.
    Reverse the array.
    For each element add it into a linked list.
    Return the linked list
"""
    # both lls empty
    if ll1.head is None and ll2.head is None:
        return

    ll1_array = []
    ll2_array = []

    current_node1 = ll1.head
    current_node2 = ll2.head

    while current_node1.next is not None:
        ll1_array.append(str(current_node1.value))
        current_node1 = current_node1.next
    ll1_array.append(str(current_node1.value))# for the final value


    while current_node2.next is not None:
        ll2_array.append(str(current_node2.value))
        current_node2 = current_node2.next
    ll2_array.append(str(current_node2.value))# for the final value

    ll1_array.reverse()
    ll2_array.reverse()

    ll1_string = "".join(ll1_array)
    ll2_string = "".join(ll2_array)

    ll1_num = int(ll1_string)
    ll2_num = int(ll2_string)
    
    result = ll1_num + ll2_num
    result_string = str(result)
    result_list = list(result_string)
    result_list.reverse()

    final_ll = LinkedList()

    for i in range(len(result_list)):
        final_ll.add(result_list[i])

    return final_ll


def palindrome(ll):
    """Implement a function to check if a linked list is a palindrome.
    
    ---------- my solution-----------
    This is a singly linked list so having two pointers one at head and one at tail will not work easily
    due to challenge in going back.
    We can use a stack where we push the first floor(n/2) elements.
    Depending on whether n is odd or even we may skip the middle node.
    After that, pop each value and compare it to current value.
    If equal go to next node and repeat.
    If all completed without error, then it is a palindrome.
    e.g racecar
    push r,a,c
    skip middle node e since n is odd
    at c, pop stack which will return c and compare.
    Go to next node a, repeat.
    """


    my_stack = []

    n= len(ll)
    number_of_steps = math.floor(n/2)

    current_node = ll.head
    #move pointer to middle or node next to middle
    for i in range(number_of_steps):
        my_stack.append(current_node.value)
        current_node = current_node.next

    #skip middle node if n is odd
    if n%2 != 0:
        current_node = current_node.next
    #now at second half
    for i in range(number_of_steps):
        my_value = my_stack.pop()
        current_value = current_node.value

        if my_value != current_value:
            return False
        
        current_node = current_node.next
    
    return True

def loop_detection(ll):
    """Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C - > D -> E -> C [the same C as earlier]
Output: C
    -----------------my solution------------
    create a set of all seen values. return if node already seen

"""

    current_node = ll.head
    # create a new set 
    seen_values = set([])    
    
    while current_node.next is not None:
        if current_node.value in seen_values:
            return current_node.value
        seen_values.add(current_node.value)
        current_node = current_node.next
    #final value
    if current_node.value in seen_values:
        return current_node.value       

if __name__ == "__main__":
    #1
    # ll = LinkedList()
    # ll.generate(100, 0, 9)
    # print(ll)
    # remove_dups(ll)
    # print(ll)
    #2
    #ll = LinkedList()
    #ll.generate(10, 0, 99)
    #print(ll)
    #print(kth_to_last(ll, 3))
    #3
    # ll = LinkedList()
    # ll.add_multiple([1, 2, 3, 4])
    # middle_node = ll.add(5)
    # ll.add_multiple([7, 8, 9])
    # print(ll)
    # delete_middle_node(ll, middle_node)
    # print(ll)
    #4
    #ll = LinkedList()
    #ll.add_multiple([3,5, 8, 5,10 ,2, 1])
    #print(ll)
    #print(partition(ll, 5))
    #5
    # ll1 = LinkedList()
    # ll2 = LinkedList()
    # ll1.add_multiple([7,1,6])
    # ll2.add_multiple([5,9,2])
    # print(sum_lists(ll1, ll2))
    #6
    #ll = LinkedList()
    #ll.add_multiple(['r','a','c','e','c','a','r'])
    #print(palindrome(ll))
    #7
    ll = LinkedList()
    ll.add_multiple(['a','b','c','d','e','c'])
    print(ll)
    print(loop_detection(ll))
