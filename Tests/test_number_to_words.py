import os, sys
sys.path.append(os.path.abspath(".."))

from words_to_number import *
from number_to_words import *

from Utils.filtered_wordifications import filtered_wordifications
from Utils.utils import extract_substrings

# First layer of testing involves checking if the wordification is present in the dictionary

dictionary = "../Utils/words_alpha_mod.txt"
original_number = "1-800-724-6837"
wordified_number = number_to_words(original_number, dictionary)

dictionary_set = open(dictionary).readlines()
dictionary_set = set(map(lambda line: line.strip('\n'), dictionary_set)) 

_, word_set = extract_substrings(wordified_number)
assert word_set.issubset(dictionary_set)
print('Passes test case for presence of the word part of the wordified number in the dictionary')

# Second layer of testing involves checking if the wordified number corresponds to the original number
generated_number = words_to_number(wordified_number, original_number)
assert generated_number == original_number
print("Passes test case for matching the number equivalent of the wordified number wih the original number")