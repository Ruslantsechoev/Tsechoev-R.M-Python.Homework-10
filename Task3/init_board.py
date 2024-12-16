from init_cell import Cell

class Board:

    def __init__(self):
        self.cells = list(Cell(number=i) for i in range(10))







    def __str__(self):
        return (f'Massive cells = {self.cells}')



    def check_cell(self, number_cell: int, symbol: str):
        '''Метод по проверке занятости ячейки, если она не занята, то изменяет ее'''

        cell = self.cells[number_cell - 1]
        if cell.busy:
            return False

        cell.symbol = symbol
        cell.busy = True

        return True


    def check_game_over(self):
        comby_for_win = [(1, 2, 3), (4, 5, 6), (7, 8, 9),       # горизонтальные
                         (1, 4, 7), (2, 5, 8), (3, 6, 9),       # вертикальные
                         (1, 5, 9), (3, 5, 7)]                  # диагонали

        for position in comby_for_win:
            if (self.cells[position[0]].symbol != ' ' and
                self.cells[position[0]].symbol == self.cells[position[1]].symbol == self.cells[position[2]].symbol):
                return True

        return False



        # win_X = list()
        # win_O = list()
        # for i in range(len(self.cells)):
        #     if self.cells[i].symbol == 'X':
        #         win_X.append(i)
        #     elif self.cells[i].symbol == 'O':
        #         win_O.append(i)
        #
        # # print(win_X)
        # # print(win_O)
        #
        # if win_X in comby_for_win:
        #     # print("Выиграли Х")
        #     return True
        # elif win_O in comby_for_win:
        #     # print("Выиграли 0")
        #     return True
        # else:
        #     # print("Ничья!")
        #     return False


    def reset_board(self):
        '''Очистка игровой доски для новой игры'''
        for cell in self.cells:
            cell.symbol = ""
            cell.busy = False



    # def display_board(self):
    #     '''Метод по отображению игрового поля'''
    #
    #     board = '_____________\n'
    #     for i in range(10):
    #         if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
    #             board += '| '
    #             board += self.cells[i].symbol
    #             board += ' '
    #         elif i == 3 or i == 6:
    #             board += '| '
    #             board += self.cells[i].symbol
    #             board += " |"
    #             board += '\n'
    #             board += '-------------'
    #             board += '\n'
    #         elif i == 9:
    #             board += '| '
    #             board += self.cells[i].symbol
    #             board += ' |'
    #             board += '\n'
    #             board += '-------------'
    #
    #     print(board)


   # Второй вариант отображения доски
    def display_board(self):

        print("-------------")
        for i in range(0, 9, 3):
            print(f'| {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |')
        print("-------------")








# if __name__ == '__main__':
#     a = Board()
#     print(a.__str__())
#     a.display_board()
#     b = a.check_cell(number_cell=2)
#     print(b)
#     c = a.check_game_over()