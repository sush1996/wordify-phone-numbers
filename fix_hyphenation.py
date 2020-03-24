'''
Design:


1. each sub-word should be contained within hyphens
2. xxx-[xxx]-xxxx : middle-structure, xxx-xxx-[xxxx] : end-structure ([] -  indicates the part of the format under consideration)

  - if the length of the sub-word exceeds middle-structure length, then continue the sub-word in end-structure without hyphenation
  - if the length of the sub-word is less than the length of either structure length, then hyphenate within the structure   
 
'''

# alphanumeric string (without special characters) and should only be part of the 
# phone number that needs to be wordified (i.e last 7 characters of the US phone number)

def fix_hyphenation_all(alphanumeric_string): 
	
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

#def fix_hyphenation_all()

'''
Next Steps:
1. Design hyphenation for filtered numbers (filtered according to a dictionary) 
'''