'''
Function: number_to_words()

Function Design:

takes as an argument a string representing a US phone number and which outputs a string which has transformed
part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone 
(for example, a valid output of number_to_words("1-800-724-6837") could be"1-800-PAINTER"). If you find it makes
things simpler, feel free to constrain this function to only output "wordifications" in English.
'''

from Utils.filtered_wordifications import filtered_wordifications

# number = "1-800-724-6837"
# dictionary = "final_dictionary.txt", "20k_final_dictionary.txt", "words_alpha_mod" - gives most sensible and concise results "

def number_to_words(number, dictionary): # type(number) : string, type(dictionary) : string, dictionary should be a filename or filepath

	# use the top result generated by filtered_wordifications as suggestion for wordififcation
	return filtered_wordifications(number, dictionary)[0]