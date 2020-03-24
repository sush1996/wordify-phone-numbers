'''   
all_wordifications(): which outputs all possible combinations of numbers and English
                      words in a given phone number.


US phone number formats taken into consideration: 
0. +1xxxxxxxxxxx, 1xxxxxxxxxxx, xxxxxxxxxx
1. +1-xxxxxxxxxxx, +1xxx-xxxxxxx, 1xxx-xxxxxxx
2. +1xxx-xxx-xxxx, 1xxx-xxx-xxxx, xxx-xxx-xxxx
3. +1-xxx-xxx-xxxx, 1-xxx-xxx-xxxx  
'''

import itertools
from fix_hyphenation import fix_hyphenation_all

#number = "1-800-724-6837"

def all_wordfifications(number):  #type(number) : string

    #Dictionary to relate numbers with its associated letters (referred to mobile phone keypad)
    #US phone numbers can only start from a number between 2-9 (excluding +1 part of the number)
    num_word_dict = {'2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
                     '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

    #Account for different styles of writing a phone number
    #Retain format for the unwordified part of the the number

    if '-' not in number:
        
        #Accounts for all number formats in 0.
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

        #Accounts for all number formats in 1.
        if len(number_list) == 2:
            if len(number_list[0]) <= 2:                                                  
                unwordified_num = number_list[0] + "-" + number_list[1][:3]
                num_to_wordify = number_list[1][3:]
            else:
                unwordified_num = number_list[0] + "-"
                num_to_wordify = number_list[1]

        #Accounts for all number formats in 2.
        elif len(number_list) == 3:
            unwordified_num = number_list[0] + "-"
            num_to_wordify = number_list[1] + number_list[2]
        
        #Accounts for all number formats in 3.
        elif len(number_list) == 4:                                                 
            unwordified_num = number_list[0] + "-" + number_list[1] + "-"
            num_to_wordify = number_list[2] + number_list[3]
        
    nums_letters_list = []

    for num in num_to_wordify:
        nums_letters_list.append([num] + num_word_dict[num])  #Create the set of input lists to be used for itertools.product

    wordified_nums_lists = list(itertools.product(*nums_letters_list)) #itertools.product creates a cartesian product of all the input lists

    all_wordified_numbers = []

    for word_list in wordified_nums_lists:
        wordfied_num = "".join(char for char in word_list)
        temp_var = unwordified_num + fix_hyphenation_all(wordfied_num)   #Appending the un-wordified part of the phone number to the wordified part
        all_wordified_numbers.append(temp_var)

    return all_wordified_numbers
    
'''
Input: 1-800-724-6837

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

'''
Completed
1. Take care of hyphenating the results
2. Find publicly available english words dictionary to create only useful/desireable wordified-numbers 

Next Steps: 
3. Filter results of all_wordifications based on a dictionary 
4. Design hyphenation for the filtered results 
5. Consider designing test cases to validate results
'''