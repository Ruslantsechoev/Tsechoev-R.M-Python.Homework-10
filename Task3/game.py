from init_player import Player
from init_board import Board

class Game:

    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.board = Board()


    def move_launch(self, player: Player):
        '''Метод по ходу одного игрока'''

        while True:
            self.board.display_board()
            number_cell = player.move_player()

            if self.board.check_cell(number_cell=number_cell, symbol=player.symbol):
                if self.board.check_game_over():
                    return True

                return False
            print(f'Клетка занята, сделайте другой ход')



    def play_one_game(self):
        '''Метод по проведению одной игры до победы одного из игроков или ничьи'''

        print('Игра началась!')
        while True:
            for player in self.players:
                if self.move_launch(player=player):
                    self.board.display_board()
                    print(f'Поздравляем - {player.name}! Вы выиграли!')
                    player.wins += 1
                    return

                if all(cell.busy for cell in self.board.cells):
                    self.board.display_board()
                    print("Ничья!")
                    return


    def start_game(self):
        '''Метод по запуску игр'''

        print('ДОПРО ПОЖАЛОВАТЬ В ИГРУ КРЕСТИКИ-НОЛИКИ!')
        while True:
            self.board.reset_board()
            self.play_one_game()
            print(f'Счет: {self.players[0].name} - {self.players[0].wins}, '
                  f'      {self.players[1].name} - {self.players[1].wins}')

            again_game = input("Хотите сыграть еще раз? (да/нет): ").lower()
            if again_game == 'нет' or again_game == 'no':
                print('Спасибо за игру!')
                break



    def __str__(self):
        return (f'Massive player - {self.players.__str__()}')



