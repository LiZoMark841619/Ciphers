class Cipher:
    def __init__(self, msg: str, kind: str) -> None:
        self.msg = msg
        self.kind = kind

    def __str__(self) -> str:
        return f'Cipher({self.kind}) with message: {self.msg}'