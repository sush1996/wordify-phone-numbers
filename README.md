# Wordify Phone Numbers
Wordifying US phone numbers 

This GitHub repository hosts 3 main functions:

`number_to_words()`, which takes as an argument a string representing a US phone number and which outputs a string which has transformed part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone (for example, a valid output of number_to_words("1-800-724-6837") could be "1-800-PAINTER"). If you find it makes things simpler, feel free to constrain this function to only output "wordifications" in English.

`words_to_number()`, which does the reverse of the above function (for example, the output of words_to_number("1-800-PAINTER") should be "1-800-724-6837")

`all_wordifications()`, which outputs all possible combinations of numbers and English words in a given phone number.

The main functions rely on many of the helper methods present in the `utils.py` in the `Utils` folder

`main.py` allows for running the above scripts in the command line interface:

A few examples are demonstrated as below:

* To fetch all possible wordifications of your number, use the function `all_wordififcations()` by running : <br />
  `python3 main.py -a [PHONE_NUMBER]`
* To fetch a set of sensible wordifications of your number, use the function `filtered_wordififcations()` by running : <br />
  `python3 main.py -filter [PHONE-NUMBER] -d [DICTIONARY_FILE]`\ `-d` is optional and can be omitted. The default dictionary then used will be `Utils/words_alpha_mod.txt` 
* To wordify your number, use the function `number_to_words()` by running : <br />
  `python3 main.py -w [PHONE_NUMBER] -d [DICTIONARY_FILE]` <br /> `-d` is optional and can be omitted. The default dictionary then used will be `Utils/words_alpha_mod.txt`
* To numerize a wordification, use the function `words_to_number()` by running : <br /> 
  `python3 main.py -n [WORDIFIED_NUMBER] -f [FORMAT]` <br /> `-f` is optional and can be omitted. The default format used is: `1-xxx-xxx-xxxx`, feel free to provide a valid format of your choice. (eg. `+1-xxx-xxx-xxxx`, `1xxx-xxx-xxxx`, `xxx-xxx-xxx`, `1xxx-xxx-xxxx`, `+1xxxxxxxxxx`, etc) 
* To create a dictionary of your choice (i.e) to pre-process or to combine multiple dictionaries, store the `.txt` files in the Dictionaries folder and run : <br />
  `python3 main.py -create -i [DICTIONARY_DIRECTORY] -o [FILENAME]` <br /> `-i` must be a directory and `-o` must be a filepath plus the filename. These arguments are optional, the default for `-i` is `/Dictionaries` and default for `-o` is `Utils/custom_final_dictionary.txt`

# Sample Output
Open terminal in the same directory as `main.py` and run: <br />

* `Input Command:` `python3 main.py -a 1-800-724-6837` <br />
```
Output:

	.
	.
	.

102392:  1-V-00-R-2-H-6-UFQ
102393:  1-800-SC-4-OV-3-R
102394:  1-T-00-PBGMTE-7
102395:  1-U-00-Q-2-GMTE-7
102396:  1-T-007-CIOVE-7
102397:  1-V-007-BGMTDQ
102398:  1-U-00-R-2-GNUFQ
102399:  1-T-00-SAHMVFR
102400:  1-800-7-BINTDS

Found 102400 Wordifications
```


* `Input Command:` `python3 main.py -filter 1-800-724-6837` <br />
```
Output:

1:  1-800-PAINTER
2:  1-800-PAINT-ES
3:  1-800-PAINT-ER
4:  1-800-SAINT-ES
5:  1-800-SAINT-ER
6:  1-800-RAI-OUDS
7:  1-800-RAH-MUDS
8:  1-800-SAG-MUDS
9:  1-800-PA-INTER
	.
	.
	.
Found 239 Wordifications
```

* `Input Command:` `python3 main.py -n 1-800-724-6837 ` <br />
```
Output:

Number: 1-800-724-6837
Wordified Number: 1-800-PAINTER
```

* `Input Command:` `python3 main.py -w 1-800PAINTER -f 1-xxx-xxx-xxxx` <br />
```
Output:

Wordified Number: 1-800PAINTER
Number 1-800-724-6837
```

* `Input Command:` `python3 main.py -create -i Dictionaries/ -o Utils/custom_final_dictionary.txt` <br />


# Tools and Packages Used

* `Python3.6.9`
* [`itertools`](https://docs.python.org/3/library/itertools.html) - the main package used when writing code for this package
* [`time`](https://docs.python.org/3/library/time.html) - to keep track of function execution time
* [`profiler`](https://docs.python.org/3/library/profile.html) - also used a profiler to keep track of the execution profile and make improvements accordingly (helped a great deal!)

# Brief Methodology

* `all_wordifications()` : made use of a hashmap (dictionary) to store the list of alphabets that a number corresponds to. `itertools.product` then takes in the list of lists of alphabets              corresponding to all the numerical digits in the given number and a cartesian product of all elements of in list of lists is the generated. Then elements of each list is joined to form a string and is then stored in a set.
* `filtered_wordifications()` : this function follows the same structure as `all_wordifications` but makes use of an english dictionary file to filter out the combinations which are not present in the dictionary - a tl;dr version of the code. I've abstracted away the many of the finer complexities in `utils` 
* `number_to_words()` : makes use of the very first number wordification in the sorted output of `filtered_wordifications`. The sorting is done in a descending order based on the count of consecutive alphabets in the wordifications proposed by `filtered_wordifications`.
* `words_to_number()` : this function makes use of the hashmap with keys as letters and the associated number as the value. Then a case by case conversion of alphabets to numbers is performed while also considering a user given format into account to get the final number equivalent of the word. 

# Resources

Dictionaries containing the most frequently found english wordsfound in other GitHub repos

* [`20k.txt`](https://github.com/first20hours/google-10000-english/blob/master/20k.txt) - Contains the 20000 most freuqently occuring words
* [`words.txt`](https://github.com/dwyl/english-words/blob/master/words.txt) - A massive dictionary that contains words which are not strictly alphabetical (need to preprocess) - use `create_dictionary.py`
* [`words_alpha.txt`](https://github.com/dwyl/english-words/blob/master/words.txt) - Another dictionary containing commonly occuring words 

`create_dictionary` can combine multiple dictionaries and pre-process the words to store them in a single `.txt` file. Or just pre-process the words in a single file.
Pre-process steps: Filter words less than length 2 and greater than length 10 and also filter all words with special characters in them. Finally capitalize each of the non filtered word and store them in a text file.  

# Notes

* The `filtered_wordifications` takes roughly ~30 seconds for numbers which don't have any 0's or 1's. But takes less than 1 second for other numbers.
Consider coming up with a better approach to wordify since current method is built on a case-by-case basis and takes a long time for certain numbers.