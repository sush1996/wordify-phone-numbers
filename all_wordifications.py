#US phone numbers can only start from a number between 2-9
#US phone number formats: +1-xxx-xxx-xxxx, 1-xxx-xxx-xxxx, xxx-xxx-xxxx, xxxxxxxxxx, +1xxxxxxxxxxx, 1xxxxxxxxxxx   
#def number_to_words(us_phone_number): #type(us_phone_number): string

import itertools
import timeit
import numpy as np

number = "+1-800-724-6837"

#Dictionary to relate numbers with its associated letters (referred to mobile phone keypad)
num_word_dict = {'2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
                 '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

#Account for different styles of writing a phone number
try:
    #Accounts for numbers with '-'
    number_list = number.split('-') 
    unwordified_num = number_list[0] + "-" + number_list[1] + "-"
    num_to_wordify = number_list[2] + number_list[3]
except:
    #Accounts for numbers without '-'
    if number[0] == '1':
        start_ind = 1
    elif number[0] == '+':
        start_ind = 2
    else:
        start_ind = 0

    unwordified_num = number[:start_ind]
    num_to_wordify = number[start_ind:]

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

All possible combinations:
[['+18007246837']
 ['+1800724683P']
 ['+1800724683Q']
 ...
 ['+1V00SCIOVFQ']
 ['+1V00SCIOVFR']
 ['+1V00SCIOVFS']]

Number of combinations
409600

Time taken for execution
0.4107859469950199
'''

'''
Next Steps: 
1. Take care of hyphenating the results
2. Find publicly available english words dictionary to create only useful/desireable wordified-numbers 
'''