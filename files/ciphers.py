class Cipher:
    
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.msg})'