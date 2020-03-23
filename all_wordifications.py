'''
US phone numbers can only start from a number between 2-9 (excluding +1)

US phone number formats taken into consideration: 
0. +1xxxxxxxxxxx, 1xxxxxxxxxxx, xxxxxxxxxx
1. +1-xxxxxxxxxxx, +1xxx-xxxxxxx, 1xxx-xxxxxxx
2. +1xxx-xxx-xxxx, 1xxx-xxx-xxxx, xxx-xxx-xxxx
3. +1-xxx-xxx-xxxx, 1-xxx-xxx-xxxx  
   
'''

#def number_to_words(us_phone_number): #type(us_phone_number): string

import itertools
import timeit
import numpy as np

number = "1-800-724-6837"

#Dictionary to relate numbers with its associated letters (referred to mobile phone keypad)
num_word_dict = {'2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
                 '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

#Account for different styles of writing a phone number
#Only perform formatting for the unwordified part of the the number

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

start = timeit.default_timer()
wordified_nums_lists = list(itertools.product(*nums_letters_list)) #itertools.product creates a cartesian product of all the input lists

all_wordified_numbers = []

for word_list in wordified_nums_lists:
    temp_var = unwordified_num + "".join(char for char in word_list) #Appending the un-wordified part of the phone number to the wordified part
    all_wordified_numbers.append(temp_var)

end = timeit.default_timer()

print(np.array(all_wordified_numbers).reshape(-1,1))
print(len(all_wordified_numbers))
print(end-start)

'''
Input: +1-800-724-6837

Output: 

All combinations:

[['1-800-7246837']
 ['1-800-724683P']
 ['1-800-724683Q']
 ...
 ['1-800-SCIOVFQ']
 ['1-800-SCIOVFR']
 ['1-800-SCIOVFS']]

Number of combinations: 25600

Time taken: 0.035845832026097924
'''

'''
Next Steps: 
1. Take care of hyphenating the results
2. Find publicly available english words dictionary to create only useful/desireable wordified-numbers 
'''