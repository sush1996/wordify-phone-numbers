# wordify-phone-numbers
Wordifying US phone numbers 

This GitHub repository hosts 3 main functions:

`number_to_words()`, which takes as an argument a string representing a US phone number and which outputs a string which has transformed part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone (for example, a valid output of number_to_words("1-800-724-6837") could be "1-800-PAINTER"). If you find it makes things simpler, feel free to constrain this function to only output "wordifications" in English.

`words_to_number()`, which does the reverse of the above function (for example, the output of words_to_number("1-800-PAINTER") should be "1-800-724-6837")

`all_wordifications()`, which outputs all possible combinations of numbers and English words in a given phone number.

The main functions rely on many of the helper methods present in the `utils.py` in the `Utils` folder

`main.py` allows for running the above scripts in the command line interface:

A few examples are demonstrated as below:

* To fetch all possible wordifications of your number, use the function `all_wordififcations()` by running :\
  `python3 main.py -a +1-800-724-6837`
* To fetch a set of sensible wordifications of your number, use the function `filtered_wordififcations()` by running :\ 
  `python3 main.py -filter +1-800-724-6837 -d Utils/custom_dictionary.txt`\ `-d` is optional and can be omitted. The default dictionary then used will be `Utils/words_alpha_mod.txt` 
* To wordify your number, use the function `number_to_words()` by running :\
  `python3 main.py -w +1-800-724-6837 -d Utils/words_alpha_mod.txt` \ `-d` is optional and can be omitted. The default dictionary then used will be `Utils/words_alpha_mod.txt`
* To numerize a wordification, use the function `words_to_number()` by running :\ 
  `python3 main.py -n 800PAINTER -f xxx-xxx-xxxx` \ `-f` is mandatory, please provide a format of your choice. (eg. `+1-xxx-xxx-xxxx` or `1xxx-xxx-xxxx` etc) 
* To create a dictionary of your choice (i.e) to pre-process or to combine multiple dictionaries, store the `.txt` files in the Dictionaries folder and run :\
  `python3 main.py -create -i /Dictionaries -o Utils/custom_final_dictionary.txt` \ `-i` must be a directory and `-o` must be a filepath plus the filename. These arguments are optional, the default for `-i` is `/Dictionaries` and default for `-o` is `Utils/custom_final_dictionary.txt`

# Tools and Packages Used

* `Python3.6.9`
* ['itertools'](https://docs.python.org/3/library/itertools.html) - the main package used when writing code for this package
* [`time` module](https://docs.python.org/3/library/time.html) - to keep track of function execution time
* ['profiler'](https://docs.python.org/3/library/profile.html) - also used a profiler to keep track of the execution profile and make improvements accordingly (helped a great deal!)

# Brief Methodology

* `all_wordifications()` : made use of a hashmap (dictionary) to store the list of alphabets that a number corresponds to. `itertools.product` takes in the list of lists of alphabets              	corresponding to all the numerical digits in the given number and a cartesian product of all elements in the input list of lists is the output - this ensures all valid combinations are generated. A set of the generated list is done finally to rid of duplicates.
* `filtered_wordifications()` : this function follows the same structure as `all_wordifications` but makes use of an english dictionary file to filter out the generated combinations which are not present in the dictionary - a tl;dr version of what the code actually does, I've abstracted away the finer complexities in `utils` 
* `number_to_words()` : makes use of the very first number wordification in the sorted output of `filtered_wordifications`. The sorting is done in a descending order based on the count of consecutive alphabets in the proposed wordifications.
* `words_to_number()` : this function makes use of the hashmap with keys as letters and the assocated number as the value. Then a case by case conversion of alphabets to numbers is performed while also considering the user given format into account. 

# Resources
Frequently used dicitonaries found in other GitHub repos

* [`20k.txt`](https://github.com/first20hours/google-10000-english/blob/master/20k.txt) - Contains the 20000 most freuqently occuring words
* [`words.txt`](https://github.com/dwyl/english-words/blob/master/words.txt) - A massive dictionary that contains words which are not strictly alphabetical (need to preprocess) - use `create_dictionary.py`
* [`words_alpha.txt`](https://github.com/dwyl/english-words/blob/master/words.txt) - Another dictionary containing commonly occuring words 

