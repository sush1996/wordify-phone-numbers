'''
utils.py contains all the functions that help shorten the main code or methods that are used commonly

Functions in utils.py:

1. split_number()
2. fix_hyphenation()
3. convert_to_format()
4. extract_substrings()
5. comb_perm()
6. get_substrings_combos()
7. get_desired_wordifications()
8. size_longest_substr()
9. check_if_single_alpha()
10. keypad()
'''


'''   
Function: split_number()

Function Design:

US phone number formats taken into consideration when splitting: 

0. +1xxxxxxxxxxx, 1xxxxxxxxxxx, xxxxxxxxxx

1.1.  +1xxx-xxxxxxx, 1xxx-xxxxxxx, xxx-xxxxxxx, xxxxxx-xxxx, +1xxxxxxx-xxxx, 1xxxxxx-xxxx
1.2.  1-xxxxxxxxxx, +1-xxxxxxxxxx

2.1.  +1xxx-xxx-xxxx, 1xxx-xxx-xxxx, xxx-xxx-xxxx,
2.2.  1-xxx-xxxxxxx, +1-xxx-xxxxxxx

3. +1-xxx-xxx-xxxx, 1-xxx-xxx-xxxx    
'''

def split_number(number): #type(number) : string, can be alphanumeric or can include special characters
	
	# account for different styles of writing a phone number
	# retain format for the unwordified part of the the number

	if '-' not in number:
		
		# accounts for all number formats in 0.
		if number[0] == '1':
			start_ind = 1
		elif number[0] == '+':
			start_ind = 2
		else:
			start_ind = 0

		unwordified_num = number[:start_ind]                                               # "+1" / "1" 
		num_to_wordify = number[start_ind:]                                                # "xxxxxxxxxx"

	else:
		number_list = number.split('-')
		
		if len(number_list) == 2:
			
			# accounts for all number formats in 1.1
			if len(number_list[0]) > 2 and number_list[0][0] == '1':
				unwordified_num = number_list[0][:1]                                       # "+1/1"
				num_to_wordify = number_list[0][1:] + number_list[1]                       # "xxx" + "xxxxxxx"
															  
			elif len(number_list[0]) > 2 and number_list[0][0] == '+':
				unwordified_num = number_list[0][:2]                                       # "+1/1"
				num_to_wordify = number_list[0][2:] + number_list[1]                       # "xxx" + xxxxxxx"
			
			elif len(number_list[0]) > 2 and number_list[0][0] not in '+1':
				unwordified_num = number_list[0][:2]                                      # "+1/1"
				num_to_wordify =  number_list[0][2:] + number_list[1]                      # "xxx" + xxxxxxx"
			
			# accounts for all number formats in 1.2
			elif len(number_list[0]) <= 3:
				unwordified_num = number_list[0] + "-"                                     # "+1/1" + "-" 
				num_to_wordify = number_list[1]                                            # "xxxxxxxxxx"
			
		elif len(number_list) == 3:
			
			# accounts for all number formats in 2.1
			if len(number_list[0]) > 2 and number_list[0][0] == '1':
				unwordified_num = number_list[0][:1]                                       # "1"
				num_to_wordify = number_list[0][1:] + number_list[1] + number_list[2]      # "xxx" + "xxx" + "xxxx"
															  
			elif len(number_list[0]) > 2 and number_list[0][0] == '+':
				unwordified_num = number_list[0][:2]                                       # "+1"
				num_to_wordify = number_list[0][2:] + number_list[1] + number_list[2]      # "xxx" + "xxx" + "xxxx"
			
			# accounts for all number formats in 2.2
			elif len(number_list[0]) < 3:
				unwordified_num = number_list[0] + "-"                                     # "+1/1" + "-"
				num_to_wordify = number_list[1] + number_list[2]                           # "xxx" + "xxxxxxx"
			
			elif len(number_list[0]) == 3:
				unwordified_num = ""                                                       # "" 
				num_to_wordify = number_list[0] + number_list[1] + number_list[2]          # "xxx" + "xxx" + "xxxx"
			
		# accounts for all number formats in 3.
		elif len(number_list) == 4:                                                 
			unwordified_num = number_list[0] + "-"                                         # "+1/1" + "-"
			num_to_wordify = number_list[1] + number_list[2] + number_list[3]              # "xxx" + "xxx" + "xxxx"

	# unwordified_num: string with both alphabetical and non-alphabetical characters
	# num_to_wordify: alphanumeric string
	return unwordified_num, num_to_wordify   


'''
Function: fix_hyphenation()

Function Design:

1. each sub-word should be contained within hyphens
2. xxx-[xxx]-xxxx : middle-structure, xxx-xxx-[xxxx] : end-structure ([] -  indicates the part of the format under consideration)

  - if the length of the sub-word exceeds middle-structure length, then continue the sub-word in end-structure without hyphenation
  - if the length of the sub-word is less than the length of either structure length, then hyphenate within the structure   
  - maintain the middle and end structure if the above two conditions are not valid
'''

# alphanumeric string (without special characters) and should only be part of the 
# phone number that needs to be wordified (i.e last 10 characters of the US phone number), 
# alphanumeric_string format: xxxxxxxxxx (x will be alphanumerical)


# ** hardcoded the rules for this method on a case by case basis, there might be some tiny errors
# ** come up with a more elegant solution
def fix_hyphenation(alnum_str): #type(alnum_str) : string which can contain only alphabetical and numrical characters 
	
	word_count = num_count = 0
	final_result = ""

	for ind, num_char in enumerate(alnum_str):
		
		# to maintain end structure
		if ind == len(alnum_str)-4 and num_char.isnumeric():
			final_result = final_result + '-'			
	
		if not num_char.isnumeric():
			if num_count > 0:
			   final_result = final_result + "-"
			
			num_count = 0
			final_result = final_result + num_char
			word_count += 1
	
		elif num_char.isnumeric():
			if ind > 0 and word_count > 0:
				final_result = final_result + "-" 	
			
			final_result = final_result + num_char
			num_count += 1
			
			if (ind == 2 and word_count > 0 and num_count == 1):
			   final_result = final_result + "-"
			   num_count = 0  
			
			word_count = 0
			
			# to maintain all structures
			if (num_count == 3 or num_count == 6) and ind < len(alnum_str)-4:
				final_result = final_result + "-"

	# 'replace' only replaces the first instance and we have a
	#  maximum of 2 such instances for any string so we use it twice
	final_result = final_result.replace("--", "-")
	final_result = final_result.replace("--", "-")
	
	return final_result   

'''
Function: convert_to_format()

Function Design:

convert a desired string to a format of your choice, formats commonly used are as found in 0, 1.1, 1,2, 2,1, 2,2, 3
in split_number design.
'''

# wordified_string may contain non-alphanumeric characters

def convert_to_format(wordified_string, number_format): # type(wordified_string): string, type(format): string

	wordified_list = list(wordified_string)
	i = j = 0

	while i < len(wordified_list) and j < len(number_format):
		
		# deals with cases where number_format has more non-alphanumeric characters than wordified_string
		if wordified_list[i].isalnum() and number_format[j].isalnum() == False or number_format[j] == '1':   
			wordified_list.insert(i, number_format[j])	
		
		# deals with cases where wordified_string has more non-alphanumeric characters than number_format
		elif wordified_list[i].isalnum() == False and number_format[j].isalnum():
			wordified_list.pop(i)
		
		i += 1
		j += 1

	return ''.join(char for char in wordified_list)


'''
Function: extract_substrings()

Function Design:

- Iterate through the alphanumerical string and keep the track of all the sub-words
- Sub-words are any consecutive set of alphabets or even just a single alphabet
'''

def extract_substrings(string):   # string can contain special, numerical and alphabetical characters
	string_list, words_set = [], set()

	temp_word, temp_num = "", ""
	
	for char in string:
		
		if char.isalpha():
			if temp_num != "":
				string_list.append(temp_num)
				temp_num = ""
			
			temp_word = temp_word + char 			
		
		else:
			if temp_word != "":
				string_list.append(temp_word)         
				words_set.add(temp_word)
				temp_word = ""
			
			temp_num = temp_num + char                             
	
	if temp_num != '':
		string_list.append(temp_num) 
	
	else:
		string_list.append(temp_word)
		words_set.add(temp_word)

	# return both a set and a list
	# set is used for checking in the dictionary - optimiation
	# set is not ordered so a list is also generated to preserve the order during final wordification
	return string_list, words_set 


'''
Function: comb_perm()

Function Design

A dictionary with the key as the length of the parent string and the value being a list of combinations of sub-lengths that add up
to the length of the parent word.
This comes in handy when word combinations for sub-words need to be generated.

'''
def comb_perm():
	'''
	num_comb, num_perm = [2,2,2,2,2,3,3,3,4,4,5,5,6,7,8], [2,2,3,3,4,4,5,6,7,8]
	comb_perm_dict = dict()

	for i in range(4, max_l+1):
		combs = [seq for j in range(len(num_comb), 0, -1) for seq in combinations(num_comb, j) if sum(seq)==i and len(seq)!=1]
		perms = [seq for j in range(len(num_perm), 0, -1) for seq in permutations(num_perm, j) if sum(seq)==i and len(seq)!=1]
		
		string_lengths = list(set(perms+combs))
		comb_perm_dict[i] = string_lengths
	'''
	# Used the above piece of code to generate the below dictionary
	
	# Computationally very expensive to generate permutations, so I've hardcoded the 
	#   set of permutations and combinations into a dictionary.
	
	# Only interested in combinations with length > 4 
	
	# key: string length
	# value: list of sub-lengths > 1 (not interested in length 1 sub-words) which add upto to the string length (key)

	comb_perm_dict = {	4: [(2, 2)],
					 	
					 	5: [(3, 2), (2, 3)],
					  	
					  	6: [(4, 2), (2, 2, 2), (2, 4), (3, 3)], 
						
						7: [(2, 3, 2), (5, 2), (3, 2, 2), (2, 5), (4, 3), (2, 2, 3), (3, 4)], 
						
						8: [(4, 2, 2), (2, 6), (3, 3, 2), (2, 2, 2, 2), (2, 2, 4), (2, 3, 3), 
						   (4, 4), (2, 4, 2), (6, 2), (5, 3), (3, 2, 3), (3, 5)],
						
						9: [(2, 7), (3, 3, 3), (5, 4), (2, 2, 5), (2, 4, 3), (4, 5), (2, 2, 2, 3), (4, 3, 2),
						   (6, 3), (4, 2, 3), (5, 2, 2), (3, 6), (3, 4, 2), (2, 3, 4), (2, 5, 2), (7, 2), (3, 2, 4)],
						
						10:[(2, 3, 5), (7, 3), (2, 3, 3, 2), (2, 8), (4, 3, 3), (2, 2, 2, 2, 2), (3, 7), (3, 4, 3),
						   (5, 2, 3), (5, 5), (3, 2, 2, 3), (2, 3, 2, 3), (3, 3, 4), (6, 2, 2), (2, 4, 4), (2, 5, 3),
						   (6, 4), (2, 6, 2), (8, 2), (2, 2, 3, 3), (2, 2, 6), (2, 2, 2, 4), (5, 3, 2), (3, 5, 2),
						   (3, 2, 3, 2), (4, 2, 4), (3, 2, 5), (4, 6), (3, 3, 2, 2), (4, 4, 2)]
					}

	return comb_perm_dict


'''
Function: get_substring_combos()

Functions Design:

To generate the sub-strings based on the combinations. The need fot this functions is shown by an example below:

eg. consider the subword PAINTER - while the word itself belongs to the dictionary but its constituent splits may also belong in
    the dictionary:
	
	Length of parent string: PAINTER = 7
	Combinations of lengths of substrings would be: [(2, 3, 2), (5, 2), (3, 2, 2), (2, 5), (4, 3), (2, 2, 3), (3, 4)]
	Generated sub-strings would be: [PA-INT-ER, PAINT-ER, PAI-NT-ER, PA-INTER, PAIN-TER, PA-IN-TER, PAI-NTER]
	Sub-strings present in dictionary: [PA-INT-ER, PAINT-ER, PA-INTER, PA-IN-TER]

'''
def get_substring_combos(subword, combos_dict): # type(subword): string, type(combos_dict): dictionary
	set_substrings, list_substrings = [], []
	
	string_lengths = combos_dict[len(subword)]  # gets the list of all possible combinations summing to a particular length
	for tup in string_lengths:
		temp_list = [0]	
		
		for element in tup:
			temp_list.append(temp_list[-1] + element)
		
		temp_substrings_list, temp_substrings_set = [], set()
		
		# generate sub-strings based on the all the possible combinations
		for i, j in zip(temp_list[:-1], temp_list[1:]):
			temp_substrings_set.add(subword[i:j])
			temp_substrings_list.append(subword[i:j])
		
		set_substrings.append(temp_substrings_set)
		list_substrings.append(temp_substrings_list)

	# return both a set and a list
	# set is used for checking in the dictionary - optimiation
	# set is not ordered so a list is also generated to preserve the order during final wordification 
	return set_substrings, list_substrings


'''
Function: get_desired_wordifications()

Function Design:

Generates all possible combinations of sub-words that may be present in the dictionary.

Criteria to invoke get_substring_combos():

i.   if all the subwords (with len <4 or with len >=4) in the string are present in a dictionary
		- we do this for including the possibility that, if the subword (with len >=4) is present then its combinations of
		  continguous splits may also be present (check example in get_substrings_combos() above)
		eg: MATEOP - Not a valid word but MAY and TOP are.

ii.  if all the subwords (with len <4) are present in the dictionary and subwords (with len >=4) is NOT present in the dictionary
		- we do this for including the possibility that, if the subword (with len >=4) is not present then its combinations of
		 contiguous splits may be present (check example in get_substrings_combos() above)

iii. if all subwords (with len <4) are present in the dictionary then DO NOT invoke the function
iv.  if any subwords (with len <4) is NOT present in the dictionary then DO NOT invoke the function
'''

# string, can also contain special characters
# dictionary: is the reference manual for word validity
# combos_dict: dictionary (hashmap) of lengths and their combinations

def get_desired_wordifications(string, dictionary, combos_dict):  
	string_list, words_set = extract_substrings(string)
	list_of_substrs = [] # should finally contain all possible valid wordififed numbers 
	
	reference = string_list.copy()
	temp_reference = string_list.copy()

	# check if all subwords is present in the dicitonary
	all_flag = all(word in dictionary for word in words_set)
	
	# check if all the subwords with length less than 4 is present in the dictionary
	small_all_flag = all(word in dictionary for word in words_set if len(word)<4)
	
	# check if any subword with length greater than equal to 4 belongs is present in the dictionary
	big_any_flag = any(len(word)>=4 and word not in dictionary for word in words_set)
	
	# accounting for conditions i, ii, iii and iv for deciding the wordified numbers
	if all_flag or (small_all_flag and big_any_flag):                           # criteria i, ii, iv
		if all_flag:
			list_of_substrs.append(''.join(element for element in string_list))	# criteria iii

		for word in words_set:
			if len(word) >= 4:   #criteria i and ii
				
				sub_strings_set, sub_strings_list = get_substring_combos(word, combos_dict)
				
				for sub_set, sub_list in zip(sub_strings_set, sub_strings_list):
					if sub_set.issubset(dictionary):
						
						new_substr = '-'.join(element for element in sub_list)
						temp_reference[reference.index(word)] = new_substr
						list_of_substrs.append(''.join(element for element in temp_reference))
	
	
	return list_of_substrs


'''
Function: size_longest_substr()

Function Design:

return the count of the largest number of consecutive alphabets in the string
'''

def size_longest_substr(alnum_str):  # type(alnum_str) : string, should contain only alphanumeric characters
	
	count, prev = 0, 0
	max_count = 0
	for i, char in enumerate(alnum_str):
		if char.isalpha() or (char.isalpha() and not alnum_str[i+1].isnumeric() and alnum_str[i+2].isalpha()):
			count += 1
		
		# give preference for contiguous alphabets without hyphens 
		if char == "-":
			count = count -0.1
		
		elif char.isnumeric():
			max_count = max(max_count, count)
			count = 0
	
	max_count = max(max_count, count)	
	
	return max_count

'''
Function: check_if_single_alpha

Function Design:

return 1 if there is a lone alphabet in the string

Criteria:

i.   if a single alphabetical character resides in between two non-alphabetical characters
ii.  if the string starts with an alphabetical character but immediately has a non-alphabetical character next to it
iii. if the string ends with an alphabetical character and it succeeded an non-alphabetical character 
'''

def check_if_single_alpha(alnum_str):        # type(alphanumeric_string) : string, should contain only alphanumeric characters
	
	n = len(alnum_str)-1
	
	if alnum_str[0].isalpha() and not alnum_str[1].isalpha():      # criteria ii 
		return 1
	elif alnum_str[-1].isalpha() and not alnum_str[n-1].isalpha(): # criteria iii
		return 1

	# criteria i 
	for i in range(1, n) :
		if not alnum_str[i-1].isalpha() and not alnum_str[i+1].isalpha() and alnum_str[i].isalpha() :
			return 1 
	return 0


'''
Function: keypad()

Function Design:

returns a hard-coded dictionary for enabling conversion from number to words and vice-versa
'''

def keypad():
	
	# dictionary to relate numbers with its associated letters (referred to mobile phone keypad)
	num_word_dict = {'1':['1'],'2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
					 '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

	word_num_dict = {'1':'1','A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4','H':'4','I':'4','J':'5','K':'5','L':'5',
					 'M':'6','N':'6','O':'6','P':'7','Q':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9',
					 'X':'9','Y':'9','Z':'9','0':'0'}
	
	return num_word_dict, word_num_dict
