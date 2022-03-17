"""
To sort a sequence S with n elements using the
three divide-and-conquer steps, the merge-sort algorithm proceeds as follows:
1. Divide: If S has zero or one element, return S immediately; it is already
sorted. Otherwise (S has at least two elements), remove all the elements
from S and put them into two sequences, S1 and S2, each containing about
half of the elements of S; that is, S1 contains the first floor(n/2) elements of S,
and S2 contains the remaining ceil(n/2) elements.
2. Conquer: Recursively sort sequences S1 and S2.
3. Combine: Put back the elements into S by merging the sorted sequences S1
and S2 into a sorted sequence.


"""


def merge(S1, S2, S):
    """A function which takes in two sorted lists and merges them into 
    S- unsorted list that is the "parent" of S1 and S2"""

    i=j=0

    while i+j < len(S):   # while we still have elements somewhere
        #Elements will be added from S1 if
        #- all elements in S2 have been added
        # OR
        #- elements from S1 are not yet done and S1[i] is less than S2[j] 
        if j == len(S2) or (i < len(S1)  and  S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1



def merge_sort(S):
    """Sort an array using merge sort"""

    #get length
    n = len(S)

    #base case: if list is a single value,return since it is already sorted
    if n < 2:
        return

    #divide into S1 and S2
    mid_point = n // 2 #floor
    S1 = S[0:mid_point]
    S2 = S[mid_point:n] 
    #conquer with recursion
    merge_sort(S1)
    merge_sort(S2)
    #now that both are sorted,you can merge using merge

    merge(S1, S2, S)



if __name__ == "__main__":
    my_array = [1,57,6,9,78,3,11,56]
    merge_sort(my_array)
    print(my_array)
