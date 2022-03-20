"""
Some terms
T - entire string, length n
P - substring we are testing, length m

We simply test all the possible placements of P relative to T.
we start at index 0 all the way to m places from the end. n - m + 1

"""

def brute_force(T, P):
    """Return the lowest index of T at which substring P begines(else -1)"""
    n, m = len(T), len(P)
    for i in range(n - m + 1): # try every potential starting index within T
        k = 0                  # an index into pattern P
        while k < m and T[i+k] == P[k]:     # kth character of P matches
            k += 1
        if k == m:  # we have matched the entire string. Thus return our starting index
            return i    # this means that P is from T[i:i+m]
        
    return -1

if __name__ == "__main__":
    full_string = "abcdefghi"
    substring = "def"
    print(brute_force(full_string, substring))