from caesar_vigenere import Caesar, Vigenere

class Valid:

    def get_valid_number(self, prompt: str, value_min: int, value_max: int) -> int:
        while True:
            try: 
                value = int(input(prompt))
                if value_min <= value <= value_max:
                    return value
                print('The number is out of range.\n')
            except ValueError: 
                print('Invalid value. Try again!\n')

    def get_valid_string(self, prompt: str, *args) -> str:
        while True:
            value = input(prompt).lower()
            if value in args:
                return value
            print('Invalid value. Try again! ')
            
class Game(Valid):

    def display(self) -> str:
        game, encryption = self.play()
        return game.decode_message() if encryption == 'decode' else game.encode_message()
    
    def play(self) -> tuple:
        cipher, message, encryption = self.set_game()
        if cipher == 'caesar': 
            return Caesar(message, self.get_valid_number('Enter the offset to shift the letters from 0-26! ', 0, 27)), encryption
        return Vigenere(message, input('Enter a keyword! ').lower()), encryption
            
    def set_game(self) -> tuple:
        cipher = self.get_valid_string('Chose from [caesar, vigenere] to start! ', 'caesar', 'vigenere')
        message = input('Enter a message you want to send! ').lower()
        encryption = self.get_valid_string('Chose from decode or encode! ', 'encode', 'decode')
        return cipher, message, encryption