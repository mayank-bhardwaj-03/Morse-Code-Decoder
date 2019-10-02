# Author: Mayank Bhardwaj
# Start date: 26 April 2018
# Last modified date: 04 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This code analyse the number of sentences in the morse code dictionary
# and put in the sentence_dictionary and display.


class SentenceAnalyser:
    # ------------------Initialize the sentences dictionary---------------------

    def __init__(self):
        self.sentence_dictionary = {}

    # -----------------------Prints the word dictionary-------------------------

    def __str__(self):
        string_to_print = 'Below is the count of number of sentences occurs:' \
                          + '\n'
        # -------------------prints the sentence dictionary---------------------
        for key_name, value_name in self.sentence_dictionary.items():
            string_to_print += (key_name + ' : ' + str(value_name) + '\n')
        return string_to_print

    # ------This analyse the number of words in the all decoded morse code------

    def analyse_sentences(self, morse_code_all_list):
        individual_dict = {}
        # -------------this block is to check type of sentences-----------------
        # ---------------------occurs in all user inputs------------------------

        for all_sentence in morse_code_all_list:
            if all_sentence in (',', '.', '?'):
                if all_sentence == '?':
                    all_sentence = 'question'
                elif all_sentence == '.':
                    all_sentence = 'sentence'
                else:
                    all_sentence = 'clause'
                if all_sentence in self.sentence_dictionary.keys():
                        self.sentence_dictionary[all_sentence] += 1
                else:

                        self.sentence_dictionary[all_sentence] = 1

                if all_sentence in individual_dict.keys():
                        individual_dict[all_sentence] += 1
                else:
                        individual_dict[all_sentence] = 1

        if 'clause' in self.sentence_dictionary.keys():
            self.sentence_dictionary['clause'] += 1
        if 'clause' in individual_dict.keys():
            individual_dict['clause'] += 1

        print(morse_code_all_list,
              'contains the below count of each sentence type:')
        for key, value in individual_dict.items():
            print(key, ':', value)
