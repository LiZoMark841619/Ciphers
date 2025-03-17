from ciphers import Cipher
from string import ascii_lowercase

alphabet = ascii_lowercase

class Caesar(Cipher):
    def __init__(self, msg: str, offset: int) -> None:
        super().__init__(msg, kind='caesar')
        self.offset = offset

    def code_message(self, encode: bool | None = True) -> str:
        offset = self.offset * -1 if encode is None or encode == True else self.offset
        return ''.join([alphabet[(alphabet.find(char) + offset) % 26] if char in alphabet else char for char in self.msg])
        
class Vigenere(Cipher):
    def __init__(self, msg: str, keyword: str) -> None:
        super().__init__(msg, kind='vigenere')
        self.keyword = keyword
    
    def generate_keyphrase(self) -> str:
        keyphrase = ''
        for value in self.msg.split():
            for i in range(len(value)):
                keyphrase += self.keyword[i % len(self.keyword)]
            keyphrase += ' '
        return keyphrase
    
    def making_shifted_indexes(self) -> tuple[list[int], list[int]]:
        keyphrase = self.generate_keyphrase()
        find_indexes = lambda x: alphabet.find(x)
        return list(map(find_indexes, self.msg)), list(map(find_indexes, keyphrase))

    def code_message(self, encode: bool | None = True) -> str:
        bases, offsets = self.making_shifted_indexes()
        modified_offsets = [-num for num in offsets] if encode is None or encode == True else offsets
        final_indexes = [(bases[i] + modified_offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([alphabet[final_indexes[i]] if self.msg[i] in alphabet else self.msg[i] for i in range(len(self.msg))])