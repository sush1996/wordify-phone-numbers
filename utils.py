'''
Design:

1. each sub-word should be contained within hyphens
2. xxx-[xxx]-xxxx : middle-structure, xxx-xxx-[xxxx] : end-structure ([] -  indicates the part of the format under consideration)

  - if the length of the sub-word exceeds middle-structure length, then continue the sub-word in end-structure without hyphenation
  - if the length of the sub-word is less than the length of either structure length, then hyphenate within the structure   
 
'''

# alphanumeric string (without special characters) and should only be part of the 
# phone number that needs to be wordified (i.e last 7 characters of the US phone number)

def fix_hyphenation(alphanumeric_string): 
	
	word_count = num_count = 0
	final_result = ""

	for ind, num_char in enumerate(alphanumeric_string):
	    if num_char.isalpha():
	        if num_count > 0:
	           final_result = final_result + "-"
	    	
	        num_count = 0
	        final_result = final_result + num_char
	        word_count += 1
	    
	    else:
	        if ind > 0 and word_count > 0 or ind == 3:
	           final_result = final_result + "-"  	
	    	
	        word_count = 0
	        final_result = final_result + num_char
	        num_count += 1

	return final_result

'''
Design:

Iterate through the alphanumerical string and keep the track of all the sub-words

Sub-words are any consecutive set of alphabets or even just a single alphabet
'''

def extract_strings(alphanumeric_string):
	list_of_strings = []
	temp_string = ""

	for char in alphanumeric_string:
		
		if char.isalpha():
			temp_string = temp_string + char 			# append consecutive characters to form a string and store it in a temporary variable 
		
		elif char.isnumeric() and temp_string != '':
			list_of_strings.append(temp_string)         # append the fully-formed sub-word to a list
			temp_string = ""                            # reset temporary variable to include the next sub-word

	# Accounting for a sub-word that may occur at the end of the string
	# if there is no sub-word at the end of the string, it will contain a ''	                                                    
	list_of_strings.append(temp_string)                    
    
    # we don't need the '' in our return
	return list_of_strings[:-1] if list_of_strings[-1] == '' else list_of_strings

def count_alphabets(alphanumeric_string):
	count = 0
	for char in alphanumeric_string:
		if char.isalpha():
			count += 1
	return count
	
def keypad():
	# dictionary to relate numbers with its associated letters (referred to mobile phone keypad)
    num_word_dict = {'2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
                     '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

    word_num_dict = {'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4','H':'4','I':'4','J':'5','K':'5','L':'5',
                     'M':'6','N':'6','O':'6','P':'7','Q':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9',
                     'X':'9','Y':'9','Z':'9','0':'0'}
    
    return num_word_dict, word_num_dict