

class Cell:

    def __init__(self, number):
        self.number = number
        self.busy = False
        self.symbol = ''   # Тут будет либо X, либо 0, либо ''


    def __str__(self):
        return (f'номер - {self.number}, занятость клетки - {self.busy}, символ, '
                f'который хранится в этой клетке - {self.symbol}')
