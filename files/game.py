from caesar_vigenere import Caesar, Vigenere

class Valid:
    def get_valid_number(self, prompt: str, value_min: int, value_max: int) -> int:
        while True:
            try: 
                value = int(input(prompt))
                if value in range(value_min, value_max+1):
                    return value
                print('The number is out of range.\n')
            except ValueError: print('Invalid value. Try again!\n')

    def get_valid_string(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt).lower()
            if value in args:
                return value
            print('Invalid value. Try again! ')
            
class Game(Valid):
    def set_game(self) -> None:
        self.cipher = self.get_valid_string('Chose from [caesar, vigenere] to start! ', 'caesar', 'vigenere')
        self.message = input('Enter a message you want to send! ').lower()
        self.encryption = self.get_valid_string('Chose from decode or encode! ', 'encode', 'decode')
        
    def get_game(self) -> tuple:
        return self.cipher, self.message, self.encryption

    def set_offset(self) -> None:
        self.offset = self.get_valid_number('Enter the offset to shift the letters from 0-26! ', 0, 26)
    
    def get_offset(self) -> int:
        return self.offset
    
    def set_keyword(self) -> None:
        self.keyword = input('Enter your keyword! ').lower()
        
    def get_keyword(self) -> str:
        while not self.keyword.isalpha():
            print('Only letters are allowed to set the keyword! Try again!')
            self.set_keyword()
        return self.keyword
            
    def play(self) -> tuple:
        self.set_game()
        cipher, message, encryption = self.get_game()
        if cipher == 'caesar': 
            self.set_offset()
            return Caesar(message, self.get_offset()), encryption
        self.set_keyword()
        return Vigenere(message, self.get_keyword()), encryption
        
    def display(self) -> str:
        game, encryption = self.play()
        if encryption == 'encode':
            return game.code_message()
        return game.code_message(encode = False)