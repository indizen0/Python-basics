# check duplicate characters in a string
def check_char_duplicate(String1):
    str_len = len(String1)
    index = 0
    for char1 in String1:
        if index == str_len:
            pass
        sub_string = String1[index+1:]
        for char in sub_string:
            if char1 == char:
                return True
        index = index+1

    return False

# check duplicate characters in a string without new data structure
def check_char_dup(String1):
    str_len = len(String1)
    index = 0
    for char1 in String1:
        if index == str_len:
            pass
        for i in range(index+1,str_len,1):
            if char1 == String1[i]:
                return True
        index = index+1
    return False

#Check if two strings are just permutation of one another
def check_string_permu(String1, String2):
    for char1 in String1:
        for i in range(0,len(String2)):
            if char1 == String2[i]:
                if i == 0:
                    String2 = String2[i+1:]
                else:
                    String2 = String2[:i]+String2[i+1:]
                break
    if len(String2) == 0:
        return True
    else:
        return False
