from game import Game
from init_player import Player
from init_board import Board


# class Main:
#
#     def start_games(self):

if __name__ == '__main__':
    man = Player(name='Игрок1', symbol='X')
    woman = Player(name='Игрок2', symbol='O')

    game = Game(player1=man, player2=woman)
    game.start_game()