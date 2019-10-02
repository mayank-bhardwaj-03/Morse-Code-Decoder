# Author: Mayank Bhardwaj
# Start date: 26 April 2018
# Last modified date: 04 May 2018
# Version 1.0 (please update the version while implementing the code changes)
# -------------------------------Version 1.0------------------------------------
# This code prints the morse code dictionary and decode the morse code input
# sequence and stores decoded in morse_code_all_list


class Decoder:
    morse_code_all_list = []

    # ----------------the Morse code dictionary defination----------------------

    def __init__(self):
        self.dictionary = {
            'A': '01',
            'B': '1000',
            'C': '1010',
            'D': '100',
            'E': '0',
            'F': '0010',
            'G': '110',
            'H': '0000',
            'I': '00',
            'J': '0111',
            'K': '101',
            'L': '0100',
            'M': '11',
            'N': '10',
            'O': '111',
            'P': '0110',
            'Q': '1101',
            'R': '010',
            'S': '000',
            'T': '1',
            'U': '001',
            'V': '0001',
            'W': '011',
            'X': '1001',
            'Y': '1011',
            'Z': '1100',
            '0': '11111',
            '1': '01111',
            '2': '00111',
            '3': '00011',
            '4': '00001',
            '5': '00000',
            '6': '10000',
            '7': '11000',
            '8': '11100',
            '9': '11110',
            '?': '001100',
            ',': '110011',
            '.': '010101'
        }

    # --------------------Prints the morse code dictionary----------------------

    def __str__(self):
        string_to_print = 'Morse code Dictionary' + '\n'
        string_to_print += 'word/number  ' + ':' + '  morse code' + '\n'

        # --------below section use to print the morse code dictionary.---------

        for key_name, value_name in self.dictionary.items():
            string_to_print += key_name + '            :  ' + value_name + '\n'
        return string_to_print

    def __get__dictionary(self):
        return self.dictionary

    # -----------------Set the value of morse code dictionary-------------------

    def __set__(self, dictionary):
        self.dictionary = dictionary

    # -------------this function use to decode the morse code input-------------

    def decode(self, morse_code_sequence):
        appended_morse_code = []
        decoded_morse_code_list = []
        user_input_list = []

        if len(morse_code_sequence) >= 1 and morse_code_sequence not in \
                ('n', 'N'):
            for value in range(len(morse_code_sequence)):
                if morse_code_sequence[value] not in ('0', '1', '*'):
                    print('Please enter the valid morse code consists of'
                          '0, 1 & *')
                    return None

                elif '***' not in morse_code_sequence:
                    print('The input does not contain atleast one set of'
                          ' triple *')
                    return None

            if morse_code_sequence is not None or morse_code_sequence != '':
                print('The entered morse code by you is ' + morse_code_sequence)
                appended_morse_code.append(morse_code_sequence)

        elif morse_code_sequence in ('N', 'n'):
            print('Exiting...................')
            return None
        else:
            print(
                'Please write your Morse Code of minimum length of 1 character')
            return None

        # split the user input and verify it from dictionary
        for user_input_list in appended_morse_code:
            split_user_input_list = user_input_list.split('*')
            decoded_morse_code_list = []

            # -----This uses to check the punctuation in the start and end------

            if split_user_input_list[-1] in ('001100', '110011', '010101') \
                    and split_user_input_list[0] not in ('001100', '110011',
                                                         '010101'):
                for i in range(len(split_user_input_list)):
                    if split_user_input_list[i] in self.dictionary.values():
                        if i != (len(split_user_input_list) - 1) and \
                                split_user_input_list[i] in ('001100',
                                                             '110011',
                                                             '010101') \
                                and \
                                split_user_input_list[i + 1] in \
                                ('001100', '110011', '010101'):
                            print('There can not be two punctuations together.')
                            return None
                        elif (i == (len(split_user_input_list) - 1)) and \
                                split_user_input_list[i] in ('001100',
                                                             '110011',
                                                             '010101') \
                                and ((split_user_input_list[i - 2] in ('001100',
                                                                       '110011',
                                                                       '010101')
                                      and split_user_input_list[i - 1] == '') or
                                     split_user_input_list[i - 1] in ('001100',
                                                                      '110011',
                                                                      '010101')):
                            print('There can not be two punctuations together.')
                            return None
                        else:
                            for key_name, value_name in self.dictionary.items():

                                # ---------Checking of user input present-------
                                # ---------in the morse code dictionary---------

                                if split_user_input_list[i] == value_name:
                                    input_check_key = key_name
                                    decoded_morse_code_list.append(
                                        input_check_key)
                                else:
                                    print('invalid morse code')
                                    return None
                    # -----Below is used to check the space and implement-------
                    # ----that space on basis of three * in the decoded code----

                    elif split_user_input_list[i] == '':
                        if i != (len(split_user_input_list) - 1):
                            if split_user_input_list[i + 1] == '' and \
                                    split_user_input_list[i + 2] == '':
                                print(user_input_list,
                                      ': contains incorrect spaces,'
                                      ' Please enter morse code with'
                                      ' correct spaces')
                                return None

                            elif split_user_input_list[i - 1] != '' and \
                                    split_user_input_list[i + 1] != '':
                                print(user_input_list,
                                      ': contains incorrect spaces, '
                                      'please enter morse code with'
                                      ' correct spaces')
                                return None
                            else:
                                decoded_morse_code_list.append(' ')

            elif split_user_input_list[-1] not in \
                    ('001100', '110011', '010101'):
                print('Morse code does not end with'
                      ' punctuation ? or , or , so it is invalid')
                return None
            elif split_user_input_list[0] in ('001100', '110011', '010101'):
                print('Morse code starts with punctuation ? or , or'
                      ' , so it is invalid')
                return None
            else:
                print(' ')
            decoded_morse_code_list = ''.join(decoded_morse_code_list)

            # -----decoded morse code appended in the morse_code_all_list-------

            Decoder.morse_code_all_list.append(decoded_morse_code_list)

            # -----------------To display the decoded morse code----------------

        if decoded_morse_code_list is not None:
            print('The decoded morse code for ', user_input_list,
                  ' is ', decoded_morse_code_list)
        else:
            print('The decoded morse code for ', user_input_list,
                  ' is ', 'no morse code conversion')

        return Decoder.morse_code_all_list
