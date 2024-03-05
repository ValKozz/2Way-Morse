from dictionary import Dictionary
from Beeper import Beeper
from TextToSpeech import TextToSpeech
from time import sleep

DOT_TIME = 0.1  # 0.1 second dot timing, you can change this here (equals about 12 words per min)
FREQUENCY = 600  # Hz


class Translator:
    def __init__(self):

        self.audio = None
        self.space_symbol = '/'

        self.ask_on_start()

    def ask_audio(self):
        if self.audio is None:
            enable_audio = input('Enable Audio? (Y/N)\n').lower()
            if enable_audio == 'y':
                self.audio = True
            else:
                print('Disabling Audio.')

    def ask_on_start(self):
        self.ask_audio()
        ask_mode = input('Decode or encode? -q to exit.\n').lower()

        if ask_mode == 'q':
            exit()

        while ask_mode != 'encode' and ask_mode != 'decode':
            print('Invalid input!')

        self.take_input(ask_mode)

    def take_input(self, mode):
        self.space_symbol = input('Enter symbol used as space, if any. Empty output defaults to "/":\n').strip()

        if self.space_symbol != '':
            self.space_symbol = self.space_symbol[0]
        else:
            self.space_symbol = '/'

        dictionary_class = Dictionary(self.space_symbol)

        message = (input('Please enter the message to encode/decode:\n')).upper()

        if mode == 'encode':
            self.encode(message, dictionary_class.translate_dict)
        else:
            self.decode(message, dictionary_class.translate_dict)

    def encode(self, message, dictionary):
        non_coded_list = [char for char in message]
        encoded_msg_list = \
            [char.replace(char[0], dictionary[char]) for char in non_coded_list if char in dictionary]

        encoded_msg = ' '.join(encoded_msg_list)
        print(encoded_msg)
        if self.audio:
            self.encode_audio(message=encoded_msg)

    def decode(self, message, dictionary):
        message_list = message.split(' ')
        output = []

        for letter in message_list:
            for key, item in dictionary.items():
                if letter == item:
                    output.append(key)
                    continue
        decoded_msg = ''.join(output)
        print(decoded_msg)

        if self.audio:
            self.decode_audio(decoded_msg)

    def encode_audio(self, message):
        beeper = Beeper(dot_time=DOT_TIME, frequency=FREQUENCY)
        for symbol in message:
            if symbol == ' ':
                sleep(beeper.l_pause)
            elif symbol == self.space_symbol:
                sleep(beeper.w_pause)
            else:
                beeper.play(symbol)

    def decode_audio(self, message):
        engine = TextToSpeech()
        engine.say(message)


if __name__ == '__main__':
    print('''
Terminal Based, audio enabled Morse code Translator in Python.
Made by Valeri Kozarev, @ValKozz
''')
    Translator()
