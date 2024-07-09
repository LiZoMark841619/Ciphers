from ciphers import Cipher

class Caesar(Cipher):
    def __init__(self, msg: str, offset: int) -> None:
        super().__init__(msg, kind='caesar')
        self.offset = offset

    def decode_message(self) -> str:
        return ''.join([self.alpha[(self.alpha.find(char) + self.offset) % 26]
                        if char in self.alpha
                        else char for char in self.msg])
    
    def encode_message(self) -> str:
        return ''.join([self.alpha[(self.alpha.find(char) - self.offset) % 26]
                        if char in self.alpha
                        else char for char in self.msg])
        
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
        find_indexes = lambda x: self.alpha.find(x)
        return list(map(find_indexes, list(self.msg))), list(map(find_indexes, list(keyphrase)))

    def decode_message(self) -> str:
        bases, offsets = self.making_shifted_indexes()
        final_indexes = [(bases[i] - offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([self.alpha[final_indexes[i]]
                        if self.msg[i] in self.alpha
                        else self.msg[i] for i in range(len(self.msg))])
    
    def encode_message(self) -> str:
        bases, offsets = self.making_shifted_indexes()
        final_indexes = [(bases[i] + offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([self.alpha[final_indexes[i]]
                        if self.msg[i] in self.alpha
                        else self.msg[i] for i in range(len(self.msg))])