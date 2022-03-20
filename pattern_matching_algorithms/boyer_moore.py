"""
The main idea of the Boyer-Moore algorithm is to improve the running time of
the brute-force algorithm by adding two potentially time-saving heuristics. Roughly
stated, these heuristics are as follows:

Looking-Glass Heuristic: When testing a possible placement of P against T, begin
    the comparisons from the end of P and move backward to the front of P.

Character-Jump Heuristic: During the testing of a possible placement of P within
    T, a mismatch of text character T[i]=c with the corresponding pattern character
    P[k] is handled as follows. If c is not contained anywhere in P, then
    shift P completely past T[i] (for it cannot match any character in P). Otherwise,
    shift P until an occurrence of character c in P gets aligned with T[i].


"""