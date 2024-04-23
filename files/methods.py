def get_valid_number(prompt: str, value_min: int, value_max: int) -> int:
    while True:
        try: 
            value = int(input(prompt))
            if value_min <= value <= value_max:
                return value
            else:
                print('The number is out of range.\n')
        except ValueError: 
            print('Enter a valid number!\n')

def get_valid_str(prompt: str, *args) -> str:
    while True:
        value = input(prompt).lower()
        if value in args:
            return value
        else:
            print('Invalid value. Try again! ')