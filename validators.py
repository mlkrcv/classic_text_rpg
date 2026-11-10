from datetime import datetime

def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print('A number must be greater than zero!')
        except ValueError:
            print('You can only enter a number. Please try again')

def get_valid_index(prompt: str, count: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if 0 < value <= count:
                return value - 1
            else:
                print('Please choose from presented options')
        except ValueError:
            print('You can only enter a number. Please try again')


def get_non_empty_string(prompt: str) -> str:
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print('You must enter a non-empty string!')

def get_valid_date(prompt: str) -> str:
    while True:
        value = (input(prompt))
        try:
            datetime.strptime(value, '%d/%m/%Y')
            return value
        except ValueError:
            print('Please enter a valid date')