class Cipher:
    
    def __init__(self, msg: str, kind: str):
        self.msg = msg
        self.kind = kind
        self.alpha = ''.join([chr(i) for i in range(97, 97+26)])

    def __str__(self) -> str:
        return f'{self.__class__.__base__.__name__}({self.kind}) object with original message: {self.msg}'