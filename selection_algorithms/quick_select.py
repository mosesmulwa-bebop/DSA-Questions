import random

def quick_select(S, k):
    """Return the kth smallest element of list S ,for k from 1 to len(S) 
    """
    #if S only has one element,return immediately
    if len(S) == 1:
        return S[0]

    # find pivot as a random choice from the list
    pivot = random.choice(S)

    # create lists to hold elements less than , equal to and greater than pivot

    L = []
    E = []
    G = []

    
    for i in range(len(S)):
        if S[i] < pivot:
            L.append(S[i])
        elif S[i] == pivot:
            E.append(S[i])
        elif S[i] > pivot:
            G.append(S[i])

    # Narrow down to which list contains the kth smallest element

    if k <= len(L): # this means that kth smallest must be in L since it contains at least k elements
        return quick_select(L, k)
    # if the number of elements in L are less than k but elements in E and L are more or equal to k
    # then it means the pivot is the kth smallest since E only contains pivot elements. 
    elif k <= len(L) + len(E):  
        return pivot
    else:   # kth smallest is in G.However we can't call quick select immediately.
            # we know that at this point number of elements in L and E do not add up to k
            # G is only a small subsection of the original S
            # calling quick select on it with k will be looking for kth smallest on G 
            # which is wrong
            # To solve this,
            # consider if we were looking for the 7th smallest element
            # if for instance L and E only contained 5 elements combined
            # we can't look for the 7th smallest in G
            # we can however substract 5 and look for the 2nd smallest in G
            # this is the solution
            # Think if the list was sorted
            # 1,2,3,4,5,6,7,8,9
            # if L and E were the first five , then G would be 6,7,8,9
            # to find the number 7 we would need to look for the 2nd smallest in G
            # since 2nd smallest in G is 7th smallest in S
        j = k - len(L) - len(E)
        return quick_select(G, j)


if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,9]
    print(quick_select(my_list,5))
    
    