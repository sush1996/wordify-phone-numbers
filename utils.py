'''
utils.py contains all the functions that help shorten the main code or methods that are used commonly

Functions in utils.py:

1. split_number()
2. fix_hyphenation()
3. convert_to_format()
4. extract_strings()
5. count_alphabets()
6. keypad()
'''


'''   
Function: split_number()

Function Design:

US phone number formats taken into consideration when splitting: 

0. +1xxxxxxxxxxx, 1xxxxxxxxxxx, xxxxxxxxxx

1.1.  +1xxx-xxxxxxx, 1xxx-xxxxxxx, xxx-xxxxxxx
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
            start_ind = 4
        elif number[0] == '+':
            start_ind = 5
        else:
            start_ind = 3

        unwordified_num = number[:start_ind]                                   # "+1xxx" / "1xxx" / "xxx" 
        num_to_wordify = number[start_ind:]                                    # "xxxxxxx"

    else:
        number_list = number.split('-')

        if len(number_list) == 2:
            
            # accounts for all number formats in 1.1
            if len(number_list[0]) > 2:                                                  
                unwordified_num = number_list[0] + "-"                         # "+1/1xxx" + "-"
                num_to_wordify = number_list[1]                                # "xxxxxxx"
            
            # accounts for all number formats in 1.2
            else:
                unwordified_num = number_list[0] + "-" + number_list[1][:3]    # "+1/1" + "-" + "xxx" 
                num_to_wordify = number_list[1][3:]                            # "xxxxxxx"
            
        elif len(number_list) == 3:
            
            # accounts for all number formats in 2.1
            if len(number_list[0]) > 2 :
                unwordified_num = number_list[0] + "-"                         # "+1/1xxx" + "-"
                num_to_wordify = number_list[1] + number_list[2]               # "xxx" + "xxxx"
	        
            # accounts for all number formats in 2.2
            else:
                unwordified_num = number_list[0] + "-" + number_list[1] + "-"  # "+1/1" + "-" + "xxx" + "-"
                num_to_wordify = number_list[2]                                # "xxxxxxx"
	            
        # accounts for all number formats in 3.
        elif len(number_list) == 4:                                                 
            unwordified_num = number_list[0] + "-" + number_list[1] + "-"      # "+1/1" + "-" + "xxx" + "-"
            num_to_wordify = number_list[2] + number_list[3]                   # "xxx" + "xxxx"
    
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
 
'''

# alphanumeric string (without special characters) and should only be part of the 
# phone number that needs to be wordified (i.e last 7 characters of the US phone number), 
# alphanumeric_string format: xxxxxxx (x will be alphanumerical)

def fix_hyphenation(alphanumeric_string): #type(alphanumeric_string) : string 
	
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
Function: extract_string()

Function Design:

- Iterate through the alphanumerical string and keep the track of all the sub-words
- Sub-words are any consecutive set of alphabets or even just a single alphabet
'''

def extract_strings(alphanumeric_string):  # type(alphanumeric_string) : string, should contain only alphanumeric characters
	
	list_of_strings = []
	temp_string = ""

	for char in alphanumeric_string:
		
		if char.isalpha():
			temp_string = temp_string + char 			# append consecutive characters to form a string and store it in a temporary variable 
		
		elif char.isnumeric() and temp_string != '':
			list_of_strings.append(temp_string)         # append the fully-formed sub-word to a list
			temp_string = ""                            # reset temporary variable to include the next sub-word

	# accounting for a sub-word that may occur at the end of the string
	# if there is no sub-word at the end of the string, it will contain a ''	                                                    
	list_of_strings.append(temp_string)                    
    
    # we don't need the '' in our return
	return list_of_strings[:-1] if list_of_strings[-1] == '' else list_of_strings


'''
Function: count_alphabets()

Function Design:

return the count of the number of alphabets in the string
'''

def count_alphabets(alphanumeric_string):        # type(alphanumeric_string) : string, should contain only alphanumeric characters
	
	return sum([1 for char in alphanumeric_string if char.isalpha()])


'''
Function: keypad()

Function Design:

returns a hard-coded dictionary for enabling conversion from number to words and vice-versa
'''

def keypad():
	
	# dictionary to relate numbers with its associated letters (referred to mobile phone keypad)
    num_word_dict = {'1':['1'], '2': ['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'],
                     '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':['0']}

    word_num_dict = {'1':'1','A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4','H':'4','I':'4','J':'5','K':'5','L':'5',
                     'M':'6','N':'6','O':'6','P':'7','Q':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9',
                     'X':'9','Y':'9','Z':'9','0':'0'}
    
    return num_word_dict, word_num_dict