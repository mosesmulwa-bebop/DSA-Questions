


def isUnique(my_string):
    """determine if a string has all unique characters"""
    # assume characters set is ASCII(it only has 128 characters)
    if len(my_string) > 128: # a character must be repeated in this case
        return False 
    # create an array that denotes whether a certain character is in the string
    char_set = [False for char in range(128)] # as of now,no character is in the string

    for char in my_string:
        val = ord(char)  # this gives it's integer unicode form (from 0 to 127)
        if char_set[val]: # if the element at that index is set to True, meaning we had seen it before
            return False
        char_set[val] = True

    return True # the for loop above has completed without returning false thus all characters are unique

    
        
def check_permutation(string1, string2):
    """Given two strings, determine if one is a permutation of the other"""

    # first they have to have equal length.
    if len(string1) != len(string2):
        return False


    # assume ASCII
    # set frequency for all characters to be 0
    string1_freq = [0 for _ in range(128)] 
    string2_freq = [0 for _ in range(128)]

    # increase frequency every time we meet a character
    for i in range(0,len(string1)):
        val1 = ord(string1[i])
        val2 = ord(string2[i])
        string1_freq[val1] += 1
        string2_freq[val2] += 1

    # compare the two frequency lists
    for i in range(0, len(string1_freq)):
        if string1_freq[i] != string2_freq[i]:
            return False
    
    return True
    
            





def urllify(true_length, my_string):
    """Replace all spaces in a string with %20 and remove trailing spaces.
    given the "true" length of the string. true length includes legitimate spaces
    but not the trailing ones.
    """
    
    string_array = my_string.split(" ")
    for word in string_array:
        if word == '':
            string_array.remove(word)
    string_array.pop()
    print(string_array)
    final_string = "%20".join(string_array)
    print(final_string)

def palindrome_permutation(string):
    """Given a string, check if it is a permutation of a palindrome.
    
    Input: Tact Coa
    Output: true   
    """
    # A palindrome should have at most one odd number of a single character,
    #  all others must occur in pairs
    #use a hash table/dict, key:character, value:frequency. Check that frequency matches the above.
    #
    # 
    my_dict = {}

    for char in string:
        if char != " ":
            from_map =my_dict.get(char)
            if from_map is not None and from_map >= 1:
                my_dict[char] += 1
            if from_map is None:
                my_dict[char] = 1
        
    count_of_odd = 0
    for key,value in my_dict.items():
        if value % 2 != 0:
            count_of_odd += 1

    if count_of_odd <= 1:
        return True
    else:
        return False
    

if __name__ == "__main__":
    
    #1
    #result = isUnique("abcdg")
    #print(result)
    #2
    #result = check_permutation("abcdg","gdcbaf")
    #print(result)
    #3
    #urllify(13,"mr john smith   ")
    #4
    result = palindrome_permutation("racecar")
    print(result)