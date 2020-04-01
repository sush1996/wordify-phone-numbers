import os, sys
sys.path.append(os.path.abspath(".."))

from words_to_number import *
from Utils.filtered_wordifications import filtered_wordifications
from all_wordifications import all_wordifications

true_number = "8007246837"

formats = ["+1-800-724-6837", "+1-800-7246837", "+1-800724-6837", "+1-8007246837",
			"+1800-724-6837", "+1800-7246837", "+1800724-6837", "+18007246837",
			"1-800-724-6837", "1800-7246837", "1800724-6837", "18007246837",
			"800-724-6837", "800-7246837", "800724-6837", "8007246837",]

words = ["800-PAINTER","800-PAI-NTER","800-PA-INTER","800-PAIN-TER","800-PA-INT-ER","800-P-A-INTER","800-P-A-I-N-T-E-R","800-PA-IN-TE-R","800-PAINTER",
		"800-PAINT-E-R", "800-PAINTE-R", "800-PAI-NTER", "800-PAINTER", "800-PAINTER", "800-PAINTER"]

# Testing the word to number functionality
for word in words:
	generated_number = words_to_number(word, true_number)
	assert generated_number == true_number

print("Passing all test cases for word to number conversion")

# Testing the convert-to-desired-format functionality of words_to_number
for f in formats:
	for word in words:
		generated_number = words_to_number(word, f)
		assert generated_number == f

print("Passing all test cases for format conversion") 

