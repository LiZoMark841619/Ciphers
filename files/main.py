from my_python.filefinder import helper
from caesar import Caesar
from vigenere import Vigenere

valid_num = helper.get_valid_number
valid_str = helper.get_valid_str

ciphers = ['caesar', 'vigenere']
cipher = valid_str(f'Chose from {ciphers} to start! ', *ciphers)
msg_ = input('Enter a message you want to send! ').lower()
question = valid_str('Chose from decode or encode! ', 'encode', 'decode')

if cipher == 'caesar':
    offset_ = valid_num(f'Enter the offset to shift the letters from 0-26! ', 0, 27)
    if question == 'decode':
        print(Caesar(msg_).decode(offset=offset_))
    else:
        print(Caesar(msg_).encode(offset=offset_))
else:
    keyword_ = input('Enter a keyword! ').lower()
    if question == 'decode':
        print(Vigenere(msg_, keyword_).decode())
    else:
        print(Vigenere(msg_, keyword_).encode())