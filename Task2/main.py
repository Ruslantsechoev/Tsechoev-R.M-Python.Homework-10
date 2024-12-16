import random

from init_home import House
from init_person import Person


class Main:

    def __init__(self):
        house1 = House()
        man = Person(name='Bob', house=house1)
        woman = Person(name='Mila', house=house1)

        print(man)
        print(woman)
        print('\n')

        self.check_life_alone(person=man, house=house1)
        print("\n")
        self.check_life_together(man=man, woman=woman, house=house1)


    def check_life_alone(self, person, house):
        '''Метод по проверке жизни в течении 1 года одному'''

        days = 1
        while days != 365:
            if person.feed_hungry < 0:
                print(f'Человек умер, нужно попробовать еще раз!')
                break
            else:
                value_cube = random.randint(1, 6)
                if person.feed_hungry < 20:
                    person.eating(value_cube=value_cube)
                elif house.refrigerator_with_food < 10:
                    person.go_to_shop_for_food(value_cube=value_cube)
                elif house.bedside_table_with_money < 50:
                    person.working(value_cube=value_cube)
                elif value_cube == 2:
                    person.playing(value_cube=value_cube)
                elif value_cube == 1:
                    person.eating(value_cube=value_cube)

            days += 1

        if days == 365:
            print(f'\nЧеловек смог прожить {days} дней один, у него осталось еды - {house.refrigerator_with_food},'
                  f' денег осталось - {house.bedside_table_with_money}, чувство сытости - {person.feed_hungry}')
        else:
            print(f'\nЧеловек не смог прожить {days} дней один, у него осталось еды - {house.refrigerator_with_food},'
                  f'денег осталось - {house.bedside_table_with_money}, чувство сытости - {person.feed_hungry}')


    def check_life_together(self, man, woman, house):
        '''Метод по проверке жизни совместно в течение 1 года'''

        days = 1
        while days != 365:
            if man.feed_hungry < 0 or woman.feed_hungry < 0:
                print(f'Человек умер, нужно попробовать еще раз!')
                break
            else:
                value_cube_for_man = random.randint(1, 6)
                value_cube_for_woman = random.randint(1, 6)
                if man.feed_hungry < 20:
                    man.eating(value_cube=value_cube_for_man)
                elif woman.feed_hungry < 20:
                    woman.eating(value_cube=value_cube_for_woman)
                elif house.refrigerator_with_food < 10:
                    man.go_to_shop_for_food(value_cube=value_cube_for_man)
                elif house.bedside_table_with_money < 50:
                    man.working(value_cube=value_cube_for_man)
                    woman.working(value_cube=value_cube_for_woman)
                elif value_cube_for_man == 2:
                    man.playing(value_cube=value_cube_for_man)
                elif value_cube_for_woman == 2:
                    woman.playing(value_cube=value_cube_for_woman)
                elif value_cube_for_man == 1:
                    man.eating(value_cube=value_cube_for_man)
                elif value_cube_for_woman == 1:
                    woman.eating(value_cube=value_cube_for_woman)

            days += 1

        if days == 365:
            print(f'\nЛюди смогли прожить {days} дней вместе, у них осталось еды - {house.refrigerator_with_food},'
                  f' денег осталось - {house.bedside_table_with_money}, чувство сытости у мужчины - {man.feed_hungry},'
                  f'чувство сытости у женщины - {woman.feed_hungry}')
        else:
            print(f'\nЛюди не смогли прожить {days} дней вместе, у них осталось еды - {house.refrigerator_with_food},'
                  f'денег осталось - {house.bedside_table_with_money}, чувство сытости у мужчины - {man.feed_hungry},'
                  f'чувство сытости у женщины - {woman.feed_hungry}')


if __name__ == '__main__':
    main = Main()

