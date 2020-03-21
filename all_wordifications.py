#US phone number format: +1-xxx-xxx-xxxx
#def number_to_words(us_phone_number): #type(us_phone_number): string
import itertools
import timeit
import numpy as np

number = "+1-800-724-6837"

num_word_dict = {'2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
                 '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

try:
    number = number.split('-')
    starting_num = number[0] + "-" + number[1] + "-"
    num_to_wordify = number[2] + number[3]
except:
    starting_num = number[0:3]
    num_to_wordify = number[3:]


list_num_letters = []
for i in num_to_wordify:
    list_num_letters.append([i] + num_word_dict[i])

start = timeit.default_timer()
res = list(itertools.product(*list_num_letters))

all_numbers = []

for i in res:
    temp_var = starting_num + "".join(char for char in i)
    all_numbers.append(temp_var)
end = timeit.default_timer()


print(np.array(all_numbers).reshape(-1,1))
print(len(res))
print(end-start)

#Input: +1-800-724-6837
#Output: 
'''
#All possible combinations
[['+1-800-7246837']
 ['+1-800-724683P']
 ['+1-800-724683Q']
 ...
 ['+1-800-SCIOVFQ']
 ['+1-800-SCIOVFR']
 ['+1-800-SCIOVFS']]
#Number of combinations
25600
#Time taken for execution
0.02312120099668391
''' 