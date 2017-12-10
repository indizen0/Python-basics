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

#urlify a string. extra spaces present in input string
def urlify(String1, length):
    char_space = " "
    char_url = "%20"
    url_string = ""
    for i in range(0,len(String1)):
        if String1[i] == char_space:
            if len(url_string) == 0:
                url_string = String1[:i] + char_url
            else:
                url_string = url_string + char_url
        else:
            url_string = url_string + String1[i]
        if len(url_string) == length:
            break
    return url_string

#check if string is a palindrome
def check_palindrome(string1):
    flag = True
    fw_index = 0
    bw_index = len(string1)
    string1 = string1.lower()
    string1 = string1.replace(" ,.?!",)

    for char in string1:
        if char == " ":
            fw_index = fw_index +1
            continue
        while string1[bw_index-1] == " ":
            bw_index = bw_index - 1

        if char == string1[bw_index-1]:
            fw_index = fw_index+1
            bw_index = bw_index-1
        else:
            flag = False
            break
        if fw_index >= bw_index:
            break
    return flag
