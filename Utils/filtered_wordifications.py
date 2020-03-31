import itertools
'''
Results from all_wordifications are filtered down to meaningful words by making use of a dictionary created using create_dictionary
Same code structure as all_wordifications.py but incorporates a dictionary to only take dictionary words into account.

Results are highly dependent on the dictionary that is used to filter the words.
I've experimented with different dictionaries and found that "words_alpha_mod.txt" gives nice and conscise results

Current content in 'dictionaries' folder
1. 20k.txt :    https://github.com/first20hours/google-10000-english/blob/master/20k.txt
2. words.txt :  https://github.com/dwyl/english-words/blob/master/words.txt

create_dictionary() in utils.py outputs final_dictionary.txt or 20k_final_dictionary.txt
'''

try:
	from Utils.utils import *
except:
	from utils import *

# number = "1-800-724-6837"
# dictionary = "final_dictionary.txt" or "20k_final_dictionary.txt" or "words_alpha_mod.txt - best results"

def filtered_wordifications(number, dictionary): # type(number) : string, type(dictionary) : string, dictionary should be a filename or filepath 
	num_word_dict, _ = keypad()                  # fetches us the dictionary needed for converting numbers to words
	combos_dict = comb_perm()					 # get the combos dictionary (hashmap)

	unwordified_num, num_to_wordify = split_number(number)  
	nums_letters_list = []

	for num in num_to_wordify:
		nums_letters_list.append([num] + num_word_dict[num])     # create the set of input lists to be used for itertools.product

	# itertools.product creates a cartesian product of all the input lists
	wordified_list = itertools.product(*nums_letters_list)  
	
	# optimization: put the list of words in a set, allows for much faster comparisons 
	# also remove single letter alphabets (plentiful and uninteresting)
	wordified_list = set(filter(lambda x: check_if_single_alpha(x)==0, wordified_list))
	
	dictionary = open(dictionary).readlines()

	# optimization: put the list of words in a set, allows for much faster comparisons
	dictionary = set(map(lambda line: line.strip('\n'), dictionary)) 

	# filter repetitions as it comes, since we're using itertools.product
	# there are boudn to be many redundant combinations
	filtered_wordified_numbers = set([])   

	for word_tup in wordified_list:
		
		word_string = "".join(char for char in word_tup)
		words_list = get_desired_wordifications(word_string, dictionary, combos_dict)     # extract_string fetches the sub-words available in an alphanumerical string
		
		if words_list != []:	
			for sub_word in words_list:
				filtered_wordified_numbers.add(unwordified_num + fix_hyphenation(sub_word))
	
	#filtered_wordified_numbers = list(filtered_wordified_numbers)
	# sort the results by the number of consecutive alphabets in the wordified number - size_longest_str
	# reversing the list ensures we get the longer words  at the front of the list 
	# assumption: longer words are more desireable - not strictly true, but will do for now   
	filtered_wordified_numbers = sorted(filtered_wordified_numbers, key=lambda x: size_longest_substr(x), reverse = True) 

	return filtered_wordified_numbers      # type(all_wordified_numbers) : list of strings
	
