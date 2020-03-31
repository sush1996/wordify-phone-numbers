# wordify-phone-numbers
Wordifying US phone numbers 

This GitHub repository hosts 3 main functions:

`number_to_words()`, which takes as an argument a string representing a US phone number and which outputs a string which has transformed part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone (for example, a valid output of number_to_words("1-800-724-6837") could be "1-800-PAINTER"). If you find it makes things simpler, feel free to constrain this function to only output "wordifications" in English.

`words_to_number()`, which does the reverse of the above function (for example, the output of words_to_number("1-800-PAINTER") should be "1-800-724-6837")

`all_wordifications()`, which outputs all possible combinations of numbers and English words in a given phone number.

The main functions rely on many of the helper methods present in the `utils.py` in the `Utils` folder

`main.py` allows for running the above scripts in the command line interface:

A few examples are demonstrated as below:

* To fetch all possible wordifications of your number, use the function `all_wordififcations()` by running  `python3 main.py -a +1-800-724-6837`
* To fetch a set of sensible wordifications of your number, use the function `filtered_wordififcations()` by running `python3 main.py -filter +1-800-724-6837 -d Utils/words_alpha_mod.txt` 
* To wordify your number, use the function `number_to_words()` by running `python3 main.py -w +1-800-724-6837 -d Utils/words_alpha_mod.txt`
* To numerize a wordification, use the function `words_to_number()` by running `python3 main.py -n 800PAINTER -f +1-xxx-xxx-xxxx`


 
