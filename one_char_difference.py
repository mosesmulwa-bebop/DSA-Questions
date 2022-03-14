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

    one_character_difference = True

    def one_char_is_different(shorter_string, longer_string):
        for i in range(len(shorter_string)):
            if shorter_string[i] != longer_string[i]:
                return i,True
        return None, False

    


    if difference == 0:# same length thus an index can be used
        #equal_strings_check(string1, string2, one_character_difference)
        for i in range(len(string1)):
            if string1[i] != string2[i] and one_character_difference is True:
                return False
            if string1[i] != string2[i] and one_character_difference is False:
                one_character_difference = True
    else:   #length differs by one
        index, one_character_difference = one_char_is_different(shorter_string, longer_string)
                #equal_strings_check(longer_string, shorter_string, one_character_difference=True)
        if index is not None:
            longer_string_array = list(longer_string)
            print("longer string before")
            print(longer_string)
            longer_string_array[index] =""
            longer_string = "".join(longer_string_array)
            print("longer string after")
            print(longer_string)
        for i in range(len(shorter_string)):
            if shorter_string[i] != longer_string[i] and one_character_difference is True:
                return False
            if shorter_string[i] != longer_string[i] and one_character_difference is False:
                one_character_difference = True
                

    return True




if __name__ == "__main__":
    result = one_away("bale","ble")
    print(result)