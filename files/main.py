from methods import Valid
from caesar import Caesar
from vigenere import Vigenere

class Game(Valid):

    def display(self):
        game, encryption = self.play()
        return game.decode_message() if encryption == 'decode' else game.encode_message()
    
    def play(self):
        cipher, message, encryption = self.set_game()
        if cipher == 'caesar': 
            game = Caesar(message, self.get_valid_number('Enter the offset to shift the letters from 0-26! ', 0, 27))
        else:
            game = Vigenere(message, input('Enter a keyword! ').lower())
        return game, encryption
    
    def set_game(self):
        cipher = self.get_valid_string('Chose from [caesar, vigenere] to start! ', 'caesar', 'vigenere')
        message = input('Enter a message you want to send! ').lower()
        encryption = self.get_valid_string('Chose from decode or encode! ', 'encode', 'decode')
        return cipher, message, encryption
    
if __name__ == '__main__':
    game = Game()
    print(game.display())