'''
Function: all_wordifications()

Function Design: 

which outputs all possible combinations of numbers and English words in a given phone number.
'''

import itertools
from Utils.utils import split_number, fix_hyphenation, keypad

# number = "1-800-724-6837"

def all_wordifications(number):  # type(number) : string

    # US phone numbers can only start from a number between 2-9 (excluding +1 part of the number)
    num_word_dict, _ = keypad() 

    unwordified_num, num_to_wordify = split_number(number) 
    nums_letters_list = []

    for num in num_to_wordify:
        nums_letters_list.append([num] + num_word_dict[num])  # create the set of input lists to be used for itertools.product

    wordified_nums_lists = list(itertools.product(*nums_letters_list)) # itertools.product creates a cartesian product of all the input lists

    all_wordified_numbers = []

    # all combinations
    for word_list in wordified_nums_lists:
        word_string = "".join(char for char in word_list)
        temp_var = unwordified_num + fix_hyphenation(word_string)   # appending the un-wordified part of the phone number to the wordified part
        all_wordified_numbers.append(temp_var)

    return all_wordified_numbers   # type(all_wordified_numbers) : list of strings

'''
Input: "1-800-724-6837"

Output: 

Sample results:

'1-800-SCG-6-UF-7', '1-800-SCG-6-UFP', '1-800-SCG-6-UFQ', '1-800-SCG-6-UFR', '1-800-SCG-6-UFS', '1-800-SCG-6-V-37',
'1-800-SCG-6-V-3-P', '1-800-SCG-6-V-3-Q', '1-800-SCG-6-V-3-R', '1-800-SCG-6-V-3-S', '1-800-SCG-6-VD-7', '1-800-SCG-6-VDP',
'1-800-SCG-6-VDQ', '1-800-SCG-6-VDR', '1-800-SCG-6-VDS', '1-800-SCG-6-VE-7', '1-800-SCG-6-VEP', '1-800-SCG-6-VEQ', '1-800-SCG-6-VER',
'1-800-SCG-6-VES', '1-800-SCG-6-VF-7', '1-800-SCG-6-VFP', '1-800-SCG-6-VFQ', '1-800-SCG-6-VFR', '1-800-SCG-6-VFS', '1-800-SCGM-837', 
'1-800-SCGM-83-P', '1-800-SCGM-83-Q', '1-800-SCGM-83-R', '1-800-SCGM-83-S', '1-800-SCGM-8-D-7', '1-800-SCGM-8-DP', '1-800-SCGM-8-DQ', 
'1-800-SCGM-8-DR', '1-800-SCGM-8-DS', '1-800-SCGM-8-E-7', '1-800-SCGM-8-EP', '1-800-SCGM-8-EQ', '1-800-SCGM-8-ER', '1-800-SCGM-8-ES',
'1-800-SCGM-8-F-7', '1-800-SCGM-8-FP', '1-800-SCGM-8-FQ', '1-800-SCGM-8-FR', '1-800-SCGM-8-FS', '1-800-SCGMT-37', '1-800-SCGMT-3-P', 
'1-800-SCGMT-3-Q', '1-800-SCIOVE-7', '1-800-SCIOVEP', '1-800-SCIOVEQ', '1-800-SCIOVER', '1-800-SCIOVES', '1-800-SCIOVF-7', '1-800-SCIOVFP'

Number of combinations: 25600

Time taken: 0.05711
'''