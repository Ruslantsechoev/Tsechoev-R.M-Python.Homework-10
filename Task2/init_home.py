

class House:


    def __init__(self):
        self.refrigerator_with_food = 50                # изначально холодильник с едой = 50
        self.bedside_table_with_money = 0              # изначально тумбочка с деньгами = 0



    def check_house(self):
        self.refrigerator_with_food -= 5
        self.bedside_table_with_money += 10


    def __str__(self):
        return (f'В доме находится еды в холодильнике - {self.refrigerator_with_food} и '
                f'денег осталось в тумбочке - {self.bedside_table_with_money}')