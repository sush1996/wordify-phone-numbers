'''
Function: words_to_number(), 

Function Design:

does the reverse of number_to_words (for example, the output of words_to_number("1-800-PAINTER") should be "1-800-724-6837")
'''

from utils import keypad, convert_to_format

# The function takes in the wordified number and your desired number format as the template
# and converts the wordified number to the desired format.

# The number_format has to have the same number of alphanumerical characters as your wordified number 

def words_to_number(wordified_num, number_format): # type(wordified_num) : string, type(number_format) : string
	
	word_num_count = sum([1 for char in wordified_num if char.isalpha()])
	number_num_count = sum([1 for char in number_format if char.isalpha()])


	_, word_num_dict = keypad()                

	numerized_word = ""
	
	for char in wordified_num:
		if char.isalpha():
			numerized_word = numerized_word + word_num_dict[char]  # if char is an alphabet, then convert it to its numerical counterpart
		else:
			numerized_word = numerized_word + char                 # if char is a number, then just append it as it is

	return convert_to_format(numerized_word, number_format)