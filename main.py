from create_dictionary import *
from number_to_words import *
from words_to_number import *
from all_wordifications import *
from filtered_wordifications import *
from utils import *

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-w", "--wordify", action = "store",
    dest = "number", help = "Suggest a Wordification for the US Phone Number")

parser.add_argument("-n", "--numerize", action = "store",
    dest = "word", help = "Convert the Wordified Number to a Phone Number")

parser.add_argument("-f", "--format", action = "store",
    dest = "format", help = "Specify a Format for Conversion to a Phone Number")

parser.add_argument("-a", "--all", action = "store",
    dest = "all", help = "Find all Wordifications of a US Phone Number")

parser.add_argument("-filtered", "--filtered", action = "store",
    dest = "filtered", help = "Find the Filtered Wordifications of a US Phone Number")

parser.add_argument("-d", "--dict", action = "store",
    dest = "dict", default = "final_dictionary.txt",
    help = "Specify Dictionary")

parser.add_argument("-i", "--input", action = "store",
    dest = "input", default = "dictionaries/",
    help = "Provide the directory path which contains the smaller dictionaries")

parser.add_argument("-o", "--output", action = "store",
    dest = "output", default = "final_dictionaries_custom.txt",
    help = "Provide the filepath (including a filename of your choice) to output the final dictionary")

parser.add_argument("-c", "--create", action = "store",
	dest = "create", help = "To Create a Dictionary")

def main(args):
    
    # wordify a given phone number and print out one wordification
    if args.number != None:
        
        wordified = number_to_words(args.number, args.dict)
        
        print("Number:", args.number)
        print("Wordified Number:", wordified)
        
        return wordified

    # numerize a string into the format of your choice
    if args.word != None:
        
        numerized = words_to_number(args.word, args.format)
        
        print("Wordified Number:", args.word)
        print("Number", numerized)
        
        return numerized

    # wordify a phone number of your choice and print out all possible wordifications
    if args.all != None:
        
        all_words = all_wordifications(args.all) 
        
        for ind, wordified in enumerate(all_words):
            print("{}: ".format(ind+1), wordified, end='\n')
        
        print("Found {} Wordifications".format(len(all_words)))
        
        return all_words

    # wordify a phone number of your choice and print out the filtered wordifications
    if args.filtered != None:
        
        filtered_words = filtered_wordifications(args.filtered, args.dict) 
        
        for ind, wordified in enumerate(filtered_words):
            print("{}: ".format(ind+1), wordified, end='\n')
        
        print("Found {} Wordifications".format(len(filtered_words)))
        
        return filtered_words

    # create a Dictionary of your choice
    if args.create != None:
    	create_dictionary(args.input, args.output)
    	print("Your new dictionary can be found at: {}".format(args.output))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)