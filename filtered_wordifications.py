'''
Results from all_wordifications are filtered down to meaningful words by making use of a dictionary created using create_dictionary
Same code structure as all_wordifications.py but incorporates a dictionary to only take dictionary words into account.
'''

import time
import itertools
from utils import *

def filtered_wordifications(number, dictionary): # type(number) : string, type(dictionary) : string, dcitonary should be a filename or filepath 
    num_word_dict, _ = keypad()        # fetches us the dictionary needed for converting numbers to words

    # account for different styles of writing a phone number
    # retain format for the unwordified part of the the number

    if '-' not in number:
        
        # accounts for all number formats in 0.
        if number[0] == '1':
            start_ind = 4
        elif number[0] == '+':
            start_ind = 5
        else:
            start_ind = 3

        unwordified_num = number[:start_ind]
        num_to_wordify = number[start_ind:]

    else:
        number_list = number.split('-')

        # accounts for all number formats in 1.
        if len(number_list) == 2:
            if len(number_list[0]) <= 2:                                                  
                unwordified_num = number_list[0] + "-" + number_list[1][:3]
                num_to_wordify = number_list[1][3:]
            else:
                unwordified_num = number_list[0] + "-"
                num_to_wordify = number_list[1]

        # accounts for all number formats in 2.
        elif len(number_list) == 3:
            unwordified_num = number_list[0] + "-"
            num_to_wordify = number_list[1] + number_list[2]
        
        # accounts for all number formats in 3.
        elif len(number_list) == 4:                                                 
            unwordified_num = number_list[0] + "-" + number_list[1] + "-"
            num_to_wordify = number_list[2] + number_list[3]
        
    nums_letters_list = []

    for num in num_to_wordify:
        nums_letters_list.append([num] + num_word_dict[num])  # create the set of input lists to be used for itertools.product

    wordified_nums_lists = list(itertools.product(*nums_letters_list))  # itertools.product creates a cartesian product of all the input lists

    filtered_wordified_numbers = []
    start = time.time()
    
    # filtered Combinations
    dictionary = open(dictionary).readlines()
    dictionary = list(map(lambda line: line.strip('\n'), dictionary))

    wordified_nums_lists = wordified_nums_lists[1:]     # the number itself will be included since it's a valid combination, but we don't need it

    for word_list in wordified_nums_lists:
        wordfied_num = "".join(char for char in word_list)
        list_of_subwords = extract_string(wordfied_num)     # extract_string fetches the sub-words available in an alphanumerical string

        flag = 0
        
        # if the wordfified number has multiple sub-words, then we consider the number if and only if all the sub-words are a part of the dictionary
        for sub_word in list_of_subwords:
            if sub_word not in dictionary:		
                flag = 1
                break

        if flag == 0:
            temp_var = unwordified_num + fix_hyphenation_all(wordfied_num)
            filtered_wordified_numbers.append(temp_var)

    # we sort the results in the order of increasing number of '-', this would put the longer wordified numbers in front of the list
    filtered_wordified_numbers = sorted(filtered_wordified_numbers, key=lambda number: number.count('-')) 
    end = time.time()

    print(end-start)
    print(len(filtered_wordified_numbers))
    return filtered_wordified_numbers      # type(all_wordified_numbers) : list of strings

print(filtered_wordifications('1-800-724-6837', '20k_final_dictionary.txt'))

'''
Input: 1-800-724-6837

Output: 

Sample results:

['1-800-PAINTER', '1-800-724-OVER', '1-800-72-INTER', '1-800-PAIN-837', '1-800-PAINT-37', '1-800-PCG-6837', '1-800-PCI-6837',
 '1-800-RAG-6837', '1-800-RAI-6837', '1-800-RAIN-837', '1-800-RBI-6837', '1-800-SAINT-37', '1-800-SBIN-837', '1-800-SCH-6837',
 '1-800-SCI-6837', '1-800-724-68-DP', '1-800-724-68-DQ', '1-800-724-68-DR', '1-800-724-68-DS', '1-800-724-68-EP', '1-800-724-68-EQ',
 '1-800-724-68-ER', '1-800-724-68-ES', '1-800-724-68-FP', '1-800-724-68-FR', '1-800-724-68-FS', '1-800-724-6-TDS', '1-800-724-6-TER',
 '1-800-724-6-TES', '1-800-724-6-UDP', '1-800-724-6-VER', '1-800-724-MT-37', '1-800-724-MU-37', '1-800-724-MUD-7', '1-800-724-MV-37',
 '1-800-724-NT-37', '1-800-724-NU-37', '1-800-724-NV-37', '1-800-724-OT-37', '1-800-724-OU-37', '1-800-724-OV-37', '1-800-72-GM-837',
 '1-800-72-GMT-37', '1-800-72-GN-837', '1-800-72-GNU-37', '1-800-72-GO-837', '1-800-72-GOT-37', '1-800-72-GOV-37', '1-800-72-HM-837', 
 '1-800-72-HN-837', '1-800-72-HO-837', '1-800-72-HOT-37', '1-800-72-IM-837', '1-800-72-IN-837', '1-800-72-INT-37', '1-800-72-IO-837', ...]

Number of combinations: 1093

Time taken: 2.95
'''

'''
Completed
1. Take care of hyphenating the results
2. Find publicly available english words dictionary to create only useful/desireable wordified-numbers 
3. Filter results of all_wordifications based on a dictionary 
4. Design hyphenation for the filtered results (was not needed)

Next Steps: 
5. Consider designing test cases to validate results
6. Make code more efficient, very slow!
'''