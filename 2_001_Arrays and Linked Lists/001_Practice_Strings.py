# String Reverser
def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    string_position = len(our_string) - 1
    reversed_string = ''

    while string_position >= 0:
        reversed_string += our_string[string_position]
        string_position -= 1

    return reversed_string


# Anagram Checker
def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    str1 = str1.lower()
    str2 = str2.lower()

    for character in str1:
        if character is ' ':  # Character "space" is omitted
            pass
        elif character in str2:
            str2 = str2.replace(character, '', 1)
        else:
            return False

    if len(str2.replace(' ', '')) == 0:  # Check for remaining characters
        return True
    else:
        return False


# Reverse the words in sentences
def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    our_string_split = our_string.split(sep=' ')
    words_reversed = []

    for word in our_string_split:
        words_reversed.append(string_reverser(word))

    return " ".join(words_reversed)


# Hamming Distance
def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    if len(str1) != len(str2):
        return None

    hamming_dist = 0

    for i_char, _ in enumerate(str1):
        if str1[i_char] != str2[i_char]:
            hamming_dist += 1

    return hamming_dist
