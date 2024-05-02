from ciphers import Cipher

class Caesar(Cipher):
    
    def __init__(self, msg: str, offset: int):
        super().__init__(msg, kind='caesar')
        self.offset = offset

    def decode_message(self) -> str:
        return ''.join([self.alpha[(self.alpha.find(char) + self.offset) % 26 ] if char in self.alpha else char for char in self.msg])
    
    def encode_message(self) -> str:
        return ''.join([self.alpha[(self.alpha.find(char) - self.offset) % 26 ] if char in self.alpha else char for char in self.msg])
