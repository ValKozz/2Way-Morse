from dictionary import Dictionary


def ask_on_start():
    ask_mode = input('Decode or encode? -q to exit.\n')

    if ask_mode == 'q':
        exit()

    if ask_mode != 'encode' and ask_mode != 'decode':
        print('Invalid input!')
        return ask_on_start()
    take_input(ask_mode)


def take_input(mode):
    space_symbol = input('Enter symbol used as space, if any. Empty output defaults to "/":\n').strip()[0]

    dictionary_class = Dictionary(space_symbol)

    message = (input('Please enter the message to encode/decode:\n')).upper()

    if mode == 'encode':
        encode(message, dictionary_class.translate_dict)
    else:
        decode(message, dictionary_class.translate_dict)


def encode(message, dictionary):

    non_coded_list = [char for char in message]
    encoded_msg_list = \
        [char.replace(char[0], dictionary[char]) for char in non_coded_list if char in dictionary]

    encoded_msg = ' '.join(encoded_msg_list)
    print(encoded_msg)
    return encoded_msg


def decode(message, dictionary):
    message_list = message.split(' ')
    output = []

    for letter in message_list:
        for key, item in dictionary.items():
            if letter == item:
                output.append(key)
                continue
    print(''.join(output))


if __name__ == '__main__':
    ask_on_start()
