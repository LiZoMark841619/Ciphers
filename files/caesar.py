from ciphers import Cipher

class Caesar(Cipher):
    
    def __init__(self, msg: str):
        super().__init__(msg, kind='caesar')

    def decode(self, offset: int) -> str:
        decoded = ''
        for char in self.msg:
            if char in self.alpha: decoded += self.alpha[(self.alpha.find(char) + offset) % 26]
            else: decoded += char
        return decoded
    
    def encode(self, offset: int) -> str:
        encoded = ''
        for char in self.msg:
            if char in self.alpha: encoded += self.alpha[(self.alpha.find(char) + offset) % 26]
            else: encoded += char
        return encoded