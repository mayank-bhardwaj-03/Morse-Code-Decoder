# Author: Mayank Bhardwaj
# Start date: 26 April 2018
# Last modified date: 04 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This code analyse the number of character in the morse code dictionary
# and put in the character_dictionary and display.


class CharacterAnalyser:
    # ---------------------Initialize the character dictionary------------------

    def __init__(self):
        self.character_dictionary = {}

    # ---------------------Prints the character dictionary----------------------

    def __str__(self):
        string_to_print = 'The total number of character occurs in the all ' \
                          'morse code are given below :' + '\n'
        # -------------------prints the character dictionary--------------------
        for key_name, value_name in self.character_dictionary.items():
            string_to_print += (key_name + ' : ' + str(value_name) + '\n')
        return string_to_print

    # ----This analyse the number of characters in the all decoded morse code---

    def analyse_characters(self, morse_code_all_list):
        individual_dict = {}
        # -------------this block is to check individual characters-------------
        # ---------------------occurs in all user inputs------------------------

        for all_character in morse_code_all_list:
            if all_character not in (',', '.', '?', '', ' '):
                if all_character in self.character_dictionary.keys():
                    self.character_dictionary[all_character] += 1
                else:
                    self.character_dictionary[all_character] = 1

                if all_character in individual_dict.keys():
                    individual_dict[all_character] += 1
                else:
                    individual_dict[all_character] = 1

        print(morse_code_all_list, 'contains the below count of each '
                                   'character:')
        for key, value in individual_dict.items():
            print(key, ':', value)
