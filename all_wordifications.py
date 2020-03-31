'''
Function: all_wordifications()

Function Design: 

which outputs all possible combinations of numbers and English words in a given phone number.
'''

import itertools
from Utils.utils import *

# number = "1-800-724-6837"

def all_wordifications(number):  # type(number) : string

    # US phone numbers can only start from a number between 2-9 (excluding +1 part of the number)
    num_word_dict, _ = keypad() 

    unwordified_num, num_to_wordify = split_number(number) 
    nums_letters_list = []

    for num in num_to_wordify:
        nums_letters_list.append([num] + num_word_dict[num])  # create the set of input lists to be used for itertools.product

    wordified_nums_lists = list(itertools.product(*nums_letters_list)) # itertools.product creates a cartesian product of all the input lists

    all_wordified_numbers = set([])

    # all combinations
    for word_list in wordified_nums_lists:
        word_string = "".join(char for char in word_list)
        temp_var = unwordified_num + fix_hyphenation(word_string)   # appending the un-wordified part of the phone number to the wordified part
        all_wordified_numbers.add(temp_var)

    return all_wordified_numbers   # type(all_wordified_numbers) : list of strings