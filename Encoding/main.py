#============================================================================================================================
#                                                     LABEL ENCODING
#============================================================================================================================


char_list:list = ["a", "f", "g", "e", "b", "c", "d"]

def label_encoding(char_list:list)->list:
    '''
    This function is used for encoding which converts text data into numeric data, based on alphabetic order.
    '''
    sorted_char_list:list = sorted(char_list)

    encoded:list = []

    for ch in char_list:
        index = sorted_char_list.index(ch)
        encoded.append(index)

    return encoded

print(label_encoding(char_list))

#============================================================================================================================
#                                                     ORDINAL ENCODING
#============================================================================================================================

char_list:list = ["a", "f", "g", "e", "b", "c", "d"]

def ordinal_encoding(char_list:list)->list:
    '''
    This function is used for encoding which converts text data into numeric data, 
    Assuming that the passed list is the order in which the user wants encoding
    '''

    encoded:list = []

    for ch in char_list:
        index = char_list.index(ch)
        encoded.append(index)

    return encoded

print(ordinal_encoding(char_list))
