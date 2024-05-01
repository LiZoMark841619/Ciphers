from ciphers import Cipher

class Caesar(Cipher):
    
    def __init__(self, msg: str, offset: int):
        super().__init__(msg, kind='caesar')
        self.offset = offset

    def decode_message(self) -> str:
        decoded = ''
        for char in self.msg:
            if char in self.alpha: decoded += self.alpha[(self.alpha.find(char) + self.offset) % 26]
            else: decoded += char
        return decoded
    
    def encode_message(self) -> str:
        encoded = ''
        for char in self.msg:
            if char in self.alpha: encoded += self.alpha[(self.alpha.find(char) - self.offset) % 26]
            else: encoded += char
        return encoded