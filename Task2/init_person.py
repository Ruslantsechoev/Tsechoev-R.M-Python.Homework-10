from init_home import House

class Person:

    def __init__(self, name: str, house):

        self.house = house
        self.name = name
        self.feed_hungry = 50


    def eating(self, value_cube: int):
        '''Метод по приему пищи'''
        self.feed_hungry += value_cube
        self.house.refrigerator_with_food -= value_cube

        print(f'Настало время покушать, сытость стала - {self.feed_hungry},'
              f'еды стало - {self.house.refrigerator_with_food}')



    def working(self, value_cube: int):
        '''Метод по работе'''
        self.feed_hungry -= value_cube
        self.house.bedside_table_with_money += value_cube

        print(f'Нужно сходить на работу, чтобы подзаработать денюжек,'
              f' Денюжек стало - {self.house.bedside_table_with_money}, сытость составляет - {self.feed_hungry}')


    def playing(self, value_cube: int):
        '''Метод по игре'''
        self.feed_hungry -= value_cube

        print(f'Можно и поиграть, сытость теперь составляет - {self.feed_hungry}')


    def go_to_shop_for_food(self, value_cube: int):
        '''Метод по ходу в магазин за продуктами'''
        self.house.refrigerator_with_food += value_cube
        self.house.bedside_table_with_money -= value_cube

        print(f'Сходим в магазин и купим продукты, еды теперь стало - {self.house.refrigerator_with_food},'
              f'а количество денег стало - {self.house.bedside_table_with_money}')


    def __str__(self):
        return (f'Имя - {self.name}, живет в доме.  {self.house.__str__()}')


