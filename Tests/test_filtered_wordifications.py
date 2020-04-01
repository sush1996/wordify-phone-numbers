import os, sys
sys.path.append(os.path.abspath(".."))

from words_to_number import *
from Utils.filtered_wordifications import filtered_wordifications
from Utils.utils import extract_substrings

# First layer of testing involves converting a wordified number back to its number equivalent
# and then checking if the conversion matches the original number

original_number = "1-800-724-6837"
dictionary = "../Utils/words_alpha_mod.txt"

wordified_nums = filtered_wordifications(original_number, dictionary)

for word in wordified_nums:
	generated_num = words_to_number(word, original_number)
	assert generated_num == original_number

print("Passing all test cases for converting the wordified number to its original number")

# Second layer involves checking if the word or the all subwords of the wordified string
# belong in the dictionary 

dictionary_set = open(dictionary).readlines()
dictionary_set = set(map(lambda line: line.strip('\n'), dictionary_set)) 

for word in wordified_nums:
	_, words_set = extract_substrings(word)
	assert words_set.issubset(dictionary_set)

print("Passing all test cases for checking if the set of subwords belong in the dictionary")

