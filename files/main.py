from methods import get_valid_number, get_valid_str
from caesar import Caesar
from vigenere import Vigenere

ciphers = ['caesar', 'vigenere']
cipher = get_valid_str(f'Chose from {ciphers} to start! ', *ciphers)
msg_ = input('Enter a message you want to send! ').lower()
question = get_valid_str('Chose from decode or encode! ', 'encode', 'decode')

if cipher == 'caesar':
    offset_ = get_valid_number(f'Enter the offset to shift the letters from 0-26! ', 0, 27)
    print(Caesar(msg_))
    if question == 'decode':
        print(f'After decoding the message: {Caesar(msg_).decode(offset=offset_)}')
    else:
        print(f'After encoding the message: {Caesar(msg_).encode(offset=offset_)}')
else:
    keyword_ = input('Enter a keyword! ').lower()
    print(Vigenere(msg_, keyword=keyword_))
    if question == 'decode':
        print(f'After decoding the message: {Vigenere(msg_, keyword_).decode()}')
    else:
        print(f'After encoding the message: {Vigenere(msg_, keyword_).decode()}')
