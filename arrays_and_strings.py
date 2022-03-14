


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

def one_away(string1, string2):
    """There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false"""
    
    # preliminary check
    # if one string is longer by 2, then automatically, a single edit won't be enough
    difference = len(string1) - len(string2)
    longer_string = string1 if len(string1) > len(string2) else string2
    shorter_string = string2 if len(string1) > len(string2) else string1
    if difference > 1 or difference < -1:
        return False 

    one_character_difference = False

    def one_char_is_different(shorter_string, longer_string):
        for i in range(len(shorter_string)):
            if shorter_string[i] != longer_string[i]:
                return i,True
        return None, False

    


    if difference == 0:# same length thus an index can be used
        
        for i in range(len(string1)):
            if string1[i] != string2[i] and one_character_difference is True:
                return False
            if string1[i] != string2[i] and one_character_difference is False:
                one_character_difference = True
    else:   #length differs by one
        index, one_character_difference = one_char_is_different(shorter_string, longer_string)
        # remove the character from that index in the longer string
        if index is not None:
            longer_string_array = list(longer_string)
            print("longer string before")
            print(longer_string)
            longer_string_array[index] =""
            longer_string = "".join(longer_string_array)
            print("longer string after")
            print(longer_string)
        # perform the same operation since they are now same length
        #note that one_character_difference is now True since one character already failed
        for i in range(len(shorter_string)):
            if shorter_string[i] != longer_string[i] and one_character_difference is True:
                return False
            if shorter_string[i] != longer_string[i] and one_character_difference is False:
                one_character_difference = True
                

    return True




def string_compression(string):
    """Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)."""

    final_string_list = []
    char_count = 0
    prev_char = ""

    for char in string:
        if prev_char == char:
            char_count += 1         # increase count if char is same as previous
        else:   # current char differs from the previous
            # we should append the previous and it's count and then set our current as previous.
            # we also reset the count to 1
            if char_count != 0 and prev_char != "": # prevent appending zeros and empty for the first step
                final_string_list.append(prev_char)
                final_string_list.append(str(char_count))
            
            prev_char = char
            char_count = 1    
    # append the final chaarcter and its count.
    # The loop above only appends when there is a change between the previous
    # and current character.
    # for the final character, there is no change from the previous and thus we append it manually        
    final_string_list.append(prev_char)
    final_string_list.append(str(char_count))

    final_string = "".join(final_string_list)

    if len(string) <= len(final_string):
        return string
    return final_string





def rotate_matrix(matrix):
    """Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees."""
    # print the before matrix
    print('Before matrix')
    for row in matrix:
        print(row)

    n = len(matrix)
    #initialize zero matrix NxN
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    #to rotate by 90 degrees,
    #previous -> some_row, some step from 0
    #new -> some step from N, some row

    for row in range(n):
        for column in range(n):
            current_val = matrix[row][column]
            new_matrix[n-1-column][row] = current_val
        

    # print the after matrix
    print('After matrix')
    for row in new_matrix:
        print(row)
    

def zero_matrix(matrix):
    """Write an algorithm such that if an element in an MxN matrix is 0, 
    its entire row and column is set to 0"""

    # first mark all the places with zeros.
    # don't replace first, otherwise the entire matrix will be replaced to zeros

    # print the before matrix
    print('Before matrix')
    for row in matrix:
        print(row)
    mark_list = []

    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])

    for row in range(no_of_rows):
        for column in range(no_of_columns):
            if matrix[row][column] == 0:
                mark_list.append((row,column))

    for mark in mark_list:
        row,column = mark
        for single_column in range(no_of_columns):
            matrix[row][single_column] = 0
        for single_row in range(no_of_rows):
            matrix[single_row][column] = 0

    # print the after matrix
    print("After Matrix")
    for row in matrix:
        print(row)







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
    #result = palindrome_permutation("racecar")
    #print(result)
    #5
    result = one_away("pale","pale")
    print(result)
    #6
    #result = string_compression("aabcccccaaa")
    #print(result)
    #7
    # rotate_matrix([
    #         [1, 2, 3, 4, 5],
    #         [6, 7, 8, 9, 10],
    #         [11, 12, 13, 14, 15],
    #         [16, 17, 18, 19, 20],
    #         [21, 22, 23, 24, 25]
    #     ])
    #8
    #zero_matrix([
    #        [1, 2, 3, 4, 0],
    #        [6, 0, 8, 9, 10],
    #        [11, 12, 13, 14, 15],
    #        [16, 0, 18, 19, 20],
    #        [21, 22, 23, 24, 25]
    #    ])
