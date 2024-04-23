from ciphers import Cipher

class Vigenere(Cipher):
    
    def __init__(self, msg: str, keyword: str) -> None:
        super().__init__(msg, kind='vigenere')
        self.keyword = keyword
    
    def key_gen(self) -> str:
        key_phrase = ''
        for value in self.msg.split():
            for i in range(len(value)):
                key_phrase += self.keyword[i % len(self.keyword)]
            key_phrase += ' '
        return key_phrase
    
    def new_loc(self) -> tuple:
        key_phrase = self.key_gen()
        f = lambda x: self.alpha.find(x)
        bases, offsets = list(map(f, list(self.msg))), list(map(f, list(key_phrase)))
        return bases, offsets
    
    def decode(self):
        bases, offsets = self.new_loc()
        fin_idx = [(bases[i] - offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([self.alpha[fin_idx[i]] if self.msg[i] in self.alpha else self.msg[i] for i in range(len(self.msg))])
    
    def encode(self):
        bases, offsets = self.new_loc()
        fin_idx = [(bases[i] + offsets[i]) % 26 for i in range(len(bases))]
        return ''.join([self.alpha[fin_idx[i]] if self.msg[i] in self.alpha else self.msg[i] for i in range(len(self.msg))])
