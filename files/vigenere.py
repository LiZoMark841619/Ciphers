from ciphers import Cipher

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
    
    def making_shifted_indexes(self) -> tuple:
        keyphrase = self.generate_keyphrase()
        f = lambda x: self.alpha.find(x)
        bases, offsets = list(map(f, list(self.msg))), list(map(f, list(keyphrase)))
        return bases, offsets
    
    def decode_message(self) -> str:
        bases, offsets = self.making_shifted_indexes()
        final_indexes = [(bases[i] - offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([self.alpha[final_indexes[i]] if self.msg[i] in self.alpha else self.msg[i] for i in range(len(self.msg))])
    
    def encode_message(self) -> str:
        bases, offsets = self.making_shifted_indexes()
        final_indexes = [(bases[i] + offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([self.alpha[final_indexes[i]] if self.msg[i] in self.alpha else self.msg[i] for i in range(len(self.msg))])