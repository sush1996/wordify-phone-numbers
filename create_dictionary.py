'''
To create a final list of words from all text files in the folder, the following steps are undertaken:

1. Choose words with length less than or equal to 7 and greater than 1
2. Exclude words which are not alphabetical in nature
3. Convert all the letters of the chosen word to uppercase

Current content in 'dictionaries' folder
1. 20k.txt :    https://github.com/first20hours/google-10000-english/blob/master/20k.txt
2. words.txt :  https://github.com/dwyl/english-words/blob/master/words.txt    
'''

import os

filepath = 'dictionaries/'  #Make sure to include any relevant text files in the 'dictionaries' folder
all_words = []

for file_name in os.listdir(filepath):
    file_to_read = open(filepath+"/"+file_name, 'r+')
    file_data = file_to_read.readlines()
    
    for word in file_data:
        word = word.strip('\n')

        if len(word) <= 7 and len(word) > 1 and word.isalpha() == True:   #Criteria 1 and 2 in the description
            word = word.upper()
            all_words.append(word)
        else:
            continue

all_words = list(set(all_words))
all_words = sorted(all_words, key=lambda word_len:len(word_len))

with open("final_dictionary.txt", "w+") as f:
    for word in all_words:
        f.write(word+'\n')

'''
Input: Takes in folder containing all the text files to pre-process and compile
Output: final_dictionary.txt - final version containing a set of all the words in all the text files that were compiled
'''