# Author: Mayank Bhardwaj
# Start date: 26 April 2018
# Last modified date: 04 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This code analyse the number of words in the morse code dictionary
# and put in the word_dictionary and display.


class WordAnalyser:
    # -----------------------Initialize the word dictionary---------------------
    def __init__(self):
        self.word_dictionary = {}

    # -----------------------Prints the word dictionary-------------------------

    def __str__(self):
        string_to_print = 'Below is the count of number of words occurs:' + '\n'
        for key_name, value_name in self.word_dictionary.items():
            string_to_print += (key_name + ' : ' + str(value_name) + '\n')
        return string_to_print

    # ------This analyse the number of words in the all decoded morse code------

    def analyse_words(self, morse_code_all_list):
        individual_dict = {}
        space_list = morse_code_all_list.split(' ')
        # -------------this block is to count individual words------------------
        # ---------------------occurs in all user inputs------------------------

        for all_word in space_list:
            if all_word not in (',', '.', '?', ''):
                all_word = all_word.replace(',', '')
                all_word = all_word.replace('.', '')
                all_word = all_word.replace('?', '')
                if all_word in self.word_dictionary.keys():
                    self.word_dictionary[all_word] += 1
                else:
                    self.word_dictionary[all_word] = 1

                if all_word in individual_dict.keys():
                    individual_dict[all_word] += 1
                else:
                    individual_dict[all_word] = 1

        print(morse_code_all_list,
              'contains the below count of each word:')
        for key, value in individual_dict.items():
            print(key, ':', value)
