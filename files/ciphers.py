class Cipher:
    
    def __init__(self, msg: str, kind: str) -> None:
        self.msg = msg
        self.kind = kind
        self.alpha = ''.join([chr(i) for i in range(97, 97+26)])

    def __str__(self) -> str:
        return f'Cipher({self.kind}) with original message: {self.msg}'