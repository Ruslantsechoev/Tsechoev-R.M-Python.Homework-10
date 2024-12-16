

class Player:

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.wins = 0


    def move_player(self):
        '''Метод по запросу хода игрока'''

        while True:
            move = int(input(f"{self.name} введите номер клетки для хода (1-9): "))

            if move < 1:
                print("Неправильный ввод, ячейки меньше 1 - нет, пожалуйста повторите ввод")
                return move
            elif move > 9:
                print("Неправильный ввод, ячейки больще 9 - нет, пожалуйста повторите ввод")
                return move
            else:
                return True


    def __str__(self):
        return (f'Имя - {self.name}, символ - {self.symbol}, побед - {self.wins}')