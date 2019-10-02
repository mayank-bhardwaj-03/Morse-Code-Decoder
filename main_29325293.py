# Author: Mayank Bhardwaj
# Start date: 26 April 2018
# Last modified date: 04 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# this is the main function that will import the
# 1. Decoder class
# 2.CharacterAnalyser class
# 3.WordAnalyse
# 4.SentenceAnalyser
# and calls the main function to decode and analyse the morse code input.

# ----------------------Below are the import of different class-----------------

from decoder_29325293 import Decoder
from character_29325293 import CharacterAnalyser
from word_29325293 import WordAnalyser
from sentence_29325293 import SentenceAnalyser


def morse_code_decoder():
    morse_code = Decoder()
    morse_code_all_list = []
    print(morse_code)
    morse_code_rerun = 'y'

# ----This block takes the user input and verifies the input is valid or not----

    while morse_code_rerun in ('y', 'Y'):
        morse_code_sequence = input(
            'please write your Morse Code for decoding(it should comprise of '
            '0, 1 & * ) or type N/leave blank and enter to Quit( and '
            'check the decoded morse code ) : ')
        morse_code_all_list = morse_code.decode(morse_code_sequence)

        morse_code_rerun = input(
            'Are you sure you want to continue? Type y for yes'
            ' and enter/type anything and then enter for No :')

    return morse_code_all_list


# ----------function will call class CharacterAnalyser and analyses-------------
# ------each character in the decoded morse code sequences and prints it--------
def count_for_character(decoded_sequence):
    # --------------------class object for CharacterAnalyser--------------------
    character_count = CharacterAnalyser()
    for each in decoded_sequence:
        character_count.analyse_characters(each)

    print(character_count)


# ----------function will call class CharacterAnalyser and analyses-------------
# ------each word in the decoded morse code sequences and prints it--------
def count_for_word(decoded_sequences):
    # -----------------------class object for WordAnalyser----------------------
    word_count = WordAnalyser()
    for each in decoded_sequences:
        word_count.analyse_words(each)

    print(word_count)


# ------------function will call class SentenceAnalyser and analyses------------
# ------each sentences in the decoded morse code sequences and prints it--------
def count_for_sentence(decoded_sequences):
    # -----------------------class object for WordAnalyser----------------------
    sentence_count = SentenceAnalyser()
    for each in decoded_sequences:
        sentence_count.analyse_sentences(each)

    print(sentence_count)


# ---------------Main function will uses to print menu for the user-------------
# ------------------and decided the flow of the all function--------------------

def main():
    code_decoder = morse_code_decoder()
    analyser_rerun = 'Y' or 'y'
    if code_decoder != '' and code_decoder is not None:
        while analyser_rerun == 'Y':

            menu = str(
                input("Enter the value to analysed different levels:\n"
                      "1. Total number of character\n"
                      "2. Total number of words\n"
                      "3. Total number of sentences\n"
                      "4. To analyse characters, words and sentences\n"))
            # ------------------Total number of characters----------------------
            if menu == '1':  # character level
                count_for_character(code_decoder)
            # ------------------Total number of words====-----------------------
            elif menu == '2':
                count_for_word(code_decoder)
            # ------------------Total number of sentences-----------------------
            elif menu == '3':  # sentence level
                count_for_sentence(code_decoder)
            # -------------To analyse characters, words and sentences-----------
            elif menu == '4':
                count_for_character(code_decoder)
                count_for_word(code_decoder)
                count_for_sentence(code_decoder)

            elif menu == '':
                print('Please enter the valid option 1, 2, 3 or 4')
            else:
                print('Please enter the valid option 1, 2, 3 or 4')

            analyser_rerun = input('Do you want to choose another option? Press'
                                   ' Y or press N or blank enter to exit:')


if __name__ == '__main__':
    # ---------------------This uses to start main function---------------------
    main()
    print('Thank you for using morse code decoder__Mayank Bhardwaj')
