'''
Results from all_wordifications are filtered down to meaningful words by making use of a dictionary created using create_dictionary
Same code structure as all_wordifications.py but incorporates a dictionary to only take dictionary words into account.

Results are highly dependent on the dictionary that is used to filter the words.
I've chosen to incorporate a big dictionary by documenting a set of other smaller dictionaries 

Current content in 'dictionaries' folder
1. 20k.txt :    https://github.com/first20hours/google-10000-english/blob/master/20k.txt
2. words.txt :  https://github.com/dwyl/english-words/blob/master/words.txt

create_dictionary() in utils.py outputs final_dictionary.txt or 20k_final_dictionary.txt
'''

import itertools
from utils import *

# number = "1-800-724-6837"
# dictionary = "final_dictionary.txt" or "20k_final_dictionary.txt"

def filtered_wordifications(number, dictionary): # type(number) : string, type(dictionary) : string, dictionary should be a filename or filepath 
    num_word_dict, _ = keypad()                  # fetches us the dictionary needed for converting numbers to words

    unwordified_num, num_to_wordify = split_number(number)  
    nums_letters_list = []

    for num in num_to_wordify:
        nums_letters_list.append([num] + num_word_dict[num])            # create the set of input lists to be used for itertools.product

    wordified_nums_lists = list(itertools.product(*nums_letters_list))  # itertools.product creates a cartesian product of all the input lists

    # filtered combinations
    dictionary = open(dictionary).readlines()
    dictionary = list(map(lambda line: line.strip('\n'), dictionary))
    dict_of_words = {word for word in dictionary}	             # optimization: put the list of words in a hashmap, allows for much faster querying

    wordified_nums_lists = wordified_nums_lists[1:]          # the number itself will be included since it's a valid combination, but we don't need it
	
    filtered_wordified_numbers = []

    for word_list in wordified_nums_lists:
        word_string = "".join(char for char in word_list)
        list_of_subwords = extract_strings(word_string)     # extract_string fetches the sub-words available in an alphanumerical string

        flag = 0
        
        # if the wordfified number has multiple sub-words, then 
        # we consider the number if and only if all the sub-words are a part of the dictionary
        for sub_word in list_of_subwords:
            if sub_word not in dict_of_words:		
                flag = 1                       # indicate presence of sub-words not present in dictionary                  
                break                     # optimization: stop comparing with the dictionary if even a single sub-word in the list fails to match

        if flag == 0:                          # indication that we're good to go ahead and format the wordified number
            temp_var = unwordified_num + fix_hyphenation(word_string)
            filtered_wordified_numbers.append(temp_var)

    # sort the results by the number of alphabets in the wordified number - count_alphabets
    # puts better results at the front of the list than results yielded by sorting on the count of '-'
    # reversing the list ensures we get the longer words  at the front of the list 
    # assumption: longer words are more desireable - not strictly true, but will do for now   
    filtered_wordified_numbers = sorted(filtered_wordified_numbers, key=count_alphabets, reverse=True) 

    return filtered_wordified_numbers      # type(all_wordified_numbers) : list of strings

'''
Input: 1-800-724-6837

Output: 

Sample results:

['1-800-PAINTER', '1-800-7-CINTER', '1-800-PA-4-MUDS', '1-800-PA-4-OTDR', '1-800-PA-4-OTES', '1-800-PA-4-OUDS', '1-800-PA-4-OVER',
 '1-800-PAG-6-TDR', '1-800-PAG-6-TDS', '1-800-PAG-6-TER', '1-800-PAG-6-TES', '1-800-PAG-6-TFP', '1-800-PAG-6-TFR', '1-800-PAG-6-TFS',
 '1-800-PAG-6-UDP', '1-800-PAG-6-UDR', '1-800-PAG-6-UDS', '1-800-PAG-6-UFS', '1-800-PAG-6-VER', '1-800-PAG-6-VFR', '1-800-PAG-6-VFS',
 '1-800-PAH-6-TDR', '1-800-PAH-6-TDS', '1-800-PAH-6-TER', '1-800-PAH-6-TES', '1-800-PAH-6-TFP', '1-800-PAH-6-TFR', '1-800-PAH-6-TFS', 
 '1-800-PAH-6-UDP', '1-800-PAH-6-UDR', '1-800-PAH-6-UDS', '1-800-PAH-6-UFS', '1-800-PAH-6-VER', '1-800-PAH-6-VFR', '1-800-PAH-6-VFS', 
 '1-800-PAHO-8-DP', '1-800-PAHO-8-DQ', '1-800-PAHO-8-DR', '1-800-PAHO-8-DS', '1-800-PAHO-8-EP', '1-800-PAHO-8-EQ', '1-800-PAHO-8-ER', 
 '1-800-PAHO-8-ES', '1-800-PAHO-8-FP', '1-800-PAHO-8-FR', '1-800-PAHO-8-FS', '1-800-PAIN-8-DP', '1-800-PAIN-8-DQ', '1-800-PAIN-8-DR', 
 '1-800-PAIN-8-DS', '1-800-PAIN-8-EP', '1-800-PAIN-8-EQ', '1-800-PAIN-8-ER', '1-800-PAIN-8-ES', '1-800-PAIN-8-FP', '1-800-PAIN-8-FR', 
 '1-800-PAIN-8-FS', '1-800-PB-4-MUDS', '1-800-PB-4-OTDR', '1-800-PB-4-OTES', '1-800-PB-4-OUDS', '1-800-PB-4-OVER', '1-800-PC-4-MUDS', 
 '1-800-PC-4-OTDR', '1-800-PC-4-OTES', '1-800-PC-4-OUDS', '1-800-PC-4-OVER', '1-800-PCG-6-TDR', '1-800-PCG-6-TDS', '1-800-PCG-6-TER', 
 '1-800-PCG-6-TES', '1-800-PCG-6-TFP', '1-800-PCG-6-TFR', '1-800-PCG-6-TFS', '1-800-PCG-6-UDP', '1-800-PCG-6-UDR', '1-800-PCG-6-UDS', 
 '1-800-PCG-6-UFS', '1-800-PCG-6-VER', '1-800-PCG-6-VFR', '1-800-PCG-6-VFS', '1-800-PCH-6-TDR', '1-800-PCH-6-TDS', '1-800-PCH-6-TER', 
 '1-800-PCH-6-TES', '1-800-PCH-6-TFP', '1-800-PCH-6-TFR', '1-800-PCH-6-TFS', '1-800-PCH-6-UDP', '1-800-PCH-6-UDR', '1-800-PCH-6-UDS', 
 '1-800-PCH-6-UFS', '1-800-PCH-6-VER', '1-800-PCH-6-VFR', '1-800-PCH-6-VFS', '1-800-PCI-6-TDR', '1-800-PCI-6-TDS', '1-800-PCI-6-TER', 
 '1-800-PCI-6-TES', '1-800-PCI-6-TFP', '1-800-PCI-6-TFR', '1-800-PCI-6-TFS', '1-800-PCI-6-UDP', '1-800-PCI-6-UDR', '1-800-PCI-6-UDS', 
 '1-800-PCI-6-UFS', '1-800-PCI-6-VER', '1-800-PCI-6-VFR', '1-800-PCI-6-VFS', '1-800-QA-4-MUDS', '1-800-QA-4-OTDR', '1-800-QA-4-OTES', 
 '1-800-QA-4-OUDS', '1-800-QA-4-OVER', '1-800-QB-4-MUDS', '1-800-QB-4-OTDR', '1-800-QB-4-OTES', '1-800-QB-4-OUDS', '1-800-QB-4-OVER', ... ]

Number of combinations: 2119

Time taken: 0.075
'''

'''
Completed
1. Take care of hyphenating the results
2. Find publicly available english words dictionary to create only useful/desireable wordified-numbers 
3. Filter results of all_wordifications based on a dictionary 
4. Design hyphenation for the filtered results (was not needed)
6. "Make code more efficient, very slow!" ~ roughly 50 times faster now (used a hashmap instead of a list to store the dictionary)

Next Steps: 
5. Consider designing test cases to validate results

'''