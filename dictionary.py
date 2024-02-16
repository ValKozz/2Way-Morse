class Dictionary:
    def __init__(self, space = '/'):
        self.dict_space = space

        self.translate_dict = {
            ' ': self.dict_space,
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-...',
            '7': '--...',
            '8': '---.',
            '9': '----.',
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            '=': '-...-',
            '/': '_ . . _.',
            '+': '. _ . _.',
            '_': '..--.-',
            '(': '-.--.',
            ')': '-.--.-',
            "'": '.----.',
            '"': '.-..-.',
            ':': '---...'
        }